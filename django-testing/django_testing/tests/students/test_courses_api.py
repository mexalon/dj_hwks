import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK

from rest_framework.test import APIClient


@pytest.mark.django_db
def test_example():
    client = APIClient()
    url = reverse("courses-list")
    resp = client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    print(f'>>>>>>>>>>>>>>>{resp_json}')

