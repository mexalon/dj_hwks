import pytest
import random
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_course_retrieve(my_api_client, course_factory):
    the_course = course_factory(_quantity=1)
    its_id = the_course[0].id
    its_name = the_course[0].name
    url = reverse("courses-list")
    resp = my_api_client.get(url + f"{its_id}/")
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json.get('id') == its_id
    assert resp_json.get('name') == its_name


@pytest.mark.django_db
def test_course_list(my_api_client, course_factory):
    q = 10
    courses = course_factory(_quantity=q)
    url = reverse("courses-list")
    resp = my_api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == q
    assert {course.id for course in courses} == {course.get('id') for course in resp_json}
    assert {course.name for course in courses} == {course.get('name') for course in resp_json}


@pytest.mark.django_db
def test_course_id_filter(my_api_client, course_factory):
    q = 10
    courses = course_factory(_quantity=q)
    some_course = random.choice(courses)
    url = reverse("courses-list")
    resp = my_api_client.get(url, {'id': some_course.id})
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0].get('id') == some_course.id
    assert resp_json[0].get('name') == some_course.name


@pytest.mark.django_db
def test_course_name_filter(my_api_client, course_factory):
    q = 10
    courses = course_factory(_quantity=q)
    some_course = random.choice(courses)
    url = reverse("courses-list")
    resp = my_api_client.get(url, {'name': some_course.name})
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1
    assert resp_json[0].get('id') == some_course.id
    assert resp_json[0].get('name') == some_course.name


@pytest.mark.django_db
def test_course_create(my_api_client):
    some_course = {"name": "test_name"}
    url = reverse("courses-list")
    resp = my_api_client.post(url, some_course)
    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert resp_json.get('name') == some_course.get("name")


@pytest.mark.django_db
def test_course_patch(my_api_client, course_factory):
    default_course = course_factory(_quantity=1)
    its_id = default_course[0].id
    url = reverse("courses-list")
    resp = my_api_client.patch(url + f"{its_id}/", {"name": "patched"})
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json.get('name') == "patched"


@pytest.mark.django_db
def test_course_delete(my_api_client, course_factory):
    default_course = course_factory(_quantity=1)
    its_id = default_course[0].id
    url = reverse("courses-list")
    resp = my_api_client.delete(url + f"{its_id}/")
    assert resp.status_code == HTTP_204_NO_CONTENT
