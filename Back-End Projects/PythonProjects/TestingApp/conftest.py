import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_3(db):
    user = User.objects.create_user('xv-user')
    print('create-user')
    return user
