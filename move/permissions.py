from rest_framework.permissions import BasePermission

class IsAuthenticatedAndCoinsEnough(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.data.get('from_user') == request.user.id:
                from_user = request.user
                coins_required = request.data.get('coins')
                return from_user.coins >= coins_required
        return False
