from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from websocket.models import Notifications
from accounts.views import Pagination10To100
from .models import Company, Product
from .serializers import CompanySerializer, ProductSerializer
from .permissions import IsOwner, IsCompanyOwnerOrEmployee


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


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsCompanyOwnerOrEmployee, IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = Pagination10To100
    http_method_names = ('get', 'post', 'patch', 'delete')

    def list(self, request, *args, **kwargs):

        queryset = Product.objects.filter(company__owner__id=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        pk = request.data.get('company_id')
        company = Company.objects.get(id=pk)
        if request.user != company.owner:
            return Response({'message': 'Only owner of company can create the new product'},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def __get_changes_of_two_dicts(self, data, new_data):
        s = '\n'
        for key in new_data:
            if data.get(key, []) != new_data[key]:
                s += f'{key}: from {data.get(key, "")} to {new_data[key]}\n'

        return s

    def partial_update(self, request, *args, **kwargs):

        user = request.user
        new_data = request.data
        pk = kwargs.get('pk')
        product = Product.objects.get(id=pk)
        changed_data = self.__get_changes_of_two_dicts(product.__dict__, new_data)
        Notifications.objects.create(title=f'user: {user} tried to change {product} ',
                                     description=f'user {user} tried to change product {product} data, {changed_data}',
                                     company=product.company)

        return super().partial_update(request, *args, **kwargs)
