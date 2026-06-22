from django.urls import path

from products.views import ProductCatalogView


urlpatterns = [
    path("", ProductCatalogView.as_view(), name="product-list"),
]
