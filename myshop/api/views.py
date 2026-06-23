from __future__ import annotations

from decimal import Decimal
from decimal import InvalidOperation
from typing import cast

from django.db.models import Avg, Count, Prefetch
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
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
    TokenAccessResponseSerializer,
    TokenLoginRequestSerializer,
    TokenPairResponseSerializer,
    TokenRefreshRequestSerializer,
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


@extend_schema(
    tags=["Users"],
    summary="Register an API user",
    description="Create a new user account for JWT-based API access.",
    request=UserRegistrationSerializer,
    responses={201: UserRegistrationSerializer},
    examples=[
        OpenApiExample(
            "Registration request",
            value={
                "username": "new-brewer",
                "password": "VeryStrongPass123",
                "email": "new-brewer@example.com",
                "first_name": "New",
                "last_name": "Brewer",
            },
            request_only=True,
        )
    ],
)
class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(
    tags=["Users"],
    summary="Get JWT access and refresh tokens",
    description=(
        "Submit username and password to receive an access token and a refresh token. "
        "Use the access token as `Authorization: Bearer <token>`."
    ),
    request=TokenLoginRequestSerializer,
    responses={200: TokenAccessResponseSerializer},
    examples=[
        OpenApiExample(
            "JWT login request",
            value={"username": "api-user", "password": "strong-password-123"},
            request_only=True,
        ),
        OpenApiExample(
            "JWT login response",
            value={"refresh": "<refresh_token>", "access": "<access_token>"},
            response_only=True,
        ),
    ],
)
class UserLoginAPIView(TokenObtainPairView):
    serializer_class = StoreTokenObtainPairSerializer


@extend_schema(
    tags=["Users"],
    summary="Refresh a JWT access token",
    description=(
        "Exchange a valid refresh token for a fresh access token when the access token "
        "expires."
    ),
    request=TokenRefreshRequestSerializer,
    responses={200: TokenPairResponseSerializer},
    examples=[
        OpenApiExample(
            "Refresh request",
            value={"refresh": "<refresh_token>"},
            request_only=True,
        ),
        OpenApiExample(
            "Refresh response",
            value={"access": "<new_access_token>"},
            response_only=True,
        ),
    ],
)
class UserTokenRefreshAPIView(TokenRefreshView):
    pass


@extend_schema(
    tags=["Products"],
    summary="List active products",
    description="Return active catalog products with pagination, search, and basic filtering.",
    parameters=[
        OpenApiParameter(
            name="q",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Search by product name or description.",
        ),
        OpenApiParameter(
            name="category",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Category slug filter.",
        ),
        OpenApiParameter(
            name="min_price",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Minimum price filter, for example `10.00`.",
        ),
        OpenApiParameter(
            name="max_price",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Maximum price filter, for example `25.00`.",
        ),
    ],
    examples=[
        OpenApiExample(
            "Filtered product list",
            value={"count": 1, "next": None, "previous": None, "results": []},
            response_only=True,
        )
    ],
)
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


@extend_schema(
    tags=["Products"],
    summary="Retrieve a product",
    description="Return a single active product with review summary and review list.",
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


@extend_schema_view(
    get=extend_schema(
        tags=["Reviews"],
        summary="List product reviews",
        description="Return published reviews for a single product.",
    ),
    post=extend_schema(
        tags=["Reviews"],
        summary="Create a product review",
        description=(
            "Create a review for a purchased product. Requires JWT authentication and a "
            "previous order containing the product."
        ),
        request=ReviewCreateSerializer,
        responses={
            201: ReviewCreateSerializer,
            400: OpenApiResponse(description="Purchase validation or rating validation failed."),
            401: OpenApiResponse(description="Authentication required."),
        },
        examples=[
            OpenApiExample(
                "Review request",
                value={"rating": 5, "comment": "Excellent ingredients and fast delivery."},
                request_only=True,
            )
        ],
    ),
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


@extend_schema_view(
    get=extend_schema(
        tags=["Cart"],
        summary="Get the current session cart",
        description=(
            "Return cart contents stored in the current Django session. Preserve cookies "
            "between cart and order requests."
        ),
        responses={200: CartSummarySerializer},
    ),
    post=extend_schema(
        tags=["Cart"],
        summary="Add a product to the cart",
        request=CartItemActionSerializer,
        responses={
            201: CartMutationResponseSerializer,
            400: OpenApiResponse(description="Cart or stock validation failed."),
        },
        examples=[
            OpenApiExample(
                "Add to cart",
                value={"product_id": 1, "quantity": 2},
                request_only=True,
            )
        ],
    ),
    patch=extend_schema(
        tags=["Cart"],
        summary="Update cart quantity",
        request=CartItemActionSerializer,
        responses={
            200: CartMutationResponseSerializer,
            400: OpenApiResponse(description="Quantity or stock validation failed."),
        },
    ),
    delete=extend_schema(
        tags=["Cart"],
        summary="Remove a cart item",
        request=CartItemActionSerializer,
        responses={200: CartMutationResponseSerializer},
    ),
)
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


@extend_schema_view(
    get=extend_schema(
        tags=["Orders"],
        summary="List the current user's orders",
        description="Return only orders owned by the authenticated user.",
    ),
    post=extend_schema(
        tags=["Orders"],
        summary="Create an order from the current session cart",
        description=(
            "Create an order using the current session cart. Provide either a saved "
            "`address_id` or a raw `shipping_address` string."
        ),
        request=OrderCreateSerializer,
        responses={
            201: OrderSerializer,
            400: OpenApiResponse(description="Cart, stock, or address validation failed."),
            401: OpenApiResponse(description="Authentication required."),
        },
        examples=[
            OpenApiExample(
                "Create order with saved address",
                value={"address_id": 1},
                request_only=True,
            ),
            OpenApiExample(
                "Create order with inline address",
                value={"shipping_address": "42 Brewery Lane, Kyiv, 02000, Ukraine"},
                request_only=True,
            ),
        ],
    ),
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


@extend_schema_view(
    get=extend_schema(
        tags=["Orders"],
        summary="Retrieve one of the current user's orders",
        responses={200: OrderSerializer, 404: OpenApiResponse(description="Order not found.")},
    ),
    put=extend_schema(
        tags=["Orders"],
        summary="Cancel an order",
        description="Users may only change their own order status to `cancelled`.",
        request=OrderStatusUpdateSerializer,
        responses={
            200: OrderSerializer,
            400: OpenApiResponse(description="The order can no longer be changed."),
            401: OpenApiResponse(description="Authentication required."),
            404: OpenApiResponse(description="Order not found."),
        },
        examples=[
            OpenApiExample(
                "Cancel payload",
                value={"status": "cancelled"},
                request_only=True,
            )
        ],
    ),
    patch=extend_schema(
        tags=["Orders"],
        summary="Cancel an order",
        description="PATCH behaves the same as PUT for cancellation in this project.",
        request=OrderStatusUpdateSerializer,
        responses={
            200: OrderSerializer,
            400: OpenApiResponse(description="The order can no longer be changed."),
        },
    ),
    delete=extend_schema(
        tags=["Orders"],
        summary="Cancel an order",
        description="DELETE performs cancellation instead of removing the database row.",
        responses={
            204: OpenApiResponse(description="Order cancelled."),
            400: OpenApiResponse(description="The order can no longer be cancelled."),
            401: OpenApiResponse(description="Authentication required."),
            404: OpenApiResponse(description="Order not found."),
        },
    ),
)
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
