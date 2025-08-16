from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    разрешаем SAFE-методы всем.
    Изменять/удалять объект может только его автор.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # у Post поле автора называется author
        return getattr(obj, "author_id", None) == request.user.id