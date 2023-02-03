from django.urls import path, include
from rest_framework import routers
from company import views

router = routers.DefaultRouter()

router.register(r'company', views.CompanyViewSet)
router.register(r'location', views.LocationViewSet)
router.register(r'location_images', views.LocationImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('my_companies/', views.MyCompaniesAPIView.as_view(), name='my_companies_list'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
