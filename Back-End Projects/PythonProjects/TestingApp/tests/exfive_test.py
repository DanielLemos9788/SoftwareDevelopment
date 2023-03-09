import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_two(db):
    user = User.objects.create_user('xv-user')
    return user


def test_set_check_username(user_two):
    assert user_two.username == 'xv-user'

