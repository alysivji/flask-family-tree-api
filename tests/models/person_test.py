from family_tree.models import Person


def test_create_person(session):
    new_user = Person(first_name="test", last_name="user", email="test@user.com")

    session.add(new_user)
    session.commit()

    assert new_user.id is not None
