from django.urls import path

from api.views import (
    CartAPIView,
    OrderDetailAPIView,
    OrderListCreateAPIView,
    ProductDetailAPIView,
    ProductListAPIView,
    ReviewListCreateAPIView,
    UserLoginAPIView,
    UserRegistrationAPIView,
    UserTokenRefreshAPIView,
)


urlpatterns = [
    path("users/register/", UserRegistrationAPIView.as_view(), name="api-user-register"),
    path("users/login/", UserLoginAPIView.as_view(), name="api-user-login"),
    path(
        "users/token/refresh/",
        UserTokenRefreshAPIView.as_view(),
        name="api-token-refresh",
    ),
    path("products/", ProductListAPIView.as_view(), name="api-product-list"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="api-product-detail"),
    path(
        "products/<int:pk>/reviews/",
        ReviewListCreateAPIView.as_view(),
        name="api-product-reviews",
    ),
    path("orders/", OrderListCreateAPIView.as_view(), name="api-order-list"),
    path("orders/<int:pk>/", OrderDetailAPIView.as_view(), name="api-order-detail"),
    path("cart/", CartAPIView.as_view(), name="api-cart"),
]
