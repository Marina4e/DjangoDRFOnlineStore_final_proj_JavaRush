from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    autocomplete_fields = ("product",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total_price", "created_at", "updated_at")
    search_fields = ("id", "user__username", "user__email", "shipping_address")
    list_filter = ("status", "created_at", "updated_at")
    ordering = ("-created_at",)
    autocomplete_fields = ("user",)
    inlines = [OrderItemInline]
