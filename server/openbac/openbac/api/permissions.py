from rest_framework import permissions
import pprint

class IsSuperUserFullOrAnyonePost(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request,view):
        if request.method == "POST":
            return True

        if request.user.is_superuser and request.method in permissions.SAFE_METHODS:
            return True

        return False
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method == "POST":
            return True

        if request.user.is_superuser and request.method in permissions.SAFE_METHODS:
            return True

        return False
