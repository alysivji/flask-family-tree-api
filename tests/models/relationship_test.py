from family_tree.models import Person, Progeny


def test_create_progeny_relationship(session):
    parent = Person(first_name="parent", last_name="user", email="parent@user.com")
    child = Person(first_name="child", last_name="user", email="child@user.com")
    parent.children.append(child)

    session.add(parent)
    session.add(child)
    session.commit()

    assert parent in child.parents


def test_delete_progeny_relationship_when_deleting_person(session):
    """Checking DELETE ON CASCADE functionality"""
    parent = Person(first_name="parent", last_name="user", email="parent@user.com")
    child = Person(first_name="child", last_name="user", email="child@user.com")
    parent.children.append(child)

    session.add(parent)
    session.add(child)
    session.commit()
    assert parent in child.parents

    session.delete(parent)
    assert len(Progeny.query.all()) == 0
