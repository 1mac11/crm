from django.urls import path, include
from rest_framework import routers
from . import views

from .views import random
router = routers.DefaultRouter()

router.register(r'notification', views.NotificationsViewSet)

urlpatterns = [
    path('', random),
    path('', include(router.urls)),
]
