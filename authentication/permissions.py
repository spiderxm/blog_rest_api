from rest_framework import permissions
from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Specifying permissions for users"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
