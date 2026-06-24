from __future__ import annotations

from decimal import Decimal
from unittest.mock import patch

import pytest
from django.core import mail
from django.urls import reverse

from orders.models import Order, OrderItem, OrderStatus
from products.models import Category, Product


pytestmark = pytest.mark.django_db


@pytest.fixture
def checkout_user(django_user_model):
    return django_user_model.objects.create_user(
        username="checkout-user",
        email="buyer@example.com",
        password="strong-password-123",
    )


@pytest.fixture
def checkout_products() -> tuple[Product, Product]:
    category = Category.objects.create(name="Yeast", slug="yeast")
    first = Product.objects.create(
        name="House Ale Yeast",
        slug="house-ale-yeast",
        description="Clean fermentation profile for everyday brewing.",
        price=Decimal("7.50"),
        category=category,
        stock=5,
    )
    second = Product.objects.create(
        name="Citrus Hop Blend",
        slug="citrus-hop-blend",
        description="Bright aroma hops for late additions and dry hopping.",
        price=Decimal("12.00"),
        category=category,
        stock=4,
    )
    return first, second


def checkout_payload(**overrides: str) -> dict[str, str]:
    payload = {
        "full_name": "Alex Brewer",
        "email": "alex@example.com",
        "phone": "+380501112233",
        "address_line1": "42 Fermentation Lane",
        "address_line2": "Apt 7",
        "city": "Kyiv",
        "postal_code": "02000",
        "country": "Ukraine",
        "payment_method": "card",
    }
    payload.update(overrides)
    return payload


def test_checkout_page_renders_summary_and_form(client, checkout_products) -> None:
    first, _ = checkout_products
    user = client.session
    user["cart"] = {str(first.id): 2}
    user.save()

    response = client.get(reverse("checkout-detail"))

    assert response.status_code == 302
    assert response.url == f"{reverse('login')}?next={reverse('checkout-detail')}"


def test_checkout_page_renders_summary_and_form_for_authenticated_user(
    client,
    checkout_user,
    checkout_products,
) -> None:
    first, _ = checkout_products
    client.force_login(checkout_user)
    session = client.session
    session["cart"] = {str(first.id): 2}
    session.save()

    response = client.get(reverse("checkout-detail"))

    assert response.status_code == 200
    assert b"Confirm your order" in response.content
    assert b"House Ale Yeast" in response.content
    assert b"Mock payment method" in response.content


def test_checkout_submit_requires_authenticated_user(client, checkout_products) -> None:
    first, _ = checkout_products
    session = client.session
    session["cart"] = {str(first.id): 1}
    session.save()

    response = client.post(reverse("checkout-submit"), checkout_payload(), follow=True)

    assert response.status_code == 200
    assert Order.objects.count() == 0
    assert response.redirect_chain[-1][0].endswith(
        f"{reverse('login')}?next={reverse('checkout-detail')}"
    )
    assert b"Sign in before placing an order." in response.content


def test_checkout_submit_validates_form_input(client, checkout_user, checkout_products) -> None:
    first, _ = checkout_products
    client.force_login(checkout_user)
    session = client.session
    session["cart"] = {str(first.id): 1}
    session.save()

    response = client.post(
        reverse("checkout-submit"),
        checkout_payload(full_name="", email="not-an-email"),
    )

    assert response.status_code == 400
    assert Order.objects.count() == 0
    assert b"Please correct the checkout form errors below." in response.content


def test_checkout_creates_order_items_sends_emails_and_clears_cart(
    client,
    settings,
    checkout_user,
    checkout_products,
) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    settings.ADMINS = [("Store Admin", "admin@example.com")]
    mail.outbox.clear()
    first, second = checkout_products
    client.force_login(checkout_user)
    session = client.session
    session["cart"] = {str(first.id): 2, str(second.id): 1}
    session.save()

    response = client.post(reverse("checkout-submit"), checkout_payload(), follow=True)

    assert response.status_code == 200
    order = Order.objects.get()
    items = list(order.items.order_by("id"))

    assert order.user == checkout_user
    assert order.status == OrderStatus.PENDING
    assert order.total_price == Decimal("27.00")
    assert "Alex Brewer" in order.shipping_address
    assert "Payment method: Card on delivery" in order.shipping_address
    assert len(items) == 2
    assert [(item.product_id, item.quantity, item.price) for item in items] == [
        (first.id, 2, Decimal("7.50")),
        (second.id, 1, Decimal("12.00")),
    ]
    first.refresh_from_db()
    second.refresh_from_db()
    assert first.stock == 3
    assert second.stock == 3
    assert client.session.get("cart", {}) == {}
    assert len(mail.outbox) == 2
    assert mail.outbox[0].to == ["alex@example.com"]
    assert mail.outbox[1].to == ["admin@example.com"]
    assert response.redirect_chain[-1][0].endswith(
        reverse("account-order-detail", kwargs={"pk": order.pk})
    )
    assert f"Order #{order.pk}".encode() in response.content
    assert b"placed successfully" in response.content


def test_checkout_rejects_insufficient_stock_and_keeps_cart(
    client,
    settings,
    checkout_user,
    checkout_products,
) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    settings.ADMINS = []
    mail.outbox.clear()
    first, _ = checkout_products
    Product.objects.filter(pk=first.pk).update(stock=1)

    client.force_login(checkout_user)
    session = client.session
    session["cart"] = {str(first.id): 2}
    session.save()

    response = client.post(reverse("checkout-submit"), checkout_payload())

    assert response.status_code == 400
    assert Order.objects.count() == 0
    assert client.session["cart"][str(first.id)] == 2
    assert b"Insufficient stock for House Ale Yeast. Only 1 left." in response.content
    assert len(mail.outbox) == 0


def test_checkout_rolls_back_when_order_item_creation_fails(
    client,
    settings,
    checkout_user,
    checkout_products,
) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    settings.ADMINS = []
    mail.outbox.clear()
    first, _ = checkout_products
    client.force_login(checkout_user)
    session = client.session
    session["cart"] = {str(first.id): 2}
    session.save()

    with patch("orders.services.OrderItem.objects.create", side_effect=RuntimeError("boom")):
        response = client.post(reverse("checkout-submit"), checkout_payload())

    assert response.status_code == 500
    assert Order.objects.count() == 0
    assert OrderItem.objects.count() == 0
    first.refresh_from_db()
    assert first.stock == 5
    assert client.session["cart"][str(first.id)] == 2
    assert b"We could not place your order right now. Please try again." in response.content
    assert len(mail.outbox) == 0
