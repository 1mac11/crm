from rest_framework import serializers

from location.models import Location
from .models import Company, Product


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'email', 'phone', 'owner', 'employee')
        extra_kwargs = {
            'owner': {'read_only': True},
            'employee': {'read_only': True}
        }

    def validate(self, attrs):
        phone = attrs.get('phone')
        if not phone.isnumeric() or len(phone) > 12:
            raise serializers.ValidationError('phone number is too length or has not numeric symbols')
        return attrs

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        print(self.context['request'].user)
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'available', 'price', 'count', 'company_id')


class CompanyDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)
