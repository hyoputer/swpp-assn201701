from rest_framework import permissions

class RoomListPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST' and request.user.username == 'omok_admin':
            return True
        else:
            return False

class DefaultPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
