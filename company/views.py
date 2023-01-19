from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     print(data, request.user.id)
    #     if request.user.id:
    #         data['owner'] = request.user.id
    #         print(data)
    #         serializer = self.get_serializer(data=data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     else:
    #         return Response({'Error': 'Not authenticated'}, status=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED)