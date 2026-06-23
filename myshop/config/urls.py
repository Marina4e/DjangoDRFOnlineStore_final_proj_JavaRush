"""Root URL configuration for the online store project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from products.views import HomePageView, ProductDetailView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
    path("admin/", admin.site.urls),
    path("", include("orders.urls")),
    path("", include("users.urls")),
    path("products/", include("products.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
