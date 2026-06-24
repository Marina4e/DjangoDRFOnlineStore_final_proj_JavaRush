from __future__ import annotations

from decimal import Decimal

import pytest
from django.urls import reverse
from django.utils import timezone

from orders.models import Order, OrderItem
from products.models import Category, Product


pytestmark = pytest.mark.django_db


@pytest.fixture
def catalog_data(django_user_model):
    user = django_user_model.objects.create_user(
        username="shopper",
        email="shopper@example.com",
        password="strong-password-123",
    )
    hops = Category.objects.create(name="Hops", slug="hops")
    malt = Category.objects.create(name="Malt", slug="malt")

    products = [
        Product.objects.create(
            name=f"Catalog Product {index:02d}",
            slug=f"catalog-product-{index:02d}",
            description=f"Batch item {index:02d} with tasting notes.",
            price=Decimal("5.00") + Decimal(index),
            category=hops if index % 2 == 0 else malt,
            stock=10 + index,
        )
        for index in range(1, 11)
    ]

    Product.objects.filter(pk=products[0].pk).update(
        name="Citra Burst",
        description="Citrus-heavy hop pellets for bright aroma.",
        created_at=timezone.now() - timezone.timedelta(days=10),
    )
    Product.objects.filter(pk=products[1].pk).update(
        name="Roasted Malt",
        description="Deep caramel malt for darker ales.",
        created_at=timezone.now() - timezone.timedelta(days=8),
    )
    Product.objects.filter(pk=products[2].pk).update(
        name="Fresh Galaxy",
        description="Passionfruit and peach aroma hop addition.",
        created_at=timezone.now() - timezone.timedelta(days=1),
    )

    first_order = Order.objects.create(
        user=user,
        total_price=Decimal("20.00"),
        shipping_address="123 Hop Lane",
    )
    second_order = Order.objects.create(
        user=user,
        total_price=Decimal("30.00"),
        shipping_address="123 Hop Lane",
    )
    OrderItem.objects.create(
        order=first_order,
        product=products[0],
        quantity=2,
        price=products[0].price,
    )
    OrderItem.objects.create(
        order=second_order,
        product=products[0],
        quantity=5,
        price=products[0].price,
    )
    OrderItem.objects.create(
        order=first_order,
        product=products[1],
        quantity=1,
        price=products[1].price,
    )

    for product in products[3:]:
        Product.objects.filter(pk=product.pk).update(
            created_at=timezone.now() - timezone.timedelta(days=product.pk)
        )

    refreshed_products = list(Product.objects.order_by("id"))
    return {
        "products": refreshed_products,
        "hops": hops,
        "malt": malt,
    }


def test_catalog_page_renders(client, catalog_data) -> None:
    response = client.get(reverse("product-list"))

    assert response.status_code == 200
    assert any(template.name == "products/catalog.html" for template in response.templates)
    assert b"Ingredients and essentials" in response.content


def test_catalog_cards_link_to_product_detail(client, catalog_data) -> None:
    product = catalog_data["products"][0]

    response = client.get(reverse("product-list"))

    assert response.status_code == 200
    assert reverse("product-detail", kwargs={"slug": product.slug}).encode() in response.content


def test_catalog_cards_render_product_images_or_placeholders(client, catalog_data) -> None:
    product = catalog_data["products"][0]

    response = client.get(reverse("product-list"))

    assert response.status_code == 200
    assert product.display_image_url.encode() in response.content


def test_catalog_filters_by_category(client, catalog_data) -> None:
    response = client.get(reverse("product-list"), {"category": catalog_data["hops"].slug})

    products = list(response.context["products"])

    assert products
    assert all(product.category_id == catalog_data["hops"].id for product in products)


def test_catalog_filters_by_price_range(client, catalog_data) -> None:
    response = client.get(
        reverse("product-list"),
        {"min_price": "10.00", "max_price": "12.00"},
    )

    prices = [product.price for product in response.context["products"]]

    assert len(prices) == 3
    assert all(Decimal("10.00") <= price <= Decimal("12.00") for price in prices)


def test_catalog_searches_name_and_description(client, catalog_data) -> None:
    response = client.get(reverse("product-list"), {"q": "citrus"})

    products = list(response.context["products"])

    assert [product.name for product in products] == ["Citra Burst"]


def test_catalog_sorts_by_price(client, catalog_data) -> None:
    response = client.get(reverse("product-list"), {"sort": "price_desc"})

    products = list(response.context["products"])

    assert products[0].price > products[-1].price


def test_catalog_sorts_by_popularity(client, catalog_data) -> None:
    response = client.get(reverse("product-list"), {"sort": "popularity"})

    products = list(response.context["products"])

    assert products[0].name == "Citra Burst"
    assert products[0].popularity == 7


def test_catalog_sorts_by_novelty(client, catalog_data) -> None:
    response = client.get(reverse("product-list"), {"sort": "newest"})

    products = list(response.context["products"])

    assert products[0].name == "Fresh Galaxy"


def test_catalog_paginates_results(client, catalog_data) -> None:
    response = client.get(reverse("product-list"), {"page": 2})

    page_obj = response.context["page_obj"]

    assert page_obj.number == 2
    assert len(response.context["products"]) == 2


def test_catalog_htmx_returns_partial(client, catalog_data) -> None:
    response = client.get(
        reverse("product-list"),
        {"q": "fresh"},
        HTTP_HX_REQUEST="true",
    )

    assert response.status_code == 200
    assert any(
        template.name == "products/partials/catalog_results.html"
        for template in response.templates
    )
    assert b"Fresh Galaxy" in response.content
    assert b"<html" not in response.content
