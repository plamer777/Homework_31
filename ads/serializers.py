"""This file contains serializer classes to serialize and deserialize
advertisement models"""
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ads.models import Ads, Category
from users.models import User
# -------------------------------------------------------------------------


def is_true(value: bool) -> None:
    """This function checks if a value is not true
    :param value: the boolean to check
    """
    if value:
        raise ValidationError('Invalid value, use false instead')


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


class AdsCreateSerializer(serializers.ModelSerializer):
    """The AdsCreateSerializer class serves to work with AdsCreateView"""
    is_published = serializers.BooleanField(validators=[is_true])

    class Meta:
        model = Ads
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        author = instance.author
        category = instance.category
        data['author'] = author.first_name if author else None
        data['category'] = category.name if category else None
        return data


class CategoryCreateSerializer(serializers.ModelSerializer):
    """The CategoryCreateSerializer class serves to work with
    CategoryCreateView"""
    class Meta:
        model = Category
        fields = '__all__'
