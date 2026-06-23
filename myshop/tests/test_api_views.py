from __future__ import annotations

from decimal import Decimal
from typing import cast

import pytest
from rest_framework.test import APIClient

from orders.models import Order, OrderStatus
from products.models import Category, Product, Review
from users.models import Address


pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def category() -> Category:
    return cast(Category, Category.objects.create(name="Extracts", slug="extracts"))


@pytest.fixture
def products(category: Category) -> tuple[Product, Product, Product]:
    first = cast(
        Product,
        Product.objects.create(
            name="Amber Malt Extract",
            slug="amber-malt-extract",
            description="Rich malt extract for amber ales.",
            price=Decimal("14.00"),
            category=category,
            stock=10,
        ),
    )
    second = cast(
        Product,
        Product.objects.create(
            name="Pilsner Extract",
            slug="pilsner-extract",
            description="Bright and crisp base for lighter beers.",
            price=Decimal("12.50"),
            category=category,
            stock=8,
        ),
    )
    third = cast(
        Product,
        Product.objects.create(
            name="Dark Candi Syrup",
            slug="dark-candi-syrup",
            description="Deep caramelized syrup for Belgian styles.",
            price=Decimal("9.75"),
            category=category,
            stock=6,
        ),
    )
    return first, second, third


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="api-user",
        email="api-user@example.com",
        password="strong-password-123",
        first_name="Api",
        last_name="User",
    )


@pytest.fixture
def other_user(django_user_model):
    return django_user_model.objects.create_user(
        username="other-user",
        email="other@example.com",
        password="strong-password-123",
    )


def authenticate_with_jwt(client: APIClient, username: str, password: str) -> dict[str, str]:
    response = client.post(
        "/api/users/login/",
        {"username": username, "password": password},
        format="json",
    )
    assert response.status_code == 200
    tokens = cast(dict[str, str], response.json())
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
    return tokens


def test_api_user_registration_and_token_refresh(api_client: APIClient) -> None:
    register_response = api_client.post(
        "/api/users/register/",
        {
            "username": "registered-user",
            "password": "VeryStrongPass123",
            "email": "registered@example.com",
            "first_name": "Registered",
            "last_name": "User",
        },
        format="json",
    )

    assert register_response.status_code == 201
    assert register_response.json()["username"] == "registered-user"

    login_response = api_client.post(
        "/api/users/login/",
        {"username": "registered-user", "password": "VeryStrongPass123"},
        format="json",
    )

    assert login_response.status_code == 200
    tokens = login_response.json()
    assert "access" in tokens
    assert "refresh" in tokens

    refresh_response = api_client.post(
        "/api/users/token/refresh/",
        {"refresh": tokens["refresh"]},
        format="json",
    )

    assert refresh_response.status_code == 200
    assert "access" in refresh_response.json()


