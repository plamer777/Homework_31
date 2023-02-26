"""There are a few permission classes in the file serving to restrict access
to selections for users who are not an owners of the selections"""
import json
from json import JSONDecodeError

from rest_framework import permissions
# -------------------------------------------------------------------------


class SelectionCreatePermission(permissions.BasePermission):
    """SelectionCreatePermission class serves to restrict selection creation
    with another owner id"""
    def has_permission(self, request, view):
        try:
            owner_id = json.loads(request.body).get('owner')
        except JSONDecodeError:
            owner_id = None

        if request.user.id == owner_id:
            return True
        elif not owner_id:
            return True

        return False


class SelectionUpdateDeletePermission(permissions.BasePermission):
    """This permission class serves to prohibit to change or delete selection
    for users who are not the selection's owners"""
    def has_object_permission(self, request, view, obj):
        owner_id = json.loads(request.body).get('owner')

        if request.user.id != obj.owner.id:
            return False

        elif request.user.id != owner_id:
            return False

        return True
