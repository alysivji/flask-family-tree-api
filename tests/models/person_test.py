from family_tree.models import User


def test_create_user(session):
    new_user = User(name="test user", email="test@user.com")

    session.add(new_user)
    session.commit()

    assert new_user.id is not None
