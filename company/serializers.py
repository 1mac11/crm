from rest_framework import serializers
from .models import Company, Location, LocationImages


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


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'address', 'company', 'employee')
        extra_kwargs = {
            'employee': {'read_only': True},
            'company': {'write_only': True}
        }

    def validate(self, attrs):
        print(attrs)
        company = attrs.get('company')
        if self.context['request'].user != company.owner:
            raise serializers.ValidationError(
                f'for creating a location you must be owner for company: {company}')

        return attrs


class LocationImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    def validate(self, attrs):
        print(attrs)
        location = attrs.get('location')
        print(self.context['request'].user)
        print(location.company.owner)
        if self.context['request'].user != location.company.owner:
            raise serializers.ValidationError(
                f'for adding a location image you must be owner for company: {location.company}')

        return attrs

    class Meta:
        model = LocationImages
        fields = ('id', 'title', 'location', 'image')
