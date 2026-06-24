from __future__ import annotations

import json
from datetime import timezone as dt_timezone
from decimal import Decimal
from typing import Any, Protocol, cast

import pytest
from django.urls import reverse
from django.utils import timezone

from orders.models import Order, OrderStatus
from products.models import Category, Product


pytestmark = pytest.mark.django_db


class GraphQLTestResponse(Protocol):
    """Minimal response interface used by the GraphQL endpoint tests."""

    status_code: int

    def json(self) -> dict[str, Any]: ...


@pytest.fixture
def analytics_data(django_user_model):
    staff_user = django_user_model.objects.create_user(
        username="staffer",
        email="staff@example.com",
        password="strong-password-123",
        is_staff=True,
        is_superuser=True,
    )
    regular_user = django_user_model.objects.create_user(
        username="regular",
        email="regular@example.com",
        password="strong-password-123",
    )
    other_user = django_user_model.objects.create_user(
        username="repeat",
        email="repeat@example.com",
        password="strong-password-123",
    )

    category = Category.objects.create(name="Brewing", slug="brewing")
    first_product = Product.objects.create(
        name="Citra Hop Pellets",
        slug="citra-hop-pellets",
        description="Bright citrus aroma hops.",
        price=Decimal("10.00"),
        category=category,
        stock=24,
    )
    second_product = Product.objects.create(
        name="Pale Ale Malt",
        slug="pale-ale-malt",
        description="Balanced malt backbone.",
        price=Decimal("20.00"),
        category=category,
        stock=18,
    )

    january_first = Order.objects.create(
        user=regular_user,
        status=OrderStatus.PAID,
        total_price=Decimal("40.00"),
        shipping_address="Kyiv",
    )
    january_first.items.create(product=first_product, quantity=2, price=Decimal("10.00"))
    january_first.items.create(product=second_product, quantity=1, price=Decimal("20.00"))
    Order.objects.filter(pk=january_first.pk).update(
        created_at=timezone.datetime(2026, 1, 15, 12, 0, tzinfo=dt_timezone.utc),
        updated_at=timezone.datetime(2026, 1, 15, 12, 0, tzinfo=dt_timezone.utc),
    )

    january_second = Order.objects.create(
        user=other_user,
        status=OrderStatus.DELIVERED,
        total_price=Decimal("30.00"),
        shipping_address="Lviv",
    )
    january_second.items.create(product=first_product, quantity=1, price=Decimal("10.00"))
    january_second.items.create(product=second_product, quantity=1, price=Decimal("20.00"))
    Order.objects.filter(pk=january_second.pk).update(
        created_at=timezone.datetime(2026, 1, 20, 12, 0, tzinfo=dt_timezone.utc),
        updated_at=timezone.datetime(2026, 1, 20, 12, 0, tzinfo=dt_timezone.utc),
    )

    february_order = Order.objects.create(
        user=regular_user,
        status=OrderStatus.SHIPPED,
        total_price=Decimal("20.00"),
        shipping_address="Kyiv",
    )
    february_order.items.create(product=first_product, quantity=2, price=Decimal("10.00"))
    Order.objects.filter(pk=february_order.pk).update(
        created_at=timezone.datetime(2026, 2, 10, 12, 0, tzinfo=dt_timezone.utc),
        updated_at=timezone.datetime(2026, 2, 10, 12, 0, tzinfo=dt_timezone.utc),
    )

    cancelled_order = Order.objects.create(
        user=other_user,
        status=OrderStatus.CANCELLED,
        total_price=Decimal("999.00"),
        shipping_address="Odesa",
    )
    cancelled_order.items.create(product=second_product, quantity=8, price=Decimal("20.00"))

    return {
        "staff_user": staff_user,
        "regular_user": regular_user,
        "other_user": other_user,
        "first_product": first_product,
        "second_product": second_product,
    }


def graphql_post(client, query: str) -> GraphQLTestResponse:
    return cast(
        GraphQLTestResponse,
        client.post(
            reverse("graphql"),
            data=json.dumps({"query": query}),
            content_type="application/json",
        ),
    )


def test_graphql_endpoint_exists_for_staff(client, analytics_data) -> None:
    client.force_login(analytics_data["staff_user"])

    response = client.get(reverse("graphql"), HTTP_ACCEPT="text/html")

    assert response.status_code == 200


def test_graphql_rejects_anonymous_users(client) -> None:
    response = graphql_post(client, "{ totalRevenue }")

    assert response.status_code == 403


def test_graphql_rejects_non_staff_users(client, analytics_data) -> None:
    client.force_login(analytics_data["regular_user"])

    response = graphql_post(client, "{ totalRevenue }")

    assert response.status_code == 403


def test_graphql_staff_can_access_analytics(client, analytics_data) -> None:
    client.force_login(analytics_data["staff_user"])

    response = graphql_post(
        client,
        """
        {
          totalRevenue
          totalQuantitySold
          averageOrderValue
          revenueTrends(granularity: MONTH) {
            period
            revenue
            orderCount
            quantitySold
          }
          popularProducts(limit: 2) {
            name
            soldQuantity
            revenue
            stock
            imageUrl
          }
          productRevenue(limit: 2) {
            name
            revenue
          }
          stockBalances(limit: 2) {
            name
            stock
          }
          activeUsers(limit: 5) {
            username
            orderCount
            totalSpent
          }
          repeatPurchasers(limit: 5) {
            username
            orderCount
          }
          orderCountPerUser(limit: 5) {
            username
            orderCount
          }
        }
        """,
    )

    assert response.status_code == 200
    payload = response.json()["data"]
    assert payload["totalRevenue"] == "90.00"
    assert payload["totalQuantitySold"] == 7
    assert payload["averageOrderValue"] == "30.00"
    assert payload["revenueTrends"] == [
        {
            "period": "2026-01",
            "revenue": "70.00",
            "orderCount": 2,
            "quantitySold": 5,
        },
        {
            "period": "2026-02",
            "revenue": "20.00",
            "orderCount": 1,
            "quantitySold": 2,
        },
    ]
    assert payload["popularProducts"][0]["name"] == "Citra Hop Pellets"
    assert payload["popularProducts"][0]["soldQuantity"] == 5
    assert payload["popularProducts"][0]["revenue"] == "50.00"
    assert payload["productRevenue"][0]["name"] == "Citra Hop Pellets"
    assert payload["productRevenue"][1]["revenue"] == "40.00"
    assert payload["stockBalances"][0]["stock"] == 24
    assert payload["activeUsers"][0]["username"] == "regular"
    assert payload["activeUsers"][0]["orderCount"] == 2
    assert payload["activeUsers"][0]["totalSpent"] == "60.00"
    assert payload["repeatPurchasers"] == [{"username": "regular", "orderCount": 2}]
    assert payload["orderCountPerUser"][0]["username"] == "regular"
