from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.views import Pagination10To100
from .models import Company
from .serializers import CompanySerializer
from .permissions import IsOwner


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = CompanySerializer
    pagination_class = Pagination10To100
    http_method_names = ('get', 'post', 'patch', 'delete')

    def list(self, request, *args, **kwargs):
        queryset = Company.objects.filter(owner_id=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
