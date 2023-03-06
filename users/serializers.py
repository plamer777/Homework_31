"""There are a few serialization classes in the file for different purposes
such as getting all records from user table or single one, to add new
records, etc."""
from datetime import date
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import User
from locations.models import Location
# --------------------------------------------------------------------------


class IsAgeValid:
    """The IsAgeValid class is a validator for user's age"""
    def __call__(self, value: str) -> None:
        difference = date.today() - date.fromisoformat(value)
        if difference.days / 365 < 9:
            raise ValidationError(
                {"birth_date": "You must be at least 9 years old"})


def is_email_unique(value: str) -> None:
    """This function serves to validate email address uniqueness
    :param value: the email address to validate
    """
    email_list = [user.email for user in User.objects.all()]
    if value in email_list:
        raise ValidationError(
            {'unique error': 'This email is already exists'})
    elif 'rambler.ru' in value:
        raise ValidationError(
            {'domain error': 'rambler.ru domain is not allowed'})


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
    birth_date = serializers.DateField()
    email = serializers.EmailField(validators=[is_email_unique, IsAgeValid()])
    location = serializers.SlugRelatedField(
        slug_field='name', queryset=User.objects.all(), required=False)

    def to_internal_value(self, data):
        super().to_internal_value(data)
        location_name = ', '.join(data['location'])
        created, _ = Location.objects.get_or_create(name=location_name)
        data['location'] = created
        return data

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['location'] = instance.location.name.split(', ')
        result.pop('password', None)
        return result

    # def validate(self, attrs):
    #     IsAgeValid()(attrs.get('birth_date', date.today()))
    #     is_email_unique(attrs.get('email', 'default@google.com'))
    #     if not attrs.get('password'):
    #         raise ValidationError({"password": "Password is required"})
    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = '__all__'


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
