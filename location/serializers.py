from rest_framework import serializers
from .models import Location, LocationImages


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'address', 'company', 'employee')
        extra_kwargs = {
            'employee': {'read_only': True},
        }

    def validate(self, attrs):
        company = attrs.get('company')
        if self.context['request'].user != company.owner:
            raise serializers.ValidationError(
                f'for creating a location you must be owner for company: {company}')

        return attrs


class LocationImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    def validate(self, attrs):
        location = attrs.get('location')
        if self.context['request'].user != location.company.owner:
            raise serializers.ValidationError(
                f'for adding a location image you must be owner for company: {location.company}')

        return attrs

    class Meta:
        model = LocationImages
        fields = ('id', 'title', 'location', 'image')
