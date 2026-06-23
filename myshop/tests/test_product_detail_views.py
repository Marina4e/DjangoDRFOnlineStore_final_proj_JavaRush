from __future__ import annotations

from decimal import Decimal

import pytest
from django.urls import reverse

from products.models import Category, Product, Review


pytestmark = pytest.mark.django_db


@pytest.fixture
def detail_product(django_user_model):
    category = Category.objects.create(name="Yeast", slug="yeast")
    product = Product.objects.create(
        name="House Saison Yeast",
        slug="house-saison-yeast",
        description="Dry and peppery fermentation profile for farmhouse ales.",
        price=Decimal("14.50"),
        category=category,
        stock=6,
    )
    first_user = django_user_model.objects.create_user(
        username="brewer_one",
        email="brewer1@example.com",
        password="strong-password-123",
    )
    second_user = django_user_model.objects.create_user(
        username="brewer_two",
        email="brewer2@example.com",
        password="strong-password-123",
    )
    Review.objects.create(
        product=product,
        user=first_user,
        rating=5,
        comment="Fantastic saison character and reliable attenuation.",
    )
    Review.objects.create(
        product=product,
        user=second_user,
        rating=3,
        comment="Solid but a little slower to start than expected.",
    )
    return product


def test_product_detail_page_renders(client, detail_product) -> None:
    response = client.get(
        reverse("product-detail", kwargs={"slug": detail_product.slug})
    )

    assert response.status_code == 200
    assert any(template.name == "products/detail.html" for template in response.templates)
    assert b"House Saison Yeast" in response.content
    assert b"Dry and peppery fermentation profile" in response.content
    assert b"Add to cart" in response.content


def test_product_detail_context_contains_rating_summary(client, detail_product) -> None:
    response = client.get(
        reverse("product-detail", kwargs={"slug": detail_product.slug})
    )

    product = response.context["product"]

    assert product.review_count == 2
    assert product.average_rating == Decimal("4")


def test_product_detail_htmx_reviews_fragment_renders_existing_reviews(
    client,
    detail_product,
) -> None:
    response = client.get(
        reverse("product-detail", kwargs={"slug": detail_product.slug}),
        {"fragment": "reviews"},
        HTTP_HX_REQUEST="true",
    )

    assert response.status_code == 200
    assert any(
        template.name == "products/partials/review_list.html"
        for template in response.templates
    )
    assert b"Fantastic saison character" in response.content
    assert b"Solid but a little slower" in response.content
    assert b"<html" not in response.content


def test_product_detail_handles_products_without_reviews(client) -> None:
    category = Category.objects.create(name="Malt", slug="base-malt")
    product = Product.objects.create(
        name="Golden Promise Malt",
        slug="golden-promise-malt",
        description="Soft biscuit sweetness for pale ales and bitters.",
        price=Decimal("9.90"),
        category=category,
        stock=0,
    )

    response = client.get(
        reverse("product-detail", kwargs={"slug": product.slug})
    )

    assert response.status_code == 200
    assert b"No ratings yet" in response.content
    assert b"This product is currently unavailable" in response.content
