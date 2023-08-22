from django.urls import path
from server.apps.users.controllers.AuthUser import AuthUserController
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)


urlpatterns = [
    path("auth/login/", AuthUserController.as_view(), name="login"),
    path(
        "auth/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "auth/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
    path(
        "auth/blacklist/",
        TokenBlacklistView.as_view(),
        name="token_blacklist",
    ),
]
