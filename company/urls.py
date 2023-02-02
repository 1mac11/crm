from django.urls import path, include
from rest_framework import routers
from company import views

company_router = routers.DefaultRouter()
company_router.register(r'company', views.CompanyViewSet)

location_router = routers.DefaultRouter()
location_router.register(r'', views.LocationViewSet)

location_images_router = routers.DefaultRouter()
location_images_router.register(r'', views.LocationImagesViewSet)

urlpatterns = [
    path('', include(company_router.urls)),
    path('location/', include(location_router.urls)),
    path('location_images/', include(location_images_router.urls)),
    path('my_companies/', views.MyCompaniesAPIView.as_view(), name='my_companies_list'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