def test_api_product_list_supports_pagination_filter_and_search(
    api_client: APIClient,
    category: Category,
    products: tuple[Product, Product, Product],
) -> None:
    first, _, _ = products

    response = api_client.get(
        "/api/products/",
        {"q": "amber", "category": category.slug, "min_price": "10.00"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["count"] == 1
    assert payload["results"][0]["name"] == first.name


def test_api_product_detail_returns_reviews(api_client: APIClient, products, user) -> None:
    first, _, _ = products
    Review.objects.create(product=first, user=user, rating=5, comment="Great extract.")

    response = api_client.get(f"/api/products/{first.pk}/")

    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == first.pk
    assert payload["review_count"] == 1
    assert payload["reviews"][0]["username"] == user.username


def test_api_cart_crud_uses_session_state(api_client: APIClient, products) -> None:
    first, _, _ = products

    add_response = api_client.post(
        "/api/cart/",
        {"product_id": first.pk, "quantity": 2},
        format="json",
    )
    assert add_response.status_code == 201
    assert add_response.json()["cart"]["total_quantity"] == 2

    update_response = api_client.patch(
        "/api/cart/",
        {"product_id": first.pk, "quantity": 3},
        format="json",
    )
    assert update_response.status_code == 200
    assert update_response.json()["cart"]["subtotal"] == "42.00"

    get_response = api_client.get("/api/cart/")
    assert get_response.status_code == 200
    assert get_response.json()["lines"][0]["product_id"] == first.pk

    delete_response = api_client.delete(
        "/api/cart/",
        {"product_id": first.pk},
        format="json",
    )
    assert delete_response.status_code == 200
    assert delete_response.json()["cart"]["is_empty"] is True


def test_api_orders_require_authentication(api_client: APIClient) -> None:
    response = api_client.get("/api/orders/")

    assert response.status_code == 401


def test_api_order_create_from_cart_with_jwt_and_address(
    api_client: APIClient,
    user,
    products,
) -> None:
    first, second, _ = products
    address = Address.objects.create(
        user=user,
        label="Home",
        recipient_name="Api User",
        phone="+380501112233",
        address_line1="42 Brewery Lane",
        city="Kyiv",
        postal_code="02000",
        country="Ukraine",
        is_default=True,
    )
    session = api_client.session
    session["cart"] = {str(first.pk): 2, str(second.pk): 1}
    session.save()
    authenticate_with_jwt(api_client, user.username, "strong-password-123")

    response = api_client.post(
        "/api/orders/",
        {"address_id": address.pk},
        format="json",
    )

    assert response.status_code == 201
    payload = response.json()
    assert payload["status"] == OrderStatus.PENDING
    assert payload["total_price"] == "40.50"
    assert len(payload["items"]) == 2
    first.refresh_from_db()
    second.refresh_from_db()
    assert first.stock == 8
    assert second.stock == 7
    assert api_client.session.get("cart", {}) == {}


def test_api_order_list_and_detail_are_scoped_to_current_user(
    api_client: APIClient,
    user,
    other_user,
    products,
) -> None:
    first, _, _ = products
    own_order = Order.objects.create(
        user=user,
        status=OrderStatus.PAID,
        total_price=Decimal("28.00"),
        shipping_address="Own address",
    )
    other_order = Order.objects.create(
        user=other_user,
        status=OrderStatus.PAID,
        total_price=Decimal("14.00"),
        shipping_address="Other address",
    )
    own_order.items.create(product=first, quantity=2, price=Decimal("14.00"))
    other_order.items.create(product=first, quantity=1, price=Decimal("14.00"))
    authenticate_with_jwt(api_client, user.username, "strong-password-123")

    list_response = api_client.get("/api/orders/")
    detail_response = api_client.get(f"/api/orders/{own_order.pk}/")
    forbidden_detail = api_client.get(f"/api/orders/{other_order.pk}/")

    assert list_response.status_code == 200
    assert list_response.json()["count"] == 1
    assert detail_response.status_code == 200
    assert detail_response.json()["id"] == own_order.pk
    assert forbidden_detail.status_code == 404


def test_api_order_update_and_delete_cancel_with_status_rules(
    api_client: APIClient,
    user,
    products,
) -> None:
    first, _, _ = products
    order = Order.objects.create(
        user=user,
        status=OrderStatus.PENDING,
        total_price=Decimal("14.00"),
        shipping_address="Api address",
    )
    order.items.create(product=first, quantity=1, price=Decimal("14.00"))
    authenticate_with_jwt(api_client, user.username, "strong-password-123")

    patch_response = api_client.patch(
        f"/api/orders/{order.pk}/",
        {"status": OrderStatus.CANCELLED},
        format="json",
    )
    order.refresh_from_db()
    assert patch_response.status_code == 200
    assert order.status == OrderStatus.CANCELLED

    delete_response = api_client.delete(f"/api/orders/{order.pk}/")
    assert delete_response.status_code == 400


def test_api_review_create_requires_purchase_and_auth(
    api_client: APIClient,
    user,
    products,
) -> None:
    first, _, _ = products

    anonymous_response = api_client.post(
        f"/api/products/{first.pk}/reviews/",
        {"rating": 5, "comment": "Excellent."},
        format="json",
    )
    assert anonymous_response.status_code == 401

    authenticate_with_jwt(api_client, user.username, "strong-password-123")
    no_purchase_response = api_client.post(
        f"/api/products/{first.pk}/reviews/",
        {"rating": 5, "comment": "Excellent."},
        format="json",
    )
    assert no_purchase_response.status_code == 400

    order = Order.objects.create(
        user=user,
        status=OrderStatus.PAID,
        total_price=Decimal("14.00"),
        shipping_address="Api address",
    )
    order.items.create(product=first, quantity=1, price=Decimal("14.00"))

    purchased_response = api_client.post(
        f"/api/products/{first.pk}/reviews/",
        {"rating": 4, "comment": "Purchased and enjoyed."},
        format="json",
    )

    assert purchased_response.status_code == 201
    assert Review.objects.filter(
        product=first,
        user=user,
        rating=4,
    ).exists()
