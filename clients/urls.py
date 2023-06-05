from django.urls import path, include
from rest_framework import routers
from clients import views

router = routers.DefaultRouter()

router.register(r'', views.ClientsViewSet)

urlpatterns = [
    path('myclients/', views.MyClientsListView.as_view(), name='myclients_all'),
    path('clients_list/', views.FilteredClientsList.as_view(), name='clients_list_filtered'),
    path('', include(router.urls)),
]
