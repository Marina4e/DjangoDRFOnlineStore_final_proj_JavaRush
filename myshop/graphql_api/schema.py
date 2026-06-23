"""GraphQL analytics schema exposing staff-only order, product, and user insights."""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Any, cast

import graphene
from django.contrib.auth import get_user_model
from django.db.models import Count, DecimalField, F, IntegerField, Q, QuerySet, Sum
from django.db.models.functions import Coalesce, TruncDate, TruncMonth
from graphql import GraphQLError

from orders.models import Order, OrderStatus
from products.models import Product


ANALYTICS_ORDER_FILTER = ~Q(status=OrderStatus.CANCELLED)
ANALYTICS_USER_ORDER_FILTER = ~Q(orders__status=OrderStatus.CANCELLED)


class RevenueTrendGranularity(graphene.Enum):
    """Supported grouping options for revenue trend analytics."""

    DAY = "day"
    MONTH = "month"


class RevenueTrendType(graphene.ObjectType):
    """Revenue trend row grouped by day or month."""

    period = graphene.String(required=True)
    revenue = graphene.Decimal(required=True)
    order_count = graphene.Int(required=True)
    quantity_sold = graphene.Int(required=True)


class ProductAnalyticsType(graphene.ObjectType):
    """Per-product analytics row for GraphQL responses."""

    product_id = graphene.ID(required=True)
    name = graphene.String(required=True)
    slug = graphene.String(required=True)
    sold_quantity = graphene.Int(required=True)
    revenue = graphene.Decimal(required=True)
    stock = graphene.Int(required=True)
    image_url = graphene.String(required=True)


class UserAnalyticsType(graphene.ObjectType):
    """Per-user analytics row for GraphQL responses."""

    user_id = graphene.ID(required=True)
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    order_count = graphene.Int(required=True)
    total_spent = graphene.Decimal(required=True)


def require_staff(info: graphene.ResolveInfo) -> None:
    """Reject GraphQL analytics access unless the current user is staff."""
    user = info.context.user
    if not user.is_authenticated or not user.is_staff:
        raise GraphQLError("Staff authentication is required for analytics access.")


def line_revenue_expression() -> F:
    """Return the expression used to aggregate order-item revenue."""
    return F("order_items__quantity") * F("order_items__price")


def annotated_product_analytics(limit: int | None = None) -> QuerySet[Product]:
    """Return products annotated with sold quantity and revenue."""
    queryset = Product.objects.select_related("category").annotate(
        sold_quantity=Coalesce(
            Sum(
                "order_items__quantity",
                filter=Q(order_items__order__status__in=OrderStatus.values)
                & ~Q(order_items__order__status=OrderStatus.CANCELLED),
                output_field=IntegerField(),
            ),
            0,
            output_field=IntegerField(),
        ),
        revenue=Coalesce(
            Sum(
                line_revenue_expression(),
                filter=Q(order_items__order__status__in=OrderStatus.values)
                & ~Q(order_items__order__status=OrderStatus.CANCELLED),
                output_field=DecimalField(max_digits=12, decimal_places=2),
            ),
            Decimal("0.00"),
            output_field=DecimalField(max_digits=12, decimal_places=2),
        ),
    )
    if limit is not None:
        return queryset[:limit]
    return queryset


def annotated_user_analytics() -> QuerySet[Any]:
    """Return users annotated with non-cancelled order counts and spend."""
    user_model = get_user_model()
    return user_model.objects.annotate(
        order_count=Coalesce(
            Count("orders", filter=ANALYTICS_USER_ORDER_FILTER, distinct=True),
            0,
            output_field=IntegerField(),
        ),
        total_spent=Coalesce(
            Sum(
                "orders__total_price",
                filter=ANALYTICS_USER_ORDER_FILTER,
                output_field=DecimalField(max_digits=12, decimal_places=2),
            ),
            Decimal("0.00"),
            output_field=DecimalField(max_digits=12, decimal_places=2),
        ),
    )


