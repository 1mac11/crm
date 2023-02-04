from rest_framework import viewsets, generics, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Company, Location, LocationImages
from .serializers import LocationSerializer, LocationImagesSerializer
from .permissions import IsLocationOwner, IsLocationImagesOwner


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    permission_classes = [IsAuthenticated, IsLocationOwner]
    serializer_class = LocationSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')

    def list(self, request, *args, **kwargs):
        queryset = Location.objects.filter(company__owner_id=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LocationImagesViewSet(viewsets.ModelViewSet):
    queryset = LocationImages.objects.all()
    permission_classes = [IsAuthenticated, IsLocationImagesOwner]
    serializer_class = LocationImagesSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    parser_classes = (FormParser, MultiPartParser)

    def list(self, request, *args, **kwargs):
        queryset = LocationImages.objects.filter(location__company__owner_id=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
