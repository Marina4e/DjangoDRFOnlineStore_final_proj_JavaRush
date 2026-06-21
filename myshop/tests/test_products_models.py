from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from products.models import Category, Product, Review


pytestmark = pytest.mark.django_db


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username="alice",
        email="alice@example.com",
        password="strong-password-123",
    )


@pytest.fixture
def category():
    return Category.objects.create(name="Hops", slug="hops")


@pytest.fixture
def product(category):
    return Product.objects.create(
        name="Citra Hops",
        slug="citra-hops",
        description="Bright citrus hop profile.",
        price=Decimal("12.50"),
        category=category,
        stock=25,
    )


def test_category_string_representation(category) -> None:
    assert str(category) == "Hops"


def test_product_string_representation(product) -> None:
    assert str(product) == "Citra Hops"


def test_review_string_representation(product, user) -> None:
    review = Review.objects.create(
        product=product,
        user=user,
        rating=5,
        comment="Excellent product.",
    )

    assert str(review) == f"Review for {product} by {user}"


@pytest.mark.parametrize("rating", [0, 6])
def test_review_rating_bounds_fail_validation(product, user, rating: int) -> None:
    review = Review(product=product, user=user, rating=rating, comment="Out of bounds.")

    with pytest.raises(ValidationError):
        review.full_clean()


def test_product_negative_stock_fails_validation(category) -> None:
    product = Product(
        name="Bad Stock Product",
        slug="bad-stock-product",
        description="Invalid stock test.",
        price=Decimal("8.00"),
        category=category,
        stock=-1,
    )

    with pytest.raises(ValidationError):
        product.full_clean()


def test_product_price_constraint_is_enforced_in_database(category) -> None:
    with pytest.raises(IntegrityError), transaction.atomic():
        Product.objects.create(
            name="Zero Price Product",
            slug="zero-price-product",
            description="Invalid price test.",
            price=Decimal("0.00"),
            category=category,
            stock=1,
        )
