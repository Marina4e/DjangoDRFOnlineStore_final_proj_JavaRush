from django.urls import path

from users.views import (
    AccountView,
    AccountOrderDetailView,
    AccountOrdersView,
    AddressCreateView,
    AddressUpdateView,
    ProfileUpdateView,
    RegisterView,
    StoreLoginView,
    StorePasswordChangeDoneView,
    StorePasswordChangeView,
    address_delete,
    logout_view,
)


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", StoreLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("account/", AccountView.as_view(), name="account-detail"),
    path("account/orders/", AccountOrdersView.as_view(), name="account-orders"),
    path(
        "account/orders/<int:pk>/",
        AccountOrderDetailView.as_view(),
        name="account-order-detail",
    ),
    path("account/profile/", ProfileUpdateView.as_view(), name="account-profile-update"),
    path("account/addresses/add/", AddressCreateView.as_view(), name="address-create"),
    path(
        "account/addresses/<int:pk>/edit/",
        AddressUpdateView.as_view(),
        name="address-update",
    ),
    path("account/addresses/<int:pk>/delete/", address_delete, name="address-delete"),
    path(
        "password/change/",
        StorePasswordChangeView.as_view(),
        name="password-change",
    ),
    path(
        "password/change/done/",
        StorePasswordChangeDoneView.as_view(),
        name="password-change-done",
    ),
]
