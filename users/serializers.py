"""There are a few serialization classes in the file for different purposes
such as getting all records from user table or single one, to add new
records, etc."""
from rest_framework import serializers
from users.models import User
from locations.models import Location
# --------------------------------------------------------------------------


class UserListSerializer(serializers.ModelSerializer):
    """This class serves to serialize and deserialize a list of user models"""
    location = serializers.SlugRelatedField(slug_field='name', read_only=True)
    total_ads = serializers.IntegerField()

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['location'] = result['location'].split(', ')
        return result

    def to_internal_value(self, data):
        data['location'] = ', '.join(data['location'])

    class Meta:
        model = User
        exclude = ['password']


class UserDetailSerializer(serializers.ModelSerializer):
    """This class serves to serialize and deserialize a single user model"""
    location = serializers.SlugRelatedField(slug_field='name', read_only=True)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['location'] = result['location'].split(', ')
        return result

    def to_internal_value(self, data):
        data['location'] = ', '.join(data['location'])

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    """This class serves to serialize newly added user"""
    id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        slug_field='name', queryset=User.objects.all(), required=False)

    def to_internal_value(self, data):
        location_name = ', '.join(data['location'])
        created, _ = Location.objects.get_or_create(name=location_name)
        data['location'] = created
        return data

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['location'] = instance.location.name.split(', ')
        return result

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        exclude = ['password']


class UserUpdateSerializer(serializers.ModelSerializer):
    """This class serves to serialize updated user data"""

    location = serializers.SlugRelatedField(
        slug_field='name', queryset=Location.objects.all(), required=False)

    def to_internal_value(self, data):
        location = ', '.join(data['location'])
        created, _ = Location.objects.get_or_create(name=location)
        data['location'] = created
        return data

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['location'] = instance.location.name.split(', ')
        result.pop('role')
        result.pop('password')
        return result

    class Meta:
        model = User
        fields = '__all__'
