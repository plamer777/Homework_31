"""There is a serializer for LocationViewSet in the file that allows to
serialize and deserialize Location models"""
from rest_framework import serializers
from locations.models import Location
# ------------------------------------------------------------------------


class LocationSerializer(serializers.ModelSerializer):
    """LocationSerializer class is a serializer for Location models"""
    class Meta:
        model = Location
        fields = '__all__'
