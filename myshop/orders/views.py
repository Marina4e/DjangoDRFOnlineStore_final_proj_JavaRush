"""Cart and checkout views for the browser-based storefront flow."""

from __future__ import annotations

from typing import Any
from typing import cast

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST

from orders.cart import (
    CartError,
    add_product,
    get_cart_summary,
    remove_product,
    update_product_quantity,
)
from orders.forms import CartQuantityForm, CheckoutForm
from orders.models import Order
from orders.services import CheckoutError, CheckoutOrderResult, create_order_from_session_cart
from products.models import Product


def _render_cart(
    request: HttpRequest,
    *,
    status: int = 200,
) -> HttpResponse:
    """Render either the full cart page or the HTMX cart fragment."""
    summary = get_cart_summary(request.session)
    summary["is_htmx"] = request.headers.get("HX-Request") == "true"
    template_name = "orders/partials/cart_shell.html"
    if not summary["is_htmx"]:
        template_name = "orders/cart.html"
    return render(request, template_name, summary, status=status)


def _send_checkout_notifications(form: CheckoutForm, result: CheckoutOrderResult) -> None:
    """Send checkout confirmation emails to the customer and site admin."""
    order = result.order
    user_subject = f"Order #{order.pk} received"
    user_body = "\n".join(
        [
            f"Hello {form.cleaned_data['full_name']},",
            "",
            f"We received your order #{order.pk}.",
            f"Payment method: {form.payment_method_label()}",
            f"Items: {result.total_quantity}",
            f"Total: ${order.total_price}",
            "",
            "Shipping details:",
            order.shipping_address,
        ]
    )
    send_mail(
        user_subject,
        user_body,
        settings.DEFAULT_FROM_EMAIL,
        [form.cleaned_data["email"]],
        fail_silently=False,
    )

    admin_emails = [email for _, email in settings.ADMINS if email]
    if admin_emails:
        admin_body = "\n".join(
            [
                f"Order #{order.pk} was placed.",
                f"Customer: {form.cleaned_data['full_name']}",
                f"Customer email: {form.cleaned_data['email']}",
                f"Payment method: {form.payment_method_label()}",
                f"Items: {result.total_quantity}",
                f"Total: ${order.total_price}",
                "",
                "Shipping details:",
                order.shipping_address,
            ]
        )
        send_mail(
            f"New order #{order.pk}",
            admin_body,
            settings.DEFAULT_FROM_EMAIL,
            admin_emails,
            fail_silently=False,
        )


def _build_checkout_context(
    request: HttpRequest,
    *,
    form: CheckoutForm | None = None,
) -> dict[str, Any]:
    """Build the checkout page context with cart state and recent-order feedback."""
    summary = get_cart_summary(request.session, persist_changes=False)
    recent_order_id = request.session.pop("recent_order_id", None)
    recent_order = None
    if recent_order_id and request.user.is_authenticated:
        recent_order = (
            Order.objects.filter(pk=recent_order_id, user=request.user)
            .prefetch_related("items__product")
            .first()
        )

    context: dict[str, Any] = {
        "form": form or CheckoutForm(),
        "cart_summary": summary,
        "requires_login": not request.user.is_authenticated,
        "recent_order": recent_order,
    }
    return context


@require_GET
def cart_detail(request: HttpRequest) -> HttpResponse:
    """Display the current session-backed cart."""
    return _render_cart(request)


@require_POST
def cart_add(request: HttpRequest, product_id: int) -> HttpResponse:
    """Add a product to the cart and redirect back to the originating page."""
    product = get_object_or_404(Product.objects.active(), pk=product_id)
    form = CartQuantityForm(request.POST)
    redirect_to = request.POST.get("next") or reverse("cart-detail")

    if not form.is_valid():
        messages.error(request, "Enter a valid quantity before adding to the cart.")
        return redirect(redirect_to)

    try:
        quantity = cast(int, form.cleaned_data["quantity"])
        new_quantity = add_product(request.session, product, quantity)
    except CartError as exc:
        messages.error(request, str(exc))
    else:
        messages.success(request, f"{product.name} added to cart. Quantity now {new_quantity}.")

    return redirect(redirect_to)


@require_POST
def cart_update(request: HttpRequest, product_id: int) -> HttpResponse:
    """Update one cart line and return the refreshed cart shell."""
    product = get_object_or_404(Product.objects.active(), pk=product_id)
    form = CartQuantityForm(request.POST)

    if not form.is_valid():
        messages.error(request, "Enter a valid quantity to update the cart.")
        return _render_cart(request, status=400)

    try:
        quantity = cast(int, form.cleaned_data["quantity"])
        update_product_quantity(request.session, product, quantity)
    except CartError as exc:
        messages.error(request, str(exc))
        return _render_cart(request, status=400)

    messages.success(request, f"Updated {product.name} quantity to {quantity}.")
    return _render_cart(request)


@require_POST
def cart_remove(request: HttpRequest, product_id: int) -> HttpResponse:
    """Remove one product from the cart and return the refreshed cart shell."""
    product = get_object_or_404(Product.objects.active(), pk=product_id)
    remove_product(request.session, product_id)
    messages.success(request, f"Removed {product.name} from the cart.")
    return _render_cart(request)


@require_GET
def checkout_detail(request: HttpRequest) -> HttpResponse:
    """Render the checkout page and current order summary."""
    if not request.user.is_authenticated:
        messages.error(request, "Sign in before placing an order.")
        return redirect(f"{reverse('login')}?next={reverse('checkout-detail')}")
    return render(request, "orders/checkout.html", _build_checkout_context(request))


@require_POST
def checkout_submit(request: HttpRequest) -> HttpResponse:
    """Validate checkout input and create an order from the session cart."""
    form = CheckoutForm(request.POST)
    if not request.user.is_authenticated:
        messages.error(request, "Sign in before placing an order.")
        return redirect(f"{reverse('login')}?next={reverse('checkout-detail')}")

    if not form.is_valid():
        messages.error(request, "Please correct the checkout form errors below.")
        return render(
            request,
            "orders/checkout.html",
            _build_checkout_context(request, form=form),
            status=400,
        )

    try:
        result = create_order_from_session_cart(
            session=request.session,
            user=request.user,
            shipping_address=form.build_shipping_address(),
        )
        _send_checkout_notifications(form, result)
    except CheckoutError as exc:
        messages.error(request, str(exc))
        return render(
            request,
            "orders/checkout.html",
            _build_checkout_context(request, form=form),
            status=400,
        )
    except Exception:
        messages.error(request, "We could not place your order right now. Please try again.")
        return render(
            request,
            "orders/checkout.html",
            _build_checkout_context(request, form=form),
            status=500,
        )

    request.session["recent_order_id"] = result.order.pk
    messages.success(request, f"Order #{result.order.pk} placed successfully.")
    return redirect(reverse("account-order-detail", kwargs={"pk": result.order.pk}))
