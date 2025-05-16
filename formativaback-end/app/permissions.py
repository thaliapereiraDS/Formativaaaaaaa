from rest_framework.permissions import BasePermission

class IsGestor(BasePermission):
    def has_permission(self, request, views):
        return request.user and request.user.is_authenticated and request.user.is_gestor

class IsProfessor(BasePermission):
    def has_permission(self, request, views):
        return request.user and request.user.is_authenticated and request.user.is_professor