from rest_framework import serializers
from .models import Company


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


