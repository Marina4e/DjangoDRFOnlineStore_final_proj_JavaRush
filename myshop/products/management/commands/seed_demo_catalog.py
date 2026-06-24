"""Seed a richer demo catalog for local browser checks."""

from __future__ import annotations

from decimal import Decimal
from typing import Any

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from products.models import Category, Product, Review


DEMO_CATALOG: list[dict[str, Any]] = [
    {
        "category": {"name": "Hops", "slug": "hops"},
        "product": {
            "name": "Citra Hop Pellets",
            "slug": "citra-hop-pellets",
            "description": "Punchy citrus and tropical hop pellets for bright pale ales and IPAs.",
            "price": Decimal("12.50"),
            "stock": 28,
        },
    },
    {
        "category": {"name": "Hops", "slug": "hops"},
        "product": {
            "name": "Mosaic Cryo Hops",
            "slug": "mosaic-cryo-hops",
            "description": "Intense berry, mango, and dank aromatics with a clean bitter edge.",
            "price": Decimal("15.90"),
            "stock": 18,
        },
    },
    {
        "category": {"name": "Malt", "slug": "malt"},
        "product": {
            "name": "Golden Promise Malt",
            "slug": "golden-promise-malt",
            "description": (
                "Soft biscuit sweetness and gentle body for bitters, blondes, "
                "and pale ales."
            ),
            "price": Decimal("9.40"),
            "stock": 36,
        },
    },
    {
        "category": {"name": "Malt", "slug": "malt"},
        "product": {
            "name": "Chocolate Rye Malt",
            "slug": "chocolate-rye-malt",
            "description": "Roasty cocoa depth with a spicy rye edge for porters and dark lagers.",
            "price": Decimal("11.80"),
            "stock": 14,
        },
    },
    {
        "category": {"name": "Yeast", "slug": "yeast"},
        "product": {
            "name": "House Saison Yeast",
            "slug": "house-saison-yeast",
            "description": "Dry, peppery farmhouse fermentation character with lively attenuation.",
            "price": Decimal("14.50"),
            "stock": 16,
        },
    },
    {
        "category": {"name": "Yeast", "slug": "yeast"},
        "product": {
            "name": "London Ale Yeast",
            "slug": "london-ale-yeast",
            "description": "Rounded ester profile and dependable flocculation for English styles.",
            "price": Decimal("13.20"),
            "stock": 20,
        },
    },
    {
        "category": {"name": "Dark Beer", "slug": "dark-beer"},
        "product": {
            "name": "Stout Night",
            "slug": "stout-night",
            "description": (
                "A roasty imperial stout ingredient kit with coffee, cocoa, "
                "and dark fruit notes."
            ),
            "price": Decimal("39.90"),
            "stock": 9,
        },
    },
    {
        "category": {"name": "Fruit Brewing", "slug": "fruit-brewing"},
        "product": {
            "name": "Wild Cherry Cider Blend",
            "slug": "wild-cherry-cider-blend",
            "description": "Bright orchard fruit blend for expressive small-batch cider projects.",
            "price": Decimal("17.60"),
            "stock": 11,
        },
    },
]

DEMO_REVIEWS = (
    {
        "slug": "stout-night",
        "rating": 5,
        "comment": "Rich roast character and a great dessert-beer finish.",
    },
    {
        "slug": "citra-hop-pellets",
        "rating": 4,
        "comment": "Fresh aroma, excellent in dry-hop additions.",
    },
    {
        "slug": "golden-promise-malt",
        "rating": 5,
        "comment": "Beautiful base malt with a clean biscuit note.",
    },
)


class Command(BaseCommand):
    """Create or refresh a realistic demo catalog without touching orders or users."""

    help = "Seed demo categories, products, and a few example reviews."

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete all categories, products, and reviews before reseeding.",
        )

    def handle(self, *args: object, **options: object) -> None:
        if bool(options["reset"]):
            Review.objects.all().delete()
            Product.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(
                    "Existing catalog, categories, and reviews removed."
                )
            )

        for entry in DEMO_CATALOG:
            category_data = entry["category"]
            product_data = entry["product"]
            category, _ = Category.objects.get_or_create(
                slug=category_data["slug"],
                defaults={"name": category_data["name"]},
            )
            if category.name != category_data["name"]:
                category.name = category_data["name"]
                category.save(update_fields=["name"])

            product, created = Product.objects.update_or_create(
                slug=product_data["slug"],
                defaults={
                    **product_data,
                    "category": category,
                    "is_active": True,
                    "image": "",
                },
            )
            action = "Created" if created else "Updated"
            self.stdout.write(f"{action} product: {product.name}")

        reviewer = self._ensure_demo_reviewer()
        for review_data in DEMO_REVIEWS:
            product = Product.objects.get(slug=review_data["slug"])
            Review.objects.update_or_create(
                product=product,
                user=reviewer,
                defaults={
                    "rating": review_data["rating"],
                    "comment": review_data["comment"],
                },
            )
        self.stdout.write(self.style.SUCCESS("Demo catalog is ready."))

    def _ensure_demo_reviewer(self) -> Any:
        user_model = get_user_model()
        reviewer, _ = user_model.objects.get_or_create(
            username="demo-reviewer",
            defaults={
                "email": "demo-reviewer@example.com",
            },
        )
        if not reviewer.has_usable_password():
            reviewer.set_password("DemoPass123!")
            reviewer.save(update_fields=["password"])
        return reviewer
