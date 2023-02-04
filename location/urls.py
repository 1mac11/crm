from django.urls import path, include
from rest_framework import routers
from location import views

router = routers.DefaultRouter()

router.register(r'location', views.LocationViewSet)
router.register(r'location_images', views.LocationImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
