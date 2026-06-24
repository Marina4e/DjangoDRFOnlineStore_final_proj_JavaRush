"""Smoke tests for the product catalog entry stage."""

from decimal import Decimal

import pytest
from django.urls import reverse

from products.models import Category, Product


pytestmark = pytest.mark.django_db


def test_homepage_renders_catalog_entry_experience(client) -> None:
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert b"Browse catalog" in response.content
    assert b"Fresh additions to the catalog" in response.content


def test_homepage_featured_product_cards_link_to_detail_pages(client) -> None:
    category = Category.objects.create(name="Hops", slug="hops")
    product = Product.objects.create(
        name="Home Linked Product",
        slug="home-linked-product",
        description="Featured product for homepage linking.",
        price=Decimal("12.50"),
        category=category,
        stock=7,
    )

    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert reverse("product-detail", kwargs={"slug": product.slug}).encode() in response.content
