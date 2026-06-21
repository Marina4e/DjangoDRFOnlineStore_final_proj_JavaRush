from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from orders.models import Order, OrderItem, OrderStatus
from products.models import Category, Product


pytestmark = pytest.mark.django_db


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="bob",
        email="bob@example.com",
        password="strong-password-123",
    )


@pytest.fixture
def product():
    category = Category.objects.create(name="Malt", slug="malt")
    return Product.objects.create(
        name="Pale Malt",
        slug="pale-malt",
        description="Base malt for brewing.",
        price=Decimal("3.50"),
        category=category,
        stock=100,
    )


@pytest.fixture
def order(user):
    return Order.objects.create(
        user=user,
        status=OrderStatus.PENDING,
        total_price=Decimal("19.99"),
        shipping_address="123 Main St",
    )


def test_order_string_representation(order) -> None:
    assert str(order) == f"Order #{order.pk}"


def test_order_item_string_representation(order, product) -> None:
    item = OrderItem.objects.create(
        order=order,
        product=product,
        quantity=2,
        price=Decimal("3.50"),
    )

    assert str(item) == "Pale Malt x 2"


def test_order_rejects_invalid_status_on_validation(user) -> None:
    order = Order(
        user=user,
        status="unknown",
        total_price=Decimal("19.99"),
        shipping_address="123 Main St",
    )

    with pytest.raises(ValidationError):
        order.full_clean()


def test_order_item_zero_quantity_fails_validation(order, product) -> None:
    item = OrderItem(order=order, product=product, quantity=0, price=Decimal("3.50"))

    with pytest.raises(ValidationError):
        item.full_clean()


def test_order_total_price_constraint_is_enforced_in_database(user) -> None:
    with pytest.raises(IntegrityError), transaction.atomic():
        Order.objects.create(
            user=user,
            status=OrderStatus.PENDING,
            total_price=Decimal("-1.00"),
            shipping_address="123 Main St",
        )


def test_order_item_price_constraint_is_enforced_in_database(order, product) -> None:
    with pytest.raises(IntegrityError), transaction.atomic():
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
            price=Decimal("0.00"),
        )
