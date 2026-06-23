from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.sessions.backends.base import SessionBase
from django.db import transaction

from orders.cart import clear_cart, get_cart_quantities
from orders.models import Order, OrderItem, OrderStatus
from products.models import Product


@dataclass(frozen=True)
class CheckoutLine:
    product: Product
    quantity: int
    line_total: Decimal


@dataclass(frozen=True)
class CheckoutOrderResult:
    order: Order
    lines: list[CheckoutLine]
    total_quantity: int


class CheckoutError(Exception):
    """Raised when checkout cannot be completed safely."""


def create_order_from_session_cart(
    *,
    session: SessionBase,
    user: AbstractBaseUser,
    shipping_address: str,
) -> CheckoutOrderResult:
    cart = get_cart_quantities(session)
    if not cart:
        raise CheckoutError("Your cart is empty. Add products before checking out.")

    product_ids = [int(product_id) for product_id in cart.keys()]

    with transaction.atomic():
        products = (
            Product.objects.select_for_update()
            .filter(id__in=product_ids, is_active=True)
            .order_by("id")
        )
        products_by_id = {product.id: product for product in products}

        missing_ids = [product_id for product_id in product_ids if product_id not in products_by_id]
        if missing_ids:
            raise CheckoutError(
                "One or more products in your cart are no longer available. "
                "Please review your cart and try again."
            )

        subtotal = Decimal("0.00")
        total_quantity = 0
        lines: list[CheckoutLine] = []

        for raw_product_id, quantity in cart.items():
            product = products_by_id[int(raw_product_id)]
            if quantity < 1:
                raise CheckoutError("Your cart contains an invalid quantity.")
            if product.stock < quantity:
                raise CheckoutError(
                    f"Insufficient stock for {product.name}. Only {product.stock} left."
                )

            line_total = product.price * quantity
            subtotal += line_total
            total_quantity += quantity
            lines.append(
                CheckoutLine(
                    product=product,
                    quantity=quantity,
                    line_total=line_total,
                )
            )

        order = Order.objects.create(
            user=user,
            status=OrderStatus.PENDING,
            total_price=subtotal,
            shipping_address=shipping_address,
        )

        for line in lines:
            OrderItem.objects.create(
                order=order,
                product=line.product,
                quantity=line.quantity,
                price=line.product.price,
            )
            line.product.stock -= line.quantity
            line.product.save(update_fields=["stock", "updated_at"])

        clear_cart(session)

    return CheckoutOrderResult(order=order, lines=lines, total_quantity=total_quantity)
