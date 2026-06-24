from __future__ import annotations

from decimal import Decimal
from typing import cast

import pytest
from django.urls import reverse

from orders.models import Order, OrderStatus
from products.models import Category, Product
from users.models import Address


pytestmark = pytest.mark.django_db


@pytest.fixture
def category() -> Category:
    return cast(Category, Category.objects.create(name="Hops", slug="hops"))


@pytest.fixture
def product(category: Category) -> Product:
    return cast(
        Product,
        Product.objects.create(
            name="Cascade Hops",
            slug="cascade-hops",
            description="Classic aroma hops for citrus-forward ales.",
            price=Decimal("8.00"),
            category=category,
            stock=12,
        ),
    )


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="alice",
        email="alice@example.com",
        password="strong-password-123",
        first_name="Alice",
        last_name="Brewer",
    )


@pytest.fixture
def other_user(django_user_model):
    return django_user_model.objects.create_user(
        username="other",
        email="other@example.com",
        password="strong-password-123",
    )


def test_registration_creates_user_logs_them_in_and_redirects(client) -> None:
    response = client.post(
        reverse("register"),
        {
            "username": "new-user",
            "first_name": "New",
            "last_name": "User",
            "email": "new@example.com",
            "password1": "UltraStrongPass123",
            "password2": "UltraStrongPass123",
        },
        follow=True,
    )

    assert response.status_code == 200
    assert response.wsgi_request.user.is_authenticated
    assert response.wsgi_request.user.username == "new-user"
    assert b"Your account has been created." in response.content
    assert b"Order history" in response.content


def test_login_and_logout_flow_uses_session_auth(client, user) -> None:
    login_response = client.post(
        reverse("login"),
        {"username": user.username, "password": "strong-password-123"},
        follow=True,
    )

    assert login_response.status_code == 200
    assert login_response.wsgi_request.user.is_authenticated
    assert b"Welcome back." in login_response.content

    logout_response = client.post(reverse("logout"), follow=True)

    assert logout_response.status_code == 200
    assert not logout_response.wsgi_request.user.is_authenticated
    assert b"You have been signed out." in logout_response.content


def test_account_page_requires_login(client) -> None:
    response = client.get(reverse("account-detail"))

    assert response.status_code == 302
    assert response.url == f"{reverse('login')}?next={reverse('account-detail')}"


def test_profile_update_changes_current_user(client, user) -> None:
    client.force_login(user)

    response = client.post(
        reverse("account-profile-update"),
        {
            "first_name": "Alicia",
            "last_name": "Hopkins",
            "email": "alicia@example.com",
        },
        follow=True,
    )

    user.refresh_from_db()

    assert response.status_code == 200
    assert user.first_name == "Alicia"
    assert user.last_name == "Hopkins"
    assert user.email == "alicia@example.com"
    assert b"Your profile has been updated." in response.content


def test_password_change_updates_credentials_and_keeps_access(client, user) -> None:
    client.force_login(user)

    response = client.post(
        reverse("password-change"),
        {
            "old_password": "strong-password-123",
            "new_password1": "NewStrongPassword123",
            "new_password2": "NewStrongPassword123",
        },
        follow=True,
    )

    user.refresh_from_db()

    assert response.status_code == 200
    assert user.check_password("NewStrongPassword123")
    assert b"Password updated" in response.content


def test_account_order_history_is_scoped_to_user_and_filterable(
    client,
    user,
    other_user,
    product,
) -> None:
    own_pending = Order.objects.create(
        user=user,
        status=OrderStatus.PENDING,
        total_price=Decimal("24.00"),
        shipping_address="Pending address",
    )
    own_paid = Order.objects.create(
        user=user,
        status=OrderStatus.PAID,
        total_price=Decimal("16.00"),
        shipping_address="Paid address",
    )
    Order.objects.create(
        user=other_user,
        status=OrderStatus.PAID,
        total_price=Decimal("32.00"),
        shipping_address="Other address",
    )
    own_pending.items.create(product=product, quantity=3, price=Decimal("8.00"))
    own_paid.items.create(product=product, quantity=2, price=Decimal("8.00"))

    client.force_login(user)

    response = client.get(reverse("account-detail"), {"status": OrderStatus.PAID})

    assert response.status_code == 200
    assert f"Order #{own_paid.pk}".encode() in response.content
    assert f"Order #{own_pending.pk}".encode() not in response.content
    assert b"Other address" not in response.content


def test_my_orders_page_requires_login(client) -> None:
    response = client.get(reverse("account-orders"))

    assert response.status_code == 302
    assert response.url == f"{reverse('login')}?next={reverse('account-orders')}"


