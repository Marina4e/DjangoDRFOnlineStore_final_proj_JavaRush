"""Admin registrations for account-related models and user summaries."""

from __future__ import annotations

from decimal import Decimal

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count, Q, QuerySet, Sum
from django.db.models.functions import Coalesce

from orders.models import OrderStatus
from users.models import Address


User = get_user_model()


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Manage saved delivery addresses in the Django admin."""

    list_display = ("label", "user", "city", "country", "is_default", "updated_at")
    search_fields = ("label", "user__username", "recipient_name", "city", "country")
    list_filter = ("is_default", "country", "updated_at")
    ordering = ("user__username", "label")
    autocomplete_fields = ("user",)

    def has_delete_permission(self, request, obj=None) -> bool:
        return bool(request.user.is_superuser and super().has_delete_permission(request, obj))


admin.site.unregister(User)


@admin.register(User)
class StoreUserAdmin(UserAdmin):
    """Extend the stock Django user admin with store analytics columns."""

    change_list_template = "admin/auth/user/change_list.html"
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "order_count",
        "total_spent",
    )

    def get_queryset(self, request) -> QuerySet[User]:
        return (
            super()
            .get_queryset(request)
            .annotate(
                order_count_total=Coalesce(
                    Count(
                        "orders",
                        filter=~Q(orders__status=OrderStatus.CANCELLED),
                        distinct=True,
                    ),
                    0,
                ),
                total_spend_amount=Coalesce(
                    Sum(
                        "orders__total_price",
                        filter=~Q(orders__status=OrderStatus.CANCELLED),
                    ),
                    Decimal("0.00"),
                ),
            )
        )

    @admin.display(ordering="order_count_total", description="Orders")
    def order_count(self, obj: User) -> int:
        return int(getattr(obj, "order_count_total", 0))

    @admin.display(ordering="total_spend_amount", description="Spent")
    def total_spent(self, obj: User):
        return getattr(obj, "total_spend_amount", Decimal("0.00"))

    def has_delete_permission(self, request, obj=None) -> bool:
        return bool(request.user.is_superuser and super().has_delete_permission(request, obj))

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        queryset = self.get_queryset(request)
        extra_context["summary_cards"] = [
            {"label": "Registered users", "value": queryset.count()},
            {"label": "Staff users", "value": queryset.filter(is_staff=True).count()},
            {
                "label": "Repeat purchasers",
                "value": queryset.filter(order_count_total__gte=2).count(),
            },
        ]
        return super().changelist_view(request, extra_context=extra_context)
