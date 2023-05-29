from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Clients
from clients import serializers
from rest_framework import generics


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    # permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = serializers.ClientSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')


class MyClientsListView(generics.GenericAPIView):
    serializer_class = serializers.MyClientsSerializer

    def post(self, request):
        company_id = request.data.get('company_id')
        clients = Clients.objects.filter(bought_products__company_id=company_id)
        serializer = serializers.ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
