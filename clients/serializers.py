from rest_framework import serializers
from .models import Clients


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('name', 'surname', 'email', 'phone', 'bought_products', 'address')


class MyClientsSerializer(serializers.Serializer):
    company_id = serializers.IntegerField(default=1)


class SendingEmailsSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()
    from_email = serializers.CharField()
