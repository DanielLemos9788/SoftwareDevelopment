import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_one(db):
    return User.objects.create_user('test-user')


@pytest.mark.django_db
def test_set_check_password(user_one):
    user_one.set_password('new')
    assert user_one.check_password('new') is True

