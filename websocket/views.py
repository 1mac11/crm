from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import NotificationSerializer
from .models import Notifications
from .permissions import IsOwner


def random(request):
    return render(request, 'basic_count.html', context={'text': "hello world"})


class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    http_method_names = ('get', 'delete')

    def list(self, request, *args, **kwargs):
        queryset = Notifications.objects.filter(company__owner__id=request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.read_status = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
