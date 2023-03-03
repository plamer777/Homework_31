"""This file contains a test_create_ad function to test AdsCreateView"""
import pytest
# --------------------------------------------------------------------------


@pytest.mark.django_db
def test_create_ad(client) -> None:
    """This function serves to test AdsCreateView of ads app
    :param client: a test client
    """
    new_ad = {
        "name": "Дубовый шкаф",
        "price": 24000,
        "description": "test",
        "is_published": False
    }
    response = client.post('/ad/create/', data=new_ad,
                           content_type="application/json")

    expected = {
        "id": response.data.get('id'),
        "is_published": False,
        "name": "Дубовый шкаф",
        "price": 24000,
        "image": None,
        "description": "test",
        "author": None,
        "category": None
    }

    assert response.status_code == 201
    assert response.data == expected
