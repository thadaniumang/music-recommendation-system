from django.urls import path
from .views import (
    RegisterView,
    VerifyEmail,
    LoginAPIView,
    LogoutAPIView,
    ChangePasswordView,
    RequestPasswordResetEmail,
    PasswordTokenCheckAPI,
    SetNewPasswordAPIView,
)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('email-verify', VerifyEmail.as_view(), name="email-verify"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutAPIView.as_view(), name="logout"),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('request-reset-email', RequestPasswordResetEmail.as_view(),
         name='request-rest-email'),
    path('password-reset/<uidb64>/<token>',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
]
