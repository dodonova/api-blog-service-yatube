from rest_framework import permissions


class AuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Custom permission class to allow only the author of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to perform the given action.
        """
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class OwnerOnly(permissions.IsAuthenticated):
    """
    Custom permission class to allow only the owner of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting user is the owner of the object.
        """
        return obj.owner == request.user


class UserIsNotFolowing(permissions.IsAuthenticated):
    """
    Custom permission class to allow access if the user is not following.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting user is not following the obj user.
        """
        return obj.following != request.user
