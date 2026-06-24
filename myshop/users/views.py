"""Session-auth account, profile, and address views."""

from __future__ import annotations

from typing import Any
from typing import cast

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeDoneView, PasswordChangeView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models.query import QuerySet
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, FormView, TemplateView, UpdateView

from orders.models import Order, OrderStatus
from users.forms import (
    AddressForm,
    ProfileForm,
    RegistrationForm,
    StoreAuthenticationForm,
    StyledPasswordChangeForm,
)
from users.models import Address


def user_orders_queryset(request: HttpRequest) -> QuerySet[Order]:
    """Return the current user's orders with items and products prefetched."""
    return (
        Order.objects.filter(user=request.user)
        .prefetch_related("items__product")
        .order_by("-created_at")
    )


def build_account_context(
    request: HttpRequest,
    *,
    profile_form: ProfileForm | None = None,
    address_form: AddressForm | None = None,
) -> dict[str, Any]:
    """Build the shared account-page context for profile, addresses, and orders."""
    selected_status = request.GET.get("status", "").strip()
    valid_statuses = set(OrderStatus.values)
    orders_queryset = user_orders_queryset(request)
    if selected_status in valid_statuses:
        orders_queryset = orders_queryset.filter(status=selected_status)

    return {
        "profile_form": profile_form or ProfileForm(instance=request.user),
        "address_form": address_form or AddressForm(),
        "addresses": request.user.addresses.all(),
        "orders": orders_queryset,
        "selected_status": selected_status,
        "status_choices": OrderStatus.choices,
    }


class RegisterView(FormView):
    """Handle browser registration with immediate session login."""

    template_name = "users/register.html"
    form_class = RegistrationForm

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("account-detail")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: RegistrationForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Your account has been created.")
        return redirect("account-detail")


class StoreLoginView(LoginView):
    """Handle browser login with the project-specific success message."""

    template_name = "users/login.html"
    authentication_form = StoreAuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form: StoreAuthenticationForm) -> HttpResponse:
        messages.success(self.request, "Welcome back.")
        return super().form_valid(form)

    def get_success_url(self) -> str:
        redirect_url = self.get_redirect_url()
        return cast(str, redirect_url or reverse("account-detail"))


@require_POST
def logout_view(request: HttpRequest) -> HttpResponse:
    """End the current session-auth login."""
    logout(request)
    messages.success(request, "You have been signed out.")
    return redirect("home")


class AccountView(LoginRequiredMixin, TemplateView):
    """Render the authenticated user's account dashboard."""

    template_name = "users/account.html"

    def get_context_data(self, **kwargs: object) -> dict[str, Any]:
        context = cast(dict[str, Any], super().get_context_data(**kwargs))
        context.update(build_account_context(self.request))
        return context


class AccountOrdersView(LoginRequiredMixin, TemplateView):
    """Render a dedicated page with the authenticated user's order history."""

    template_name = "users/order_list.html"

    def get_context_data(self, **kwargs: object) -> dict[str, Any]:
        context = cast(dict[str, Any], super().get_context_data(**kwargs))
        selected_status = self.request.GET.get("status", "").strip()
        valid_statuses = set(OrderStatus.values)
        orders = user_orders_queryset(self.request)
        if selected_status in valid_statuses:
            orders = orders.filter(status=selected_status)
        context.update(
            {
                "orders": orders,
                "selected_status": selected_status,
                "status_choices": OrderStatus.choices,
            }
        )
        return context


class AccountOrderDetailView(LoginRequiredMixin, DetailView):
    """Render one ownership-scoped order detail page for the current user."""

    model = Order
    template_name = "users/order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "pk"

    def get_queryset(self) -> QuerySet[Order]:
        """Limit order detail access to the authenticated user's own orders."""
        return user_orders_queryset(self.request)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Handle profile updates for the currently authenticated user."""

    form_class = ProfileForm
    http_method_names = ["post"]

    def get_object(self, queryset: QuerySet[Any] | None = None) -> Any:
        """Return the current authenticated user for profile editing."""
        return self.request.user

    def form_valid(self, form: ProfileForm) -> HttpResponse:
        form.save()
        messages.success(self.request, "Your profile has been updated.")
        return redirect("account-detail")

    def form_invalid(self, form: ProfileForm) -> HttpResponse:
        messages.error(self.request, "Please correct the profile form errors below.")
        context = build_account_context(self.request, profile_form=form)
        return render(self.request, "users/account.html", context, status=400)


class AddressCreateView(LoginRequiredMixin, FormView):
    """Create a saved address for the current user."""

    form_class = AddressForm
    http_method_names = ["post"]

    def form_valid(self, form: AddressForm) -> HttpResponse:
        address = form.save(commit=False)
        address.user = self.request.user
        address.save()
        messages.success(self.request, "Address saved to your account.")
        return redirect("account-detail")

    def form_invalid(self, form: AddressForm) -> HttpResponse:
        messages.error(self.request, "Please correct the address form errors below.")
        context = build_account_context(self.request, address_form=form)
        return render(self.request, "users/account.html", context, status=400)


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    """Edit an existing saved address owned by the current user."""

    model = Address
    form_class = AddressForm
    template_name = "users/address_form.html"

    def get_queryset(self) -> QuerySet[Address]:
        """Limit address editing to the current user's saved addresses."""
        return Address.objects.filter(user=self.request.user)

    def form_valid(self, form: AddressForm) -> HttpResponse:
        form.save()
        messages.success(self.request, "Address updated.")
        return redirect("account-detail")


@login_required
@require_POST
def address_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """Delete one saved address owned by the current user."""
    address = get_object_or_404(Address, pk=pk, user=request.user)
    address.delete()
    messages.success(request, "Address removed.")
    return redirect("account-detail")


class StorePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """Handle password changes for the currently authenticated user."""

    template_name = "users/password_change.html"
    form_class = StyledPasswordChangeForm
    success_url = reverse_lazy("password-change-done")

    def form_valid(self, form: StyledPasswordChangeForm) -> HttpResponse:
        messages.success(self.request, "Your password has been changed.")
        return super().form_valid(form)


class StorePasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    """Show the success page after a password change."""

    template_name = "users/password_change_done.html"
