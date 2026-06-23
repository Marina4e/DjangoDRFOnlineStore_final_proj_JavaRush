from __future__ import annotations

from django import forms


class CartQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=999)
    next = forms.CharField(required=False)


class CheckoutForm(forms.Form):
    PAYMENT_CARD = "card"
    PAYMENT_BANK = "bank"
    PAYMENT_CASH = "cash"

    PAYMENT_METHOD_CHOICES = (
        (PAYMENT_CARD, "Card on delivery"),
        (PAYMENT_BANK, "Bank transfer"),
        (PAYMENT_CASH, "Cash on delivery"),
    )

    full_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=50)
    address_line1 = forms.CharField(max_length=255, label="Street address")
    address_line2 = forms.CharField(
        max_length=255,
        required=False,
        label="Apartment, suite, etc.",
    )
    city = forms.CharField(max_length=120)
    postal_code = forms.CharField(max_length=20)
    country = forms.CharField(max_length=120, initial="Ukraine")
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES,
        widget=forms.RadioSelect,
        initial=PAYMENT_CARD,
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        text_input_classes = (
            "w-full rounded-md border border-amber-200 bg-amber-50 px-3 py-2.5 "
            "text-sm text-stone-900 outline-none transition "
            "focus:border-amber-400 focus:ring-2 focus:ring-amber-200"
        )
        for field_name, field in self.fields.items():
            if field_name == "payment_method":
                continue
            field.widget.attrs.setdefault("class", text_input_classes)
            field.widget.attrs.setdefault("placeholder", field.label)

    def payment_method_label(self) -> str:
        return dict(self.PAYMENT_METHOD_CHOICES)[self.cleaned_data["payment_method"]]

    def build_shipping_address(self) -> str:
        lines = [
            f"Contact: {self.cleaned_data['full_name']}",
            f"Email: {self.cleaned_data['email']}",
            f"Phone: {self.cleaned_data['phone']}",
            self.cleaned_data["address_line1"],
        ]
        address_line2 = self.cleaned_data.get("address_line2", "").strip()
        if address_line2:
            lines.append(address_line2)
        lines.append(
            ", ".join(
                [
                    self.cleaned_data["city"],
                    self.cleaned_data["postal_code"],
                    self.cleaned_data["country"],
                ]
            )
        )
        lines.append(f"Payment method: {self.payment_method_label()}")
        return "\n".join(lines)
