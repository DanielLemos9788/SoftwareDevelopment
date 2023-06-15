

def test_create_new_user(new_user):
    print(new_user.first_name)
    assert new_user.first_name == 'MyName'


def test_create_new_staff_user(new_staff_user):
    print(new_staff_user.first_name)
    assert new_staff_user.first_name == 'Perkins'