def test_my_orders_page_shows_only_current_users_orders_with_items(
    client,
    user,
    other_user,
    product,
) -> None:
    own_order = Order.objects.create(
        user=user,
        status=OrderStatus.PAID,
        total_price=Decimal("24.00"),
        shipping_address="Alice address",
    )
    own_order.items.create(product=product, quantity=3, price=Decimal("8.00"))
    other_order = Order.objects.create(
        user=other_user,
        status=OrderStatus.SHIPPED,
        total_price=Decimal("16.00"),
        shipping_address="Other address",
    )
    other_order.items.create(product=product, quantity=2, price=Decimal("8.00"))

    client.force_login(user)

    response = client.get(reverse("account-orders"))

    assert response.status_code == 200
    assert b"My orders" in response.content
    assert f"Order #{own_order.pk}".encode() in response.content
    assert f"Order #{other_order.pk}".encode() not in response.content
    assert b"Cascade Hops" in response.content
    assert b"$24.00" in response.content
    assert b"Other address" not in response.content


def test_order_detail_page_is_owner_scoped(client, user, other_user, product) -> None:
    own_order = Order.objects.create(
        user=user,
        status=OrderStatus.PAID,
        total_price=Decimal("24.00"),
        shipping_address="Alice address",
    )
    own_order.items.create(product=product, quantity=3, price=Decimal("8.00"))
    other_order = Order.objects.create(
        user=other_user,
        status=OrderStatus.PAID,
        total_price=Decimal("16.00"),
        shipping_address="Other address",
    )
    other_order.items.create(product=product, quantity=2, price=Decimal("8.00"))

    client.force_login(user)

    own_response = client.get(reverse("account-order-detail", kwargs={"pk": own_order.pk}))
    other_response = client.get(reverse("account-order-detail", kwargs={"pk": other_order.pk}))

    assert own_response.status_code == 200
    assert b"Order #" in own_response.content
    assert b"Cascade Hops" in own_response.content
    assert b"$8.00" in own_response.content
    assert b"$24.00" in own_response.content
    assert other_response.status_code == 404


def test_address_crud_and_default_switching_work_for_owner(client, user) -> None:
    client.force_login(user)

    create_response = client.post(
        reverse("address-create"),
        {
            "label": "Home",
            "recipient_name": "Alice Brewer",
            "phone": "+380501112233",
            "address_line1": "123 Hop Street",
            "address_line2": "",
            "city": "Kyiv",
            "postal_code": "02000",
            "country": "Ukraine",
            "is_default": "on",
        },
        follow=True,
    )

    address = Address.objects.get(user=user, label="Home")

    assert create_response.status_code == 200
    assert address.is_default is True
    assert b"Address saved to your account." in create_response.content

    second_address = Address.objects.create(
        user=user,
        label="Office",
        recipient_name="Alice Brewer",
        phone="+380501112233",
        address_line1="1 Brew Ave",
        city="Kyiv",
        postal_code="01001",
        country="Ukraine",
    )

    update_response = client.post(
        reverse("address-update", kwargs={"pk": second_address.pk}),
        {
            "label": "Office",
            "recipient_name": "Alice Brewer",
            "phone": "+380501112233",
            "address_line1": "1 Brew Ave",
            "address_line2": "Suite 5",
            "city": "Kyiv",
            "postal_code": "01001",
            "country": "Ukraine",
            "is_default": "on",
        },
        follow=True,
    )

    address.refresh_from_db()
    second_address.refresh_from_db()

    assert update_response.status_code == 200
    assert second_address.is_default is True
    assert address.is_default is False
    assert second_address.address_line2 == "Suite 5"

    delete_response = client.post(
        reverse("address-delete", kwargs={"pk": address.pk}),
        follow=True,
    )

    assert delete_response.status_code == 200
    assert not Address.objects.filter(pk=address.pk).exists()


def test_address_edit_is_restricted_to_owner(client, user, other_user) -> None:
    address = Address.objects.create(
        user=other_user,
        label="Private",
        recipient_name="Other User",
        phone="+380000000000",
        address_line1="Secret 1",
        city="Lviv",
        postal_code="79000",
        country="Ukraine",
    )
    client.force_login(user)

    response = client.get(reverse("address-update", kwargs={"pk": address.pk}))

    assert response.status_code == 404


def test_address_delete_redirects_anonymous_user_to_login(client, user) -> None:
    address = Address.objects.create(
        user=user,
        label="Home",
        recipient_name="Alice Brewer",
        phone="+380501112233",
        address_line1="123 Hop Street",
        city="Kyiv",
        postal_code="02000",
        country="Ukraine",
    )
    response = client.post(reverse("address-delete", kwargs={"pk": address.pk}))

    assert response.status_code == 302
    expected_next = reverse("address-delete", kwargs={"pk": address.pk})
    assert response.url == f"{reverse('login')}?next={expected_next}"
