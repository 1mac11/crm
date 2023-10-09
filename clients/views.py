from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.response import Response

from .models import Clients
from clients import serializers
from .send_emails_to_clients import send_emails
from .tasks import send_email_task


class ClientFilter(FilterSet):
    class Meta:
        model = Clients
        fields = {
            'name': ['icontains'],
            'surname': ['icontains'],
            'phone': ['icontains'],
            'email': ['icontains'],
            'bought_products__company_id': ['exact'],

        }


class SendingEmailsAPIView(generics.GenericAPIView):
    serializer_class = serializers.SendingEmailsSerializer

    def post(self, request):
        company_id = request.data.get('company_id')
        title = request.data.get('title')
        message = request.data.get('text')
        from_email = request.data.get('from_email')

        try:
            send_email_task.delay(company_id, title, message, from_email)
            return Response({'message': 'emails has been send succesfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print('ex:', e)
            return Response({'message': 'sorry'}, status=status.HTTP_400_BAD_REQUEST)


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    # permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = serializers.ClientSerializer
    filterset_class = ClientFilter
    http_method_names = ('get', 'post', 'patch', 'delete')
