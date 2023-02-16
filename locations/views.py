"""This unit contains CBV providing CRUD operations for location table"""
from rest_framework.viewsets import ModelViewSet
from locations.models import Location
from locations.serializers import LocationSerializer
# ------------------------------------------------------------------------


class LocationViewSet(ModelViewSet):
    """This view set provides all necessary functionality to work with
    location table"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
