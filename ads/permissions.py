"""This unit contains permission classes to check user's permissions to
change or delete advertisements"""
import json
from json import JSONDecodeError

from rest_framework import permissions
from users.models import User
# -------------------------------------------------------------------------


class IsOwnerPermission(permissions.BasePermission):
    """The IsOwnerPermission class serves to validate user's permission to
    change or delete advertisement

    :return: True if user is allowed to change or delete advertisement or
    False otherwise
    """
    def has_object_permission(self, request, view, obj):
        try:
            author_id = json.loads(request.body).get('author_id')
        except JSONDecodeError:
            author_id = None
        if not obj.author or request.user.id != obj.author.id:
            return False
        elif author_id and request.user.id != author_id:
            return False

        return True


class IsAdminModerator(permissions.BasePermission):
    """The IsAdminModerator class serves to allow user with admin or moderator
    permission change or delete any advertisement

    :return: True if user is admin or moderator or False otherwise
    """
    def has_object_permission(self, request, view, obj):

        if request.user.role not in [User.ADMIN, User.MODERATOR]:
            return False

        return True
