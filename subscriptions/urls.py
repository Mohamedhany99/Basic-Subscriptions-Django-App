from django.urls import path
from .views import (
    RegisterUserView,
    CustomLoginView,
    PackageListView,
    SubscriptionCreateView,
    UserSubscriptionsView,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("packages/", PackageListView.as_view(), name="package-list"),
    path(
        "subscriptions/", SubscriptionCreateView.as_view(), name="subscription-create"
    ),
    path(
        "user/subscriptions/",
        UserSubscriptionsView.as_view(),
        name="user-subscriptions",
    ),
]
