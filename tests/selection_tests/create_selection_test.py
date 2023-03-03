"""This file contains a test_create_selection function to test
SelectionViewSet of selections app"""
import pytest
from tests.factories import AdsFactory
# --------------------------------------------------------------------------


@pytest.mark.django_db
def test_create_selection(client, get_token):
    """This function serves to test SelectionViewSet of selections app
    :param client: a test client
    :param get_token: a fixture returning an access token and user id
    """
    new_ads = AdsFactory.create_batch(3)
    new_selection = {
        "name": "My selection",
        "items": [ad.id for ad in new_ads],
        "owner": get_token[1]
    }

    response = client.post('/selection/', data=new_selection,
                           content_type="application/json",
                           HTTP_AUTHORIZATION="Bearer " + get_token[0]
                           )

    expected = {
        "id": response.data.get('id'),
        "name": "My selection",
        "items": [ad.id for ad in new_ads],
        "owner": get_token[1]
    }

    assert response.status_code == 201, response.data
    assert response.data == expected
