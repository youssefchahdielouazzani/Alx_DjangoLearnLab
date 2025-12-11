from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Permission to allow only owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
