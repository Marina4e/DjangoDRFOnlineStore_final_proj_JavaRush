from __future__ import annotations

from decimal import Decimal, InvalidOperation
from typing import Any, cast

from django.db.models import IntegerField, OuterRef, Subquery, Sum, Value
from django.db.models.functions import Coalesce
from django.views.generic import ListView, TemplateView

from orders.models import OrderItem
from products.models import Category, Product


def parse_decimal(raw_value: str | None) -> Decimal | None:
    if not raw_value:
        return None

    try:
        return Decimal(raw_value)
    except InvalidOperation:
        return None


class HomePageView(TemplateView):
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

    def get_queryset(self):  # type: ignore[override]
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

        return (
            queryset.search(search_term)
            .in_category(category_slug)
            .within_price_range(min_price, max_price)
            .order_by(ordering, "name")
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
