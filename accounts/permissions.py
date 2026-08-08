from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        return request.method in ["GET", "HEAD", "OPTIONS"]


class IsAdminOrFaculty(BasePermission):
    """
    Admins and Faculty can access the endpoint.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        return request.user.groups.filter(
            name__in=["Admin", "Faculty"]
        ).exists()


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        return (
            request.user.is_superuser
            or request.user.groups.filter(name="Admin").exists()
        )