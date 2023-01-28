from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Company
from .serializers import CompanySerializer
from .permissions import IsOwner


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CompanySerializer
    http_method_names = ('get', 'post', 'patch', 'delete')
