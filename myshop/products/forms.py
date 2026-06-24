"""Forms used by the browser-rendered product pages."""

from __future__ import annotations

from django import forms

from products.models import Review


RATING_CHOICES = (
    (1, "1 - Poor"),
    (2, "2 - Fair"),
    (3, "3 - Good"),
    (4, "4 - Very good"),
    (5, "5 - Excellent"),
)


class ReviewForm(forms.ModelForm):
    """Collect a browser review rating and comment for a product."""

    rating = forms.TypedChoiceField(
        choices=RATING_CHOICES,
        coerce=int,
        empty_value=None,
        widget=forms.Select(
            attrs={
                "class": (
                    "rounded-md border border-amber-200 bg-amber-50 px-3 py-2 text-sm "
                    "text-stone-900 outline-none transition focus:border-amber-400 "
                    "focus:ring-2 focus:ring-amber-200"
                )
            }
        ),
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "placeholder": "Share what you liked, what stood out, or how it brewed.",
                "class": (
                    "w-full rounded-md border border-amber-200 bg-amber-50 px-3 py-2 text-sm "
                    "text-stone-900 outline-none transition focus:border-amber-400 "
                    "focus:ring-2 focus:ring-amber-200"
                ),
            }
        )
    )

    class Meta:
        model = Review
        fields = ("rating", "comment")
