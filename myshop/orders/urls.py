from django.urls import path

from orders.views import (
    cart_add,
    cart_detail,
    cart_remove,
    cart_update,
    checkout_detail,
    checkout_submit,
)


urlpatterns = [
    path("cart/", cart_detail, name="cart-detail"),
    path("cart/add/<int:product_id>/", cart_add, name="cart-add"),
    path("cart/items/<int:product_id>/", cart_update, name="cart-update"),
    path("cart/items/<int:product_id>/remove/", cart_remove, name="cart-remove"),
    path("checkout/", checkout_detail, name="checkout-detail"),
    path("checkout/submit/", checkout_submit, name="checkout-submit"),
]
