from rest_framework import permissions


class DebtListPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.user.username == 'debt_admin':
            return True
        return False

class AdminPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.username == 'debt_admin':
            return True

        return False

class DebtPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.username == 'debt_admin':
            return True

        if request.method in permissions.SAFE_METHODS:
            return obj.borrower == request.user or obj.lender == request.user

        if request.method == 'DELETE':
            return request.user == obj.lender 

class UserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.username == 'debt_admin':
            return True

        if request.method in permissions.SAFE_METHODS:
            return obj == request.user
