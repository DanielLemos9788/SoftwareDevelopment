

def test_check_username(user_3):
    print('check-user')
    assert user_3.username == 'xv-user'


def test_check_username2(user_3):
    print('check-user2')
    assert user_3.username == 'xv-user'


def test_check_is_staff(new_staff_user):
    print(new_staff_user.is_staff)
    assert new_staff_user.is_staff == 'True'
