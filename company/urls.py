from django.urls import path, include
from rest_framework import routers
from company import views

router = routers.DefaultRouter()

router.register(r'company', views.CompanyViewSet)
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    path('myproducts/', views.MyProductsListView.as_view(), name='myproducts'),
    path('', include(router.urls)),
]
