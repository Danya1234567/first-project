from rest_framework import permissions

class IsAdminOrAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'user':
            return True
        return obj.author == request.user