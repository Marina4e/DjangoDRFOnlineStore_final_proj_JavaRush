from __future__ import annotations

from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from orders.models import Order, OrderItem, OrderStatus
from products.models import Product, Review
from users.models import Address


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "email", "first_name", "last_name")

    def validate_password(self, value: str) -> str:
        validate_password(value)
        return value

    def create(self, validated_data: dict[str, Any]):
        password = validated_data.pop("password")
        user = get_user_model().objects.create_user(password=password, **validated_data)
        return user


class StoreTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.get_username()
        return token


class TokenLoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class TokenPairResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class TokenRefreshRequestSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class TokenAccessResponseSerializer(serializers.Serializer):
    access = serializers.CharField()


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)
    category_slug = serializers.CharField(source="category.slug", read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "price",
            "category",
            "category_slug",
            "stock",
            "is_active",
        )


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Review
        fields = ("id", "username", "rating", "comment", "created_at")
        read_only_fields = ("id", "username", "created_at")


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("rating", "comment")


class ProductDetailSerializer(ProductListSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "price",
            "category",
            "category_slug",
            "stock",
            "is_active",
            "review_count",
            "average_rating",
            "reviews",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product.id", read_only=True)
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ("id", "product_id", "product_name", "quantity", "price")


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "status",
            "total_price",
            "shipping_address",
            "created_at",
            "updated_at",
            "items",
        )
        read_only_fields = ("id", "created_at", "updated_at", "items", "total_price")


class OrderCreateSerializer(serializers.Serializer):
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.none(),
        required=False,
        allow_null=True,
    )
    shipping_address = serializers.CharField(required=False, allow_blank=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request is not None and request.user.is_authenticated:
            self.fields["address_id"].queryset = Address.objects.filter(user=request.user)

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        if not attrs.get("address_id") and not attrs.get("shipping_address"):
            raise serializers.ValidationError(
                "Provide either address_id or shipping_address."
            )
        return attrs

    def build_shipping_address(self) -> str:
        address = self.validated_data.get("address_id")
        if address is not None:
            lines = [
                f"Label: {address.label}",
                f"Recipient: {address.recipient_name}",
                f"Phone: {address.phone}",
                address.address_line1,
            ]
            if address.address_line2:
                lines.append(address.address_line2)
            lines.append(
                ", ".join([address.city, address.postal_code, address.country])
            )
            return "\n".join(lines)
        return str(self.validated_data["shipping_address"])


class OrderStatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=OrderStatus.choices)

    def validate_status(self, value: str) -> str:
        if value != OrderStatus.CANCELLED:
            raise serializers.ValidationError(
                "Users can only change their own orders to cancelled."
            )
        return value


class CartItemActionSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1, required=False)


class CartLineSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(source="product.id")
    product_name = serializers.CharField(source="product.name")
    product_slug = serializers.CharField(source="product.slug")
    quantity = serializers.IntegerField()
    unit_price = serializers.DecimalField(
        source="product.price",
        max_digits=10,
        decimal_places=2,
    )
    line_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField(source="product.stock")


class CartSummarySerializer(serializers.Serializer):
    lines = CartLineSerializer(many=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = serializers.IntegerField()
    is_empty = serializers.BooleanField()


class CartMutationResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()
    cart = CartSummarySerializer()