def format_period(value: date | datetime, granularity: RevenueTrendGranularity) -> str:
    """Normalize grouped date values into stable response strings."""
    if granularity == RevenueTrendGranularity.MONTH:
        return value.strftime("%Y-%m")
    return value.strftime("%Y-%m-%d")


class Query(graphene.ObjectType):
    """Root analytics queries for the GraphQL bonus phase."""

    total_revenue = graphene.Decimal(required=True)
    total_quantity_sold = graphene.Int(required=True)
    average_order_value = graphene.Decimal(required=True)
    revenue_trends = graphene.List(
        RevenueTrendType,
        granularity=graphene.Argument(
            RevenueTrendGranularity,
            required=False,
            default_value=RevenueTrendGranularity.MONTH,
        ),
    )
    popular_products = graphene.List(
        ProductAnalyticsType,
        limit=graphene.Int(required=False, default_value=5),
    )
    product_revenue = graphene.List(
        ProductAnalyticsType,
        limit=graphene.Int(required=False, default_value=5),
    )
    stock_balances = graphene.List(
        ProductAnalyticsType,
        limit=graphene.Int(required=False, default_value=10),
    )
    active_users = graphene.List(
        UserAnalyticsType,
        limit=graphene.Int(required=False, default_value=10),
    )
    repeat_purchasers = graphene.List(
        UserAnalyticsType,
        limit=graphene.Int(required=False, default_value=10),
    )
    order_count_per_user = graphene.List(
        UserAnalyticsType,
        limit=graphene.Int(required=False, default_value=10),
    )

    def resolve_total_revenue(self, info: graphene.ResolveInfo) -> Decimal:
        """Return total non-cancelled order revenue."""
        require_staff(info)
        return cast(
            Decimal,
            Order.objects.filter(ANALYTICS_ORDER_FILTER).aggregate(
                total=Coalesce(
                    Sum(
                        "total_price",
                        output_field=DecimalField(max_digits=12, decimal_places=2),
                    ),
                    Decimal("0.00"),
                    output_field=DecimalField(max_digits=12, decimal_places=2),
                )
            )["total"],
        )

    def resolve_total_quantity_sold(self, info: graphene.ResolveInfo) -> int:
        """Return total sold quantity across non-cancelled orders."""
        require_staff(info)
        return cast(
            int,
            Order.objects.filter(ANALYTICS_ORDER_FILTER).aggregate(
                total=Coalesce(
                    Sum("items__quantity", output_field=IntegerField()),
                    0,
                    output_field=IntegerField(),
                )
            )["total"],
        )

    def resolve_average_order_value(self, info: graphene.ResolveInfo) -> Decimal:
        """Return average order value across non-cancelled orders."""
        require_staff(info)
        order_values = list(
            Order.objects.filter(ANALYTICS_ORDER_FILTER).values_list("total_price", flat=True)
        )
        if not order_values:
            return Decimal("0.00")
        return sum(order_values, Decimal("0.00")) / Decimal(len(order_values))

    def resolve_revenue_trends(
        self,
        info: graphene.ResolveInfo,
        granularity: RevenueTrendGranularity,
    ) -> list[RevenueTrendType]:
        """Return grouped revenue trends by day or month."""
        require_staff(info)
        truncator = TruncMonth("created_at") if granularity == RevenueTrendGranularity.MONTH else TruncDate("created_at")
        rows = (
            Order.objects.filter(ANALYTICS_ORDER_FILTER)
            .annotate(period=truncator)
            .values("period")
            .annotate(
                revenue=Coalesce(
                    Sum(
                        F("items__quantity") * F("items__price"),
                        output_field=DecimalField(max_digits=12, decimal_places=2),
                    ),
                    Decimal("0.00"),
                    output_field=DecimalField(max_digits=12, decimal_places=2),
                ),
                order_count=Coalesce(
                    Count("id", distinct=True),
                    0,
                    output_field=IntegerField(),
                ),
                quantity_sold=Coalesce(
                    Sum("items__quantity", output_field=IntegerField()),
                    0,
                    output_field=IntegerField(),
                ),
            )
            .order_by("period")
        )
        return [
            RevenueTrendType(
                period=format_period(cast(date | datetime, row["period"]), granularity),
                revenue=cast(Decimal, row["revenue"]),
                order_count=cast(int, row["order_count"]),
                quantity_sold=cast(int, row["quantity_sold"]),
            )
            for row in rows
            if row["period"] is not None
        ]

    def resolve_popular_products(
        self,
        info: graphene.ResolveInfo,
        limit: int,
    ) -> list[ProductAnalyticsType]:
        """Return products ordered by sold quantity."""
        require_staff(info)
        queryset = annotated_product_analytics(limit=None).order_by("-sold_quantity", "-revenue", "name")[:limit]
        return [
            ProductAnalyticsType(
                product_id=product.pk,
                name=product.name,
                slug=product.slug,
                sold_quantity=cast(int, product.sold_quantity),
                revenue=cast(Decimal, product.revenue),
                stock=product.stock,
                image_url=info.context.build_absolute_uri(product.display_image_url),
            )
            for product in queryset
        ]

    def resolve_product_revenue(
        self,
        info: graphene.ResolveInfo,
        limit: int,
    ) -> list[ProductAnalyticsType]:
        """Return products ordered by generated revenue."""
        require_staff(info)
        queryset = annotated_product_analytics(limit=None).order_by("-revenue", "-sold_quantity", "name")[:limit]
        return [
            ProductAnalyticsType(
                product_id=product.pk,
                name=product.name,
                slug=product.slug,
                sold_quantity=cast(int, product.sold_quantity),
                revenue=cast(Decimal, product.revenue),
                stock=product.stock,
                image_url=info.context.build_absolute_uri(product.display_image_url),
            )
            for product in queryset
        ]

    def resolve_stock_balances(
        self,
        info: graphene.ResolveInfo,
        limit: int,
    ) -> list[ProductAnalyticsType]:
        """Return current stock balances with analytics metadata."""
        require_staff(info)
        queryset = annotated_product_analytics(limit=None).order_by("-stock", "name")[:limit]
        return [
            ProductAnalyticsType(
                product_id=product.pk,
                name=product.name,
                slug=product.slug,
                sold_quantity=cast(int, product.sold_quantity),
                revenue=cast(Decimal, product.revenue),
                stock=product.stock,
                image_url=info.context.build_absolute_uri(product.display_image_url),
            )
            for product in queryset
        ]

    def resolve_active_users(
        self,
        info: graphene.ResolveInfo,
        limit: int,
    ) -> list[UserAnalyticsType]:
        """Return users with at least one non-cancelled order."""
        require_staff(info)
        queryset = annotated_user_analytics().filter(order_count__gte=1).order_by("-order_count", "username")[:limit]
        return [
            UserAnalyticsType(
                user_id=user.pk,
                username=user.username,
                email=user.email,
                order_count=cast(int, user.order_count),
                total_spent=cast(Decimal, user.total_spent),
            )
            for user in queryset
        ]

    def resolve_repeat_purchasers(
        self,
        info: graphene.ResolveInfo,
        limit: int,
    ) -> list[UserAnalyticsType]:
        """Return users with at least two non-cancelled orders."""
        require_staff(info)
        queryset = annotated_user_analytics().filter(order_count__gte=2).order_by("-order_count", "username")[:limit]
        return [
            UserAnalyticsType(
                user_id=user.pk,
                username=user.username,
                email=user.email,
                order_count=cast(int, user.order_count),
                total_spent=cast(Decimal, user.total_spent),
            )
            for user in queryset
        ]

    def resolve_order_count_per_user(
        self,
        info: graphene.ResolveInfo,
        limit: int,
    ) -> list[UserAnalyticsType]:
        """Return users ordered by their non-cancelled order count."""
        require_staff(info)
        queryset = annotated_user_analytics().order_by("-order_count", "username")[:limit]
        return [
            UserAnalyticsType(
                user_id=user.pk,
                username=user.username,
                email=user.email,
                order_count=cast(int, user.order_count),
                total_spent=cast(Decimal, user.total_spent),
            )
            for user in queryset
        ]


schema = graphene.Schema(query=Query)
