"""Product, category, and review models for the storefront."""

from __future__ import annotations

from decimal import Decimal
from typing import cast

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q, QuerySet
from django.templatetags.static import static


class Category(models.Model):
    """A catalog category that may optionally have a parent category."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return str(self.name)


class ProductQuerySet(QuerySet["Product"]):
    def active(self) -> "ProductQuerySet":
        """Return only active products."""
        return cast(ProductQuerySet, self.filter(is_active=True))

    def search(self, term: str) -> "ProductQuerySet":
        """Filter products by a case-insensitive name or description search."""
        if not term:
            return self
        return cast(
            ProductQuerySet,
            self.filter(Q(name__icontains=term) | Q(description__icontains=term)),
        )

    def in_category(self, category_slug: str) -> "ProductQuerySet":
        """Filter products by category slug when one is provided."""
        if not category_slug:
            return self
        return cast(ProductQuerySet, self.filter(category__slug=category_slug))

    def within_price_range(
        self,
        min_price: Decimal | None,
        max_price: Decimal | None,
    ) -> "ProductQuerySet":
        """Filter products by optional minimum and maximum prices."""
        queryset: ProductQuerySet = self
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        return queryset


class Product(models.Model):
    """A purchasable product in the online store catalog."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )
    image = models.ImageField(upload_to="products/", blank=True)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductQuerySet.as_manager()

    class Meta:
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(price__gte=Decimal("0.01")),
                name="product_price_gte_0_01",
            ),
            models.CheckConstraint(
                condition=models.Q(stock__gte=0),
                name="product_stock_gte_0",
            ),
        ]

    def __str__(self) -> str:
        return str(self.name)

    @property
    def placeholder_image_path(self) -> str:
        """Return a local fallback image path when no uploaded product image exists."""
        keyword_source = f"{self.name} {self.category.name}".lower()
        if "hop" in keyword_source:
            return "img/products/hops-placeholder.svg"
        if any(keyword in keyword_source for keyword in ("malt", "grain", "barley")):
            return "img/products/malt-placeholder.svg"
        if any(keyword in keyword_source for keyword in ("yeast", "ferment")):
            return "img/products/yeast-placeholder.svg"
        return "img/products/general-placeholder.svg"

    @property
    def display_image_url(self) -> str:
        """Return the uploaded image URL or a static placeholder URL."""
        if self.image:
            return str(self.image.url)
        return static(self.placeholder_image_path)


class Review(models.Model):
    """A user review left for a purchased product."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                name="review_rating_between_1_and_5",
            ),
        ]

    def __str__(self) -> str:
        return f"Review for {self.product} by {self.user}"
