from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsCreatorManagerOrRedonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        import ipdb; ipdb.set_trace()
        if request.method in SAFE_METHODS:
            return True
        # in_develop