"""This file contains fixtures and registered factories for testing purposes"""
import pytest
from pytest_factoryboy import register
from tests.factories import AdsFactory, CategoryFactory, UserFactory
# --------------------------------------------------------------------------

register(UserFactory)
register(CategoryFactory)
register(AdsFactory)


@pytest.mark.django_db
@pytest.fixture
def get_token(client, django_user_model) -> tuple[str, int]:
    """This fixture serves to create a user and return his id with an
    access token
    :param client: a test client
    :param django_user_model: a fixture to create a new user
    :return: a tuple with an access token and a user id
    """
    user_data = {
        "username": "legat88",
        "first_name": "Legat",
        "last_name": "Cezar",
        "email": "legat777@rambler.ru",
        "birth_date": "2010-10-07",
        "password": "legat777"
    }

    user = django_user_model.objects.create_user(**user_data)
    user_data['location'] = []
    response = client.post('/user/token/', data=user_data, format='json')

    return response.data.get('access'), user.pk
