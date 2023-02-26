"""This file contains serializer classes to serialize and deserialize
advertisement models"""
from rest_framework import serializers
from ads.models import Ads
from users.models import User
# -------------------------------------------------------------------------


class AdsSerializer(serializers.ModelSerializer):
    """The AdsSerializer class serves to serialize and serialize Ads models"""

    author = serializers.PrimaryKeyRelatedField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        found_user = User.objects.get(pk=instance.author.id)
        data['author'] = found_user.first_name
        data['author_id'] = found_user.id
        return data

    class Meta:
        model = Ads
        fields = '__all__'
