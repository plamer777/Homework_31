"""This file contains serializer classes to serialize and deserialize
selection models"""
from rest_framework import serializers
from ads.models import Ads
from ads.serializers import AdsSerializer
from selections.models import Selection
from users.models import User
# -------------------------------------------------------------------------


class SelectionListSerializer(serializers.ModelSerializer):
    """SelectionListSerializer class serves to work with lists of selection
    models"""
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionRetrieveSerializer(serializers.ModelSerializer):
    """This serializer serves to work with single selection"""
    items = AdsSerializer(many=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionChangeSerializer(serializers.ModelSerializer):
    """SelectionCreateSerializer class serves to work with Create, Update and
    Delete views"""
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    items = serializers.PrimaryKeyRelatedField(queryset=Ads.objects.all(),
                                               many=True)

    class Meta:
        model = Selection
        fields = '__all__'
