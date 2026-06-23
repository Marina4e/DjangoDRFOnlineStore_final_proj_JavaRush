"""Catalog and product-detail views for the storefront."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import Any, cast

from django.db.models import Avg, Count, IntegerField, OuterRef, Prefetch, Subquery, Sum, Value
from django.db.models.query import QuerySet
from django.db.models.functions import Coalesce
from django.views.generic import DetailView, ListView, TemplateView

from orders.models import OrderItem
from products.models import Category, Product, ProductQuerySet, Review


def parse_decimal(raw_value: str | None) -> Decimal | None:
    """Parse a decimal query parameter and ignore invalid values."""
    if not raw_value:
        return None

    try:
        return Decimal(raw_value)
    except InvalidOperation:
        return None


class HomePageView(TemplateView):
    """Render the storefront landing page with featured catalog data."""

    template_name = "products/home.html"

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = cast(dict[str, Any], super().get_context_data(**kwargs))
        context["featured_products"] = (
            Product.objects.active().select_related("category").order_by("-created_at")[:3]
        )
        context["top_categories"] = (
            Category.objects.filter(products__is_active=True).distinct().order_by("name")[:6]
        )
        return context


class ProductCatalogView(ListView):
    """Render the main catalog with filtering, search, and sorting."""

    model = Product
    template_name = "products/catalog.html"
    context_object_name = "products"
    paginate_by = 8

    sort_options = {
        "newest": "-created_at",
        "price_asc": "price",
        "price_desc": "-price",
        "popularity": "-popularity",
    }

    def get_template_names(self) -> list[str]:
        if self.request.headers.get("HX-Request") == "true":
            return ["products/partials/catalog_results.html"]
        return [self.template_name]

    def get_queryset(self) -> ProductQuerySet:  # type: ignore[override]
        """Build the annotated queryset used by the catalog page."""
        popularity_subquery = (
            OrderItem.objects.filter(product=OuterRef("pk"))
            .values("product")
            .annotate(total=Sum("quantity"))
            .values("total")[:1]
        )

        queryset = (
            Product.objects.active()
            .select_related("category")
            .annotate(
                popularity=Coalesce(
                    Subquery(popularity_subquery, output_field=IntegerField()),
                    Value(0),
                )
            )
        )

        search_term = self.request.GET.get("q", "").strip()
        category_slug = self.request.GET.get("category", "").strip()
        min_price = parse_decimal(self.request.GET.get("min_price"))
        max_price = parse_decimal(self.request.GET.get("max_price"))
        sort_key = self.request.GET.get("sort", "newest")
        ordering = self.sort_options.get(sort_key, self.sort_options["newest"])

        return cast(
            ProductQuerySet,
            queryset.search(search_term)
            .in_category(category_slug)
            .within_price_range(min_price, max_price)
            .order_by(ordering, "name"),
        )

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = cast(dict[str, Any], super().get_context_data(**kwargs))
        current_query = self.request.GET.copy()
        current_query.pop("page", None)
        page_query = current_query.urlencode()
        page_obj = context["page_obj"]

        context.update(
            {
                "categories": Category.objects.filter(products__is_active=True)
                .distinct()
                .order_by("name"),
                "current_search": self.request.GET.get("q", "").strip(),
                "current_category": self.request.GET.get("category", "").strip(),
                "current_min_price": self.request.GET.get("min_price", "").strip(),
                "current_max_price": self.request.GET.get("max_price", "").strip(),
                "current_sort": self.request.GET.get("sort", "newest"),
                "page_query_prefix": f"{page_query}&" if page_query else "",
                "page_numbers": page_obj.paginator.get_elided_page_range(
                    page_obj.number,
                    on_each_side=1,
                    on_ends=1,
                ),
            }
        )
        return context


class ProductDetailView(DetailView):
    """Render one product detail page and its review fragment."""

    model = Product
    template_name = "products/detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_template_names(self) -> list[str]:
        if (
            self.request.headers.get("HX-Request") == "true"
            and self.request.GET.get("fragment") == "reviews"
        ):
            return ["products/partials/review_list.html"]
        return [self.template_name]

    def get_queryset(self) -> QuerySet[Product]:  # type: ignore[override]
        """Return active products with review and popularity annotations."""
        popularity_subquery = (
            OrderItem.objects.filter(product=OuterRef("pk"))
            .values("product")
            .annotate(total=Sum("quantity"))
            .values("total")[:1]
        )
        review_queryset = Review.objects.select_related("user").order_by("-created_at")

        return (
            Product.objects.active()
            .select_related("category")
            .prefetch_related(Prefetch("reviews", queryset=review_queryset))
            .annotate(
                popularity=Coalesce(
                    Subquery(popularity_subquery, output_field=IntegerField()),
                    Value(0),
                ),
                average_rating=Avg("reviews__rating"),
                review_count=Count("reviews"),
            )
        )

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = cast(dict[str, Any], super().get_context_data(**kwargs))
        product = cast(Product, context["product"])
        context["quantity_options"] = range(1, min(product.stock, 10) + 1)
        context["stock_state"] = "In stock" if product.stock > 0 else "Out of stock"
        context["stock_state_tone"] = (
            "bg-emerald-100 text-emerald-800"
            if product.stock > 0
            else "bg-rose-100 text-rose-800"
        )
        return context
