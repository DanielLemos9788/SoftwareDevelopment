import pytest
from django.contrib.auth.models import User

# function: runs once per test
# class: runs once per class of tests
# module: runs once per module
# module: runs once per session

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'xvxtest@gmail.com', 'testify')
    count = User.objects.all().count()
    print(count)
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_create_count():
    count = User.objects.all().count()
    assert count == 0

