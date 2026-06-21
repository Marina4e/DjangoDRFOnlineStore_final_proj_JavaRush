"""Root URL configuration for the online store project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import include, path


def home(request: HttpRequest) -> HttpResponse:
    """Return a small placeholder response for the project foundation stage."""
    return HttpResponse("myshop foundation is up", content_type="text/plain")


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path("orders/", include("orders.urls")),
    path("users/", include("users.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
