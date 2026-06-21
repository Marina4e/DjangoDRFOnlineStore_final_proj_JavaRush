from django.contrib import admin

from .models import Category, Product, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "parent", "created_at", "updated_at")
    search_fields = ("name", "slug")
    list_filter = ("created_at", "updated_at")
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "stock",
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "slug", "description", "category__name")
    list_filter = ("is_active", "category", "created_at", "updated_at")
    ordering = ("name",)
    list_select_related = ("category",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "created_at")
    search_fields = ("product__name", "user__username", "comment")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
    autocomplete_fields = ("product", "user")
