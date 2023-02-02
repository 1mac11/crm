from rest_framework import viewsets, generics, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Company, Location, LocationImages
from .serializers import CompanySerializer, LocationSerializer, LocationImagesSerializer
from .permissions import IsOwner, IsLocationOwner, IsLocationImagesOwner


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CompanySerializer
    http_method_names = ('get', 'post', 'patch', 'delete')


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    permission_classes = [IsAuthenticated, IsLocationOwner]
    serializer_class = LocationSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')


class LocationImagesViewSet(viewsets.ModelViewSet):
    queryset = LocationImages.objects.all()
    permission_classes = [IsAuthenticated, IsLocationImagesOwner]
    serializer_class = LocationImagesSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
    parser_classes = (FormParser, MultiPartParser)


class MyCompaniesAPIView(generics.GenericAPIView):
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CompanySerializer

    def get(self, request):
        user = request.user
        queryset = Company.objects.filter(owner=user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)