# to give permissions that django rest_framework giver to customize what can do each user
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit theier own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        # When the user make a request It will check that is on Safe methods, so it return true if the user is 
        # trying to update is own profile or return false. And also it will return the obj.id == request.user.id
        return obj.id == request.user.id