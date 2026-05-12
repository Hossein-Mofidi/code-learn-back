from attr.validators import instance_of
from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class IsVerifiedInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_verified

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_verified


class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return not isinstance(request.user, AnonymousUser) and request.user.role != 'student'

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)