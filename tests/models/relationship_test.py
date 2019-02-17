import uuid
import pytest
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


@pytest.fixture
def create_person(session):
    def _create_person():
        p = Person(first_name="Test", last_name="User", email=str(uuid.uuid4()))
        session.add(p)
        session.commit()
        return p

    return _create_person


def test_family_tree(session, create_person):
    child1 = create_person()
    child1_child1 = create_person()
    child1_child2 = create_person()
    child1.children.extend([child1_child1, child1_child2])

    child3 = create_person()
    child3_child1 = create_person()
    child3_child2 = create_person()
    child3_child3 = create_person()
    child3.children.extend([child3_child1, child3_child2, child3_child3])

    head_of_family = create_person()
    child2 = create_person()
    head_of_family.children.extend([child1, child2, child3])

    assert head_of_family.grandchildren == [
        child1_child1,
        child1_child2,
        child3_child1,
        child3_child2,
        child3_child3,
    ]
