"""This file contains a test_ad_retrieve function to test AdsEntityView"""
import pytest
from ads.serializers import AdsSerializer
# --------------------------------------------------------------------------


@pytest.mark.django_db
def test_ad_retrieve(client, ads, get_token) -> None:
    """This function serves to test AdsEntityView of ads app
    :param client: a test client
    :param ads: AdsFactory fixture
    :param get_token: a fixture returning an access token and user id
    """
    expected = AdsSerializer(ads).data

    response = client.get(f'/ad/{ads.id}/',
                          content_type='application/json',
                          HTTP_AUTHORIZATION='Bearer ' + get_token[0])

    assert response.status_code == 200
    assert expected == response.json()
