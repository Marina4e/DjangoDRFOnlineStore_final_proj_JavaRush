from __future__ import annotations

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm

from users.models import Address


def _input_class() -> str:
    return (
        "w-full rounded-md border border-amber-200 bg-amber-50 px-3 py-2.5 "
        "text-sm text-stone-900 outline-none transition "
        "focus:border-amber-400 focus:ring-2 focus:ring-amber-200"
    )


def apply_form_styling(form: forms.BaseForm) -> None:
    base_class = _input_class()
    for field in form.fields.values():
        widget = field.widget
        if isinstance(widget, forms.RadioSelect):
            continue
        widget.attrs.setdefault("class", base_class)
        if not isinstance(widget, forms.CheckboxInput):
            widget.attrs.setdefault("placeholder", field.label)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        apply_form_styling(self)


class StoreAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        apply_form_styling(self)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        apply_form_styling(self)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "label",
            "recipient_name",
            "phone",
            "address_line1",
            "address_line2",
            "city",
            "postal_code",
            "country",
            "is_default",
        )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        apply_form_styling(self)


class StyledPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        apply_form_styling(self)
