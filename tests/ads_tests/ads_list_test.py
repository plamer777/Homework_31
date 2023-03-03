"""This file contains a test_ads_list function to test AdsView"""
import pytest
from tests.factories import AdsFactory
from ads.serializers import AdsSerializer
# --------------------------------------------------------------------------


@pytest.mark.django_db
def test_ads_list(client) -> None:
    """This function serves to test AdsView of ads app
    :param client: a test client
    """
    new_ads = AdsFactory.create_batch(8)
    expected = {
        'items': [dict(item) for item in AdsSerializer(new_ads,
                                                       many=True).data],
        'total': 8,
        'num_pages': 1
    }
    response = client.get('/ad/', content_type='application/json')
    assert response.status_code == 200
    assert expected == response.json()
