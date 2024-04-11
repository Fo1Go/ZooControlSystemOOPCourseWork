from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(request.method in SAFE_METHODS or (request.user and request.user.is_staff))


class IsOwnerOrIsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return bool(request.user == obj.user or request.user.is_staff)
