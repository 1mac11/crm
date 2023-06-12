from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.response import Response

from .models import Clients
from clients import serializers
from .send_emails_to_clients import send_emails


class ClientFilter(FilterSet):
    class Meta:
        model = Clients
        fields = {
            'name': ['icontains'],
            'surname': ['icontains'],
            'phone': ['icontains'],
            'email': ['icontains'],

        }


class SendingEmailsAPIView(generics.GenericAPIView):
    serializer_class = serializers.SendingEmailsSerializer

    def post(self, request):
        company_id = request.data.get('company_id')
        title = request.data.get('title')
        text = request.data.get('text')
        from_email = request.data.get('from_email')

        try:
            send_emails(company_id, title, text, from_email)
            return Response({'message': 'emails has been send succesfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    # permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = serializers.ClientSerializer
    filterset_class = ClientFilter
    http_method_names = ('get', 'post', 'patch', 'delete')
