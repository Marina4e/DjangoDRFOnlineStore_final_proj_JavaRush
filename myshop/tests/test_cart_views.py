from __future__ import annotations

from decimal import Decimal
from typing import cast

import pytest
from django.urls import reverse

from products.models import Category, Product


pytestmark = pytest.mark.django_db


@pytest.fixture
def cart_product() -> Product:
    category = Category.objects.create(name="Adjuncts", slug="adjuncts")
    return cast(
        Product,
        Product.objects.create(
            name="Orange Blossom Honey",
            slug="orange-blossom-honey",
            description="Floral fermentable addition for specialty brews.",
            price=Decimal("11.25"),
            category=category,
            stock=8,
        ),
    )


def test_cart_page_renders_empty_state(client) -> None:
    response = client.get(reverse("cart-detail"))

    assert response.status_code == 200
    assert b"Your cart is empty" in response.content


def test_add_to_cart_stores_session_data(client, cart_product) -> None:
    response = client.post(
        reverse("cart-add", kwargs={"product_id": cart_product.id}),
        {"quantity": "2", "next": reverse("product-detail", kwargs={"slug": cart_product.slug})},
    )

    assert response.status_code == 302
    assert client.session["cart"][str(cart_product.id)] == 2


def test_cart_page_shows_added_product_and_total(client, cart_product) -> None:
    session = client.session
    session["cart"] = {str(cart_product.id): 3}
    session.save()

    response = client.get(reverse("cart-detail"))

    assert response.status_code == 200
    assert b"Orange Blossom Honey" in response.content
    assert b"$33.75" in response.content


def test_cart_update_changes_quantity_and_persists(client, cart_product) -> None:
    session = client.session
    session["cart"] = {str(cart_product.id): 1}
    session.save()

    response = client.post(
        reverse("cart-update", kwargs={"product_id": cart_product.id}),
        {"quantity": "4"},
        HTTP_HX_REQUEST="true",
    )

    assert response.status_code == 200
    assert client.session["cart"][str(cart_product.id)] == 4
    assert b"Updated Orange Blossom Honey quantity to 4." in response.content


def test_cart_remove_deletes_item_from_session(client, cart_product) -> None:
    session = client.session
    session["cart"] = {str(cart_product.id): 2}
    session.save()

    response = client.post(
        reverse("cart-remove", kwargs={"product_id": cart_product.id}),
        HTTP_HX_REQUEST="true",
    )

    assert response.status_code == 200
    assert str(cart_product.id) not in client.session.get("cart", {})
    assert b"Your cart is empty" in response.content


def test_add_to_cart_rejects_quantity_over_stock(client, cart_product) -> None:
    response = client.post(
        reverse("cart-add", kwargs={"product_id": cart_product.id}),
        {"quantity": "12", "next": reverse("product-detail", kwargs={"slug": cart_product.slug})},
        follow=True,
    )

    assert response.status_code == 200
    assert str(cart_product.id) not in client.session.get("cart", {})
    assert b"Requested quantity exceeds available stock." in response.content


def test_cart_update_rejects_quantity_over_stock(client, cart_product) -> None:
    session = client.session
    session["cart"] = {str(cart_product.id): 2}
    session.save()

    response = client.post(
        reverse("cart-update", kwargs={"product_id": cart_product.id}),
        {"quantity": "20"},
        HTTP_HX_REQUEST="true",
    )

    assert response.status_code == 400
    assert client.session["cart"][str(cart_product.id)] == 2
    assert b"Requested quantity exceeds available stock." in response.content


def test_cart_summary_uses_current_product_price(client, cart_product) -> None:
    session = client.session
    session["cart"] = {str(cart_product.id): 2}
    session.save()

    Product.objects.filter(pk=cart_product.pk).update(price=Decimal("13.00"))

    response = client.get(reverse("cart-detail"))

    assert response.status_code == 200
    assert b"$26.00" in response.content
