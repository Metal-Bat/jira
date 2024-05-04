from app.users.models import User


def test_user_get_full_name(user: User):
    assert user.get_full_name() == str(user.first_name) + " " + str(user.last_name)
