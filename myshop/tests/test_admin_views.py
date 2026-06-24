from __future__ import annotations

from decimal import Decimal

import pytest
from django.contrib.auth.models import Permission
from django.urls import reverse

from orders.models import Order, OrderItem, OrderStatus
from products.models import Category, Product


pytestmark = pytest.mark.django_db


def test_admin_redirects_authenticated_non_staff_user(client, django_user_model) -> None:
    user = django_user_model.objects.create_user(
        username="member",
        email="member@example.com",
        password="strong-password-123",
    )
    client.force_login(user)

    response = client.get(reverse("admin:index"))

    assert response.status_code == 302
    assert reverse("admin:login") in response.headers["Location"]


def test_staff_user_can_see_order_admin_analytics(client, django_user_model) -> None:
    staff_user = django_user_model.objects.create_user(
        username="staffer",
        email="staffer@example.com",
        password="strong-password-123",
        is_staff=True,
    )
    staff_user.user_permissions.add(Permission.objects.get(codename="view_order"))
    buyer = django_user_model.objects.create_user(
        username="buyer",
        email="buyer@example.com",
        password="strong-password-123",
    )
    category = Category.objects.create(name="Beer", slug="beer")
    product = Product.objects.create(
        name="Amber Ale",
        slug="amber-ale",
        description="Balanced amber ale.",
        price=Decimal("12.50"),
        category=category,
        stock=10,
    )
    order = Order.objects.create(
        user=buyer,
        status=OrderStatus.DELIVERED,
        total_price=Decimal("25.00"),
        shipping_address="1 Hop Lane, Kyiv",
    )
    OrderItem.objects.create(order=order, product=product, quantity=2, price=product.price)
    client.force_login(staff_user)

    response = client.get(reverse("admin:orders_order_changelist"))

    assert response.status_code == 200
    assert b"Analytics summary" in response.content
    assert b"Order count" in response.content
    assert b"25.00" in response.content


def test_staff_user_can_see_product_admin_analytics(client, django_user_model) -> None:
    staff_user = django_user_model.objects.create_user(
        username="catalog_staff",
        email="catalog_staff@example.com",
        password="strong-password-123",
        is_staff=True,
    )
    staff_user.user_permissions.add(Permission.objects.get(codename="view_product"))
    buyer = django_user_model.objects.create_user(
        username="analytics-buyer",
        email="analytics-buyer@example.com",
        password="strong-password-123",
    )
    category = Category.objects.create(name="Malt", slug="malt")
    product = Product.objects.create(
        name="Golden Promise",
        slug="golden-promise",
        description="Soft biscuit sweetness.",
        price=Decimal("9.90"),
        category=category,
        stock=14,
    )
    order = Order.objects.create(
        user=buyer,
        status=OrderStatus.PAID,
        total_price=Decimal("19.80"),
        shipping_address="2 Grain Road, Kyiv",
    )
    OrderItem.objects.create(order=order, product=product, quantity=2, price=product.price)
    client.force_login(staff_user)

    response = client.get(reverse("admin:products_product_changelist"))

    assert response.status_code == 200
    assert b"Analytics summary" in response.content
    assert b"Active products" in response.content
    assert b"Golden Promise" in response.content
