# posts/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Safe methods allowed for all. Write allowed only to object owner.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute `author`.
        return getattr(obj, 'author', None) == request.user
