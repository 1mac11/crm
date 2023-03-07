from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsCompanyOwnerOrEmployee(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.company.owner == request.user or (request.user in obj.company.employee.all())
