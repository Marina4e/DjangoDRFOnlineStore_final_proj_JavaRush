from __future__ import annotations

from typing import cast

from django.contrib import messages
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
from orders.forms import CartQuantityForm
from products.models import Product


def _render_cart(
    request: HttpRequest,
    *,
    status: int = 200,
) -> HttpResponse:
    summary = get_cart_summary(request.session)
    summary["is_htmx"] = request.headers.get("HX-Request") == "true"
    template_name = "orders/partials/cart_shell.html"
    if not summary["is_htmx"]:
        template_name = "orders/cart.html"
    return render(request, template_name, summary, status=status)


@require_GET
def cart_detail(request: HttpRequest) -> HttpResponse:
    return _render_cart(request)


@require_POST
def cart_add(request: HttpRequest, product_id: int) -> HttpResponse:
    product = get_object_or_404(Product.objects.active(), pk=product_id)
    form = CartQuantityForm(request.POST)
    redirect_to = request.POST.get("next") or reverse(
        "product-detail",
        kwargs={"slug": product.slug},
    )

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
    product = get_object_or_404(Product.objects.active(), pk=product_id)
    remove_product(request.session, product_id)
    messages.success(request, f"Removed {product.name} from the cart.")
    return _render_cart(request)
