"""This file contains selection ViewSet with full CRUD functionality"""
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from selections.models import Selection
from selections.permissions import SelectionCreatePermission, \
    SelectionUpdateDeletePermission
from selections.serializers import SelectionListSerializer, \
    SelectionRetrieveSerializer, SelectionChangeSerializer
# -------------------------------------------------------------------------


class SelectionView(ModelViewSet):
    """SelectionView provides CRUD functionality and restrict access for
    unauthenticated users or whose permissions are not allowed to create,
    change or delete selections"""
    queryset = Selection.objects.all()
    default_serializer = SelectionListSerializer
    serializers = {'list': SelectionListSerializer,
                   'retrieve': SelectionRetrieveSerializer,
                   'create': SelectionChangeSerializer,
                   'update': SelectionChangeSerializer,
                   'partial_update': SelectionChangeSerializer}
    default_permissions = [AllowAny]
    permissions = {'create': [IsAuthenticated,
                              SelectionCreatePermission],
                   'update': [IsAuthenticated,
                              SelectionUpdateDeletePermission],
                   'partial_update': [IsAuthenticated,
                                      SelectionUpdateDeletePermission],
                   'destroy': [IsAuthenticated,
                               SelectionUpdateDeletePermission]
                   }

    def get_serializer_class(self):
        serializer = self.serializers.get(self.action, self.default_serializer)

        return serializer

    def get_permissions(self):
        permissions = [permission() for permission in self.permissions.get(
            self.action, self.default_permissions)]
        return permissions
