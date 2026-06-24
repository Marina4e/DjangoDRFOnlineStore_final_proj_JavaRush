from django.contrib import admin
from django.contrib.admin import ModelAdmin
from decimal import Decimal

from django.db.models import Count, DecimalField, F, IntegerField, OuterRef, QuerySet, Subquery, Sum, Value
from django.db.models.functions import Coalesce

from orders.models import OrderItem

from .models import Category, Product, Review


class StaffScopedAdminMixin(ModelAdmin):
    """Apply simple role-aware restrictions to admin models."""

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


@admin.register(Category)
class CategoryAdmin(StaffScopedAdminMixin, admin.ModelAdmin):
    list_display = ("name", "slug", "parent", "created_at", "updated_at")
    search_fields = ("name", "slug")
    list_filter = ("created_at", "updated_at")
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(StaffScopedAdminMixin, admin.ModelAdmin):
    change_list_template = "admin/products/product/change_list.html"
    list_display = (
        "name",
        "category",
        "price",
        "stock",
        "sold_quantity",
        "earned_revenue",
        "review_total",
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "slug", "description", "category__name")
    list_filter = ("is_active", "category", "created_at", "updated_at")
    ordering = ("name",)
    list_select_related = ("category",)
    prepopulated_fields = {"slug": ("name",)}

    def get_queryset(self, request) -> QuerySet[Product]:
        sold_quantity_subquery = (
            OrderItem.objects.filter(product=OuterRef("pk"))
            .values("product")
            .annotate(total=Coalesce(Sum("quantity"), 0))
            .values("total")[:1]
        )
        revenue_subquery = (
            OrderItem.objects.filter(product=OuterRef("pk"))
            .values("product")
            .annotate(
                total=Coalesce(
                    Sum(
                        F("quantity") * F("price"),
                        output_field=DecimalField(max_digits=12, decimal_places=2),
                    ),
                    Value(Decimal("0.00")),
                )
            )
            .values("total")[:1]
        )
        return (
            super()
            .get_queryset(request)
            .select_related("category")
            .annotate(
                sold_quantity_total=Coalesce(
                    Subquery(sold_quantity_subquery, output_field=IntegerField()),
                    0,
                ),
                earned_revenue_total=Coalesce(
                    Subquery(
                        revenue_subquery,
                        output_field=DecimalField(max_digits=12, decimal_places=2),
                    ),
                    Value(Decimal("0.00")),
                ),
                review_total_count=Coalesce(Count("reviews", distinct=True), 0),
            )
        )

    @admin.display(ordering="sold_quantity_total", description="Sold units")
    def sold_quantity(self, obj: Product) -> int:
        return int(getattr(obj, "sold_quantity_total", 0))

    @admin.display(ordering="earned_revenue_total", description="Revenue")
    def earned_revenue(self, obj: Product):
        return getattr(obj, "earned_revenue_total", 0)

    @admin.display(ordering="review_total_count", description="Reviews")
    def review_total(self, obj: Product) -> int:
        return int(getattr(obj, "review_total_count", 0))

    def changelist_view(self, request, extra_context=None):
        queryset = self.get_queryset(request)
        extra_context = extra_context or {}
        top_product = queryset.order_by("-sold_quantity_total", "name").first()
        extra_context["summary_cards"] = [
            {"label": "Active products", "value": queryset.filter(is_active=True).count()},
            {"label": "Units in stock", "value": queryset.aggregate(total=Coalesce(Sum("stock"), 0))["total"]},
            {
                "label": "Top product",
                "value": top_product.name if top_product and getattr(top_product, "sold_quantity_total", 0) else "No sales yet",
            },
        ]
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Review)
class ReviewAdmin(StaffScopedAdminMixin, admin.ModelAdmin):
    list_display = ("product", "user", "rating", "created_at")
    search_fields = ("product__name", "user__username", "comment")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
    autocomplete_fields = ("product", "user")
