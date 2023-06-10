from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from .models import Clients
from clients import serializers


class ClientFilter(FilterSet):
    class Meta:
        model = Clients
        fields = {
            'name': ['icontains'],
            'surname': ['icontains'],
            'phone': ['icontains'],
            'email': ['icontains'],

        }


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    # permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = serializers.ClientSerializer
    filterset_class = ClientFilter
    http_method_names = ('get', 'post', 'patch', 'delete')


