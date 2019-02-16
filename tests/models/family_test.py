from family_tree.models import Person, Family


def test_create_family(session):
    new_user = Person(first_name="test", last_name="user", email="test@user.com")
    new_family = Family(name="Test", head_of_family=new_user)

    session.add(new_user)
    session.add(new_family)
    session.commit()

    assert new_user.id is not None
    assert new_family.name == "Test"
    assert new_family.head_of_family.id == new_user.id
