from __future__ import annotations

from decimal import Decimal
from decimal import InvalidOperation
from typing import cast

from django.db.models import Avg, Count, Prefetch
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.serializers import (
    CartItemActionSerializer,
    CartMutationResponseSerializer,
    CartSummarySerializer,
    OrderCreateSerializer,
    OrderSerializer,
    OrderStatusUpdateSerializer,
    ProductDetailSerializer,
    ProductListSerializer,
    ReviewCreateSerializer,
    ReviewSerializer,
    StoreTokenObtainPairSerializer,
    UserRegistrationSerializer,
)
from orders.cart import (
    CartError,
    add_product,
    get_cart_summary,
    remove_product,
    update_product_quantity,
)
from orders.models import Order, OrderItem, OrderStatus
from orders.services import CheckoutError, create_order_from_session_cart
from products.models import Product, Review


def parse_decimal(raw_value: str | None) -> Decimal | None:
    if not raw_value:
        return None
    try:
        return Decimal(raw_value)
    except InvalidOperation:
        return None


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = StoreTokenObtainPairSerializer


class UserTokenRefreshAPIView(TokenRefreshView):
    pass


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Product.objects.active().select_related("category")
        search_term = self.request.query_params.get("q", "").strip()
        category_slug = self.request.query_params.get("category", "").strip()
        min_price = parse_decimal(self.request.query_params.get("min_price"))
        max_price = parse_decimal(self.request.query_params.get("max_price"))
        return (
            queryset.search(search_term)
            .in_category(category_slug)
            .within_price_range(min_price, max_price)
            .order_by("name")
        )


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return (
            Product.objects.active()
            .select_related("category")
            .prefetch_related(
                Prefetch(
                    "reviews",
                    queryset=Review.objects.select_related("user").order_by("-created_at"),
                )
            )
            .annotate(review_count=Count("reviews"), average_rating=Avg("reviews__rating"))
        )


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        product = get_object_or_404(Product.objects.active(), pk=self.kwargs["pk"])
        return product.reviews.select_related("user").order_by("-created_at")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ReviewCreateSerializer
        return ReviewSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def perform_create(self, serializer: ReviewCreateSerializer) -> None:
        product = get_object_or_404(Product.objects.active(), pk=self.kwargs["pk"])
        has_purchased = OrderItem.objects.filter(
            order__user=self.request.user,
            order__status__in=[
                OrderStatus.PENDING,
                OrderStatus.PAID,
                OrderStatus.SHIPPED,
                OrderStatus.DELIVERED,
            ],
            product=product,
        ).exists()
        if not has_purchased:
            raise serializers.ValidationError(
                {"detail": "You can leave a review only after purchasing this product."}
            )
        serializer.save(product=product, user=self.request.user)


class CartAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request) -> Response:
        serializer = CartSummarySerializer(get_cart_summary(request.session))
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = CartItemActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(
            Product.objects.active(),
            pk=serializer.validated_data["product_id"],
        )
        quantity = cast(int, serializer.validated_data.get("quantity", 1))
        try:
            add_product(request.session, product, quantity)
        except CartError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            CartMutationResponseSerializer(
                {
                    "detail": f"{product.name} added to the cart.",
                    "cart": get_cart_summary(request.session),
                }
            ).data,
            status=status.HTTP_201_CREATED,
        )

    def patch(self, request: Request) -> Response:
        serializer = CartItemActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if "quantity" not in serializer.validated_data:
            raise serializers.ValidationError({"quantity": "This field is required."})
        product = get_object_or_404(
            Product.objects.active(),
            pk=serializer.validated_data["product_id"],
        )
        try:
            update_product_quantity(
                request.session,
                product,
                cast(int, serializer.validated_data["quantity"]),
            )
        except CartError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            CartMutationResponseSerializer(
                {
                    "detail": f"{product.name} quantity updated.",
                    "cart": get_cart_summary(request.session),
                }
            ).data
        )

    def delete(self, request: Request) -> Response:
        serializer = CartItemActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_id = cast(int, serializer.validated_data["product_id"])
        remove_product(request.session, product_id)
        return Response(
            CartMutationResponseSerializer(
                {
                    "detail": "Cart item removed.",
                    "cart": get_cart_summary(request.session),
                }
            ).data
        )


class OrderListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .prefetch_related("items__product")
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderCreateSerializer
        return OrderSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = create_order_from_session_cart(
                session=request.session,
                user=request.user,
                shipping_address=serializer.build_shipping_address(),
            )
        except CheckoutError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_400_BAD_REQUEST)

        output = OrderSerializer(result.order, context=self.get_serializer_context())
        return Response(output.data, status=status.HTTP_201_CREATED)


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .prefetch_related("items__product")
        )

    def update(self, request: Request, *args, **kwargs) -> Response:
        order = self.get_object()
        serializer = OrderStatusUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if order.status in {OrderStatus.CANCELLED, OrderStatus.DELIVERED}:
            return Response(
                {"detail": "This order can no longer be changed."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        order.status = OrderStatus.CANCELLED
        order.save(update_fields=["status", "updated_at"])
        return Response(OrderSerializer(order).data)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        order = self.get_object()
        if order.status in {OrderStatus.CANCELLED, OrderStatus.DELIVERED}:
            return Response(
                {"detail": "This order can no longer be cancelled."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        order.status = OrderStatus.CANCELLED
        order.save(update_fields=["status", "updated_at"])
        return Response(status=status.HTTP_204_NO_CONTENT)
