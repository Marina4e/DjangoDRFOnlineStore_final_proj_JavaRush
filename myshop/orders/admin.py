from decimal import Decimal

from django.contrib import admin
from django.db.models import Avg, Count, QuerySet, Sum
from django.db.models.functions import Coalesce

from .models import Order, OrderItem, OrderStatus


class StaffScopedAdminMixin(admin.ModelAdmin):
    """Restrict admin model visibility and destructive actions to staff roles."""

    def has_module_permission(self, request) -> bool:
        return bool(request.user.is_active and request.user.is_staff)

    def has_view_permission(self, request, obj=None) -> bool:
        return self.has_module_permission(request) and super().has_view_permission(request, obj)

    def has_change_permission(self, request, obj=None) -> bool:
        return self.has_module_permission(request) and super().has_change_permission(request, obj)

    def has_add_permission(self, request) -> bool:
        return self.has_module_permission(request) and super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None) -> bool:
        return bool(request.user.is_superuser and super().has_delete_permission(request, obj))


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    autocomplete_fields = ("product",)


@admin.register(Order)
class OrderAdmin(StaffScopedAdminMixin, admin.ModelAdmin):
    change_list_template = "admin/orders/order/change_list.html"
    list_display = ("id", "user", "status", "total_price", "created_at", "updated_at")
    search_fields = ("id", "user__username", "user__email", "shipping_address")
    list_filter = ("status", "created_at", "updated_at")
    ordering = ("-created_at",)
    autocomplete_fields = ("user",)
    inlines = [OrderItemInline]
    actions = ("mark_paid", "mark_shipped", "mark_delivered", "mark_cancelled")

    def get_queryset(self, request) -> QuerySet[Order]:
        return super().get_queryset(request).select_related("user").prefetch_related("items__product")

    @admin.action(description="Mark selected orders as paid", permissions=["change"])
    def mark_paid(self, request, queryset: QuerySet[Order]) -> None:
        queryset.exclude(status=OrderStatus.CANCELLED).update(status=OrderStatus.PAID)

    @admin.action(description="Mark selected orders as shipped", permissions=["change"])
    def mark_shipped(self, request, queryset: QuerySet[Order]) -> None:
        queryset.exclude(status=OrderStatus.CANCELLED).update(status=OrderStatus.SHIPPED)

    @admin.action(description="Mark selected orders as delivered", permissions=["change"])
    def mark_delivered(self, request, queryset: QuerySet[Order]) -> None:
        queryset.exclude(status=OrderStatus.CANCELLED).update(status=OrderStatus.DELIVERED)

    @admin.action(description="Mark selected orders as cancelled", permissions=["change"])
    def mark_cancelled(self, request, queryset: QuerySet[Order]) -> None:
        queryset.update(status=OrderStatus.CANCELLED)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        analytics = (
            self.get_queryset(request)
            .exclude(status=OrderStatus.CANCELLED)
            .aggregate(
                order_count=Count("id"),
                total_revenue=Coalesce(Sum("total_price"), Decimal("0.00")),
                average_order_value=Coalesce(Avg("total_price"), Decimal("0.00")),
            )
        )
        extra_context["summary_cards"] = [
            {"label": "Order count", "value": analytics["order_count"]},
            {"label": "Revenue", "value": analytics["total_revenue"]},
            {"label": "Average order", "value": analytics["average_order_value"]},
        ]
        return super().changelist_view(request, extra_context=extra_context)
