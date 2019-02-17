from typing import NamedTuple
import uuid
import pytest


class RelationshipDetails(NamedTuple):
    from_person_id: int
    to_person_id: int
    type: str


@pytest.fixture
def create_person(client, session):
    def _create_person():
        new_person = {
            "first_name": "Test",
            "last_name": "User",
            "email": str(uuid.uuid4()),
        }
        rv = client.post("/api/person", json=new_person)
        assert rv.status_code == 201

        return rv.json["data"]["id"]

    return _create_person


@pytest.fixture
def create_relationship(client, session):
    def _create_relationship(*, from_id, to_id, rel_type):
        rel = {"relation_type": rel_type, "person_id_for_relation_type": to_id}
        rv = client.post(f"/api/person/{from_id}/relationship", json=rel)
        assert rv.status_code == 201
        return RelationshipDetails(from_id, to_id, rel_type)

    return _create_relationship


def test_create_child_relationship_type(client, session, create_person):
    # Arrange
    parent_id = create_person()
    child_id = create_person()

    # Act
    new_relationship = {
        "relation_type": "child",
        "person_id_for_relation_type": child_id,
    }
    rv = client.post(f"/api/person/{parent_id}/relationship", json=new_relationship)

    # Assert
    assert rv.status_code == 201

    rv = client.get(f"/api/person/{parent_id}")
    assert child_id in rv.json["data"]["children"]

    rv = client.get(f"/api/person/{child_id}")
    assert parent_id in rv.json["data"]["parents"]


def test_create_parent_relationship_type(client, session, create_person):
    # Arrange
    parent_id = create_person()
    child_id = create_person()

    # Act
    new_relationship = {
        "relation_type": "parent",
        "person_id_for_relation_type": parent_id,
    }
    rv = client.post(f"/api/person/{child_id}/relationship", json=new_relationship)

    # Assert
    assert rv.status_code == 201

    rv = client.get(f"/api/person/{parent_id}")
    assert rv.status_code == 200
    assert child_id in rv.json["data"]["children"]

    rv = client.get(f"/api/person/{child_id}")
    assert rv.status_code == 200
    assert parent_id in rv.json["data"]["parents"]


def test_delete_child_relationship_type(
    client, session, create_person, create_relationship
):
    # Arrange
    parent_id = create_person()
    child_id = create_person()
    create_relationship(from_id=parent_id, to_id=child_id, rel_type="child")

    # Act
    rel_to_delete = {
        "relation_type": "child",
        "person_id_for_relation_type": child_id,
    }
    rv = client.delete(f"/api/person/{parent_id}/relationship", json=rel_to_delete)

    # Assert
    assert rv.status_code == 200

    rv = client.get(f"/api/person/{parent_id}")
    assert rv.status_code == 200
    assert child_id not in rv.json["data"]["children"]

    rv = client.get(f"/api/person/{child_id}")
    assert rv.status_code == 200
    assert parent_id not in rv.json["data"]["parents"]


def test_delete_parent_relationship_type(
    client, session, create_person, create_relationship
):
    # Arrange
    parent_id = create_person()
    child_id = create_person()
    create_relationship(from_id=parent_id, to_id=child_id, rel_type="child")

    # Act
    rel_to_delete = {
        "relation_type": "parent",
        "person_id_for_relation_type": parent_id,
    }
    rv = client.delete(f"/api/person/{child_id}/relationship", json=rel_to_delete)

    # Assert
    assert rv.status_code == 200

    rv = client.get(f"/api/person/{parent_id}")
    assert rv.status_code == 200
    assert child_id not in rv.json["data"]["children"]

    rv = client.get(f"/api/person/{child_id}")
    assert rv.status_code == 200
    assert parent_id not in rv.json["data"]["parents"]
