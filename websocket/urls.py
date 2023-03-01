from django.urls import path
from .views import random

urlpatterns = [
    path('', random)
]
