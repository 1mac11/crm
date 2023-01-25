from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('verify_email', views.VerifyEmail.as_view(), name="verify_email"),
    path('email_verify_code_check', views.VerificationCodeCheck.as_view(), name="code_check"),
    path('forgot_password', views.ForgotPassword.as_view(), name="forgot_password"),
    path('change_password', views.SetNewPassword.as_view(), name="change_password"),
    path('user_detail', views.UserDetailView.as_view(), name="user_detail"),
    path('user_update', views.UserUpdateView.as_view(), name="user_update"),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
