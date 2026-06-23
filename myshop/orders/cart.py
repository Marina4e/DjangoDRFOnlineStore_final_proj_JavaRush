from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from django.contrib.sessions.backends.base import SessionBase

from products.models import Product


CART_SESSION_KEY = "cart"


@dataclass(frozen=True)
class CartLine:
    product: Product
    quantity: int
    line_total: Decimal


class CartError(Exception):
    """Raised when a cart operation cannot be completed."""


def _get_cart_data(session: SessionBase) -> dict[str, int]:
    cart = session.get(CART_SESSION_KEY, {})
    return {str(key): int(value) for key, value in cart.items()}


def _save_cart_data(session: SessionBase, cart: dict[str, int]) -> None:
    session[CART_SESSION_KEY] = cart
    session.modified = True


def add_product(session: SessionBase, product: Product, quantity: int) -> int:
    if quantity < 1:
        raise CartError("Quantity must be at least 1.")
    if product.stock < 1:
        raise CartError("This product is currently out of stock.")

    cart = _get_cart_data(session)
    key = str(product.pk)
    new_quantity = cart.get(key, 0) + quantity
    if new_quantity > product.stock:
        raise CartError("Requested quantity exceeds available stock.")

    cart[key] = new_quantity
    _save_cart_data(session, cart)
    return new_quantity


def update_product_quantity(session: SessionBase, product: Product, quantity: int) -> int:
    if quantity < 1:
        raise CartError("Quantity must be at least 1.")
    if quantity > product.stock:
        raise CartError("Requested quantity exceeds available stock.")

    cart = _get_cart_data(session)
    cart[str(product.pk)] = quantity
    _save_cart_data(session, cart)
    return quantity


def remove_product(session: SessionBase, product_id: int) -> None:
    cart = _get_cart_data(session)
    if str(product_id) in cart:
        cart.pop(str(product_id), None)
        _save_cart_data(session, cart)


def get_cart_summary(session: SessionBase) -> dict[str, object]:
    cart = _get_cart_data(session)
    product_ids = [int(product_id) for product_id in cart.keys()]
    products = Product.objects.active().filter(id__in=product_ids).select_related("category")
    products_by_id = {product.id: product for product in products}

    lines: list[CartLine] = []
    subtotal = Decimal("0.00")
    total_quantity = 0
    cleaned_cart: dict[str, int] = {}

    for raw_product_id, quantity in cart.items():
        product = products_by_id.get(int(raw_product_id))
        if product is None:
            continue

        safe_quantity = min(quantity, product.stock)
        if safe_quantity < 1:
            continue

        cleaned_cart[str(product.id)] = safe_quantity
        line_total = product.price * safe_quantity
        lines.append(
            CartLine(
                product=product,
                quantity=safe_quantity,
                line_total=line_total,
            )
        )
        subtotal += line_total
        total_quantity += safe_quantity

    if cleaned_cart != cart:
        _save_cart_data(session, cleaned_cart)

    return {
        "lines": lines,
        "subtotal": subtotal,
        "total_quantity": total_quantity,
        "is_empty": not lines,
    }
