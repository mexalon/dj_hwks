import pytest
from rest_framework.test import APIClient
from model_bakery import baker



@pytest.fixture
def my_api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make('Course', **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make('Students', **kwargs)
    return factory
