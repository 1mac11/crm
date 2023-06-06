from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.response import Response
from .models import Clients
from clients import serializers
from rest_framework import generics


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

# class MyClientsListView(generics.GenericAPIView):
#     serializer_class = serializers.MyClientsSerializer
#
#     def post(self, request):
#         company_id = request.data.get('company_id')
#         # below we get the clients by comparing their bought_products' company ids with our company id
#         clients = Clients.objects.filter(bought_products__company_id=company_id)
#         serializer = serializers.ClientSerializer(clients, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class FilteredClientsList(generics.ListAPIView):
#     queryset = Clients.objects.all()
#     serializer_class = serializers.ClientSerializer
#     filterset_class = ClientFilter
#     # filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['name', 'surname', 'phone', 'email']
