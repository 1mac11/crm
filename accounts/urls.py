from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'accounts'

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name="register"),
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('verify_email', views.VerifyEmail.as_view(), name="verify_email"),
    path('password_reset', views.password_reset, name="password_reset"),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]