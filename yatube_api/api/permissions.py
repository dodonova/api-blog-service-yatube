
from rest_framework import permissions


class AuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class OwnerOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class UserIsNotFolowing(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.following != request.user
