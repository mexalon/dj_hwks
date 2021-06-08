from rest_framework import permissions


class MyFirstPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator or request.user.is_staff
