from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS)


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(request.method in SAFE_METHODS) or bool(request.user and request.user.is_staff)


class IsOwnerOrIsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return bool(request.user == obj.user or request.user.is_staff)


class IsAdminUserOrIsEmployer(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return bool(request.user.is_superuser or request.user.employer is not None)