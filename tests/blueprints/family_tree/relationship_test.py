# from urllib.parse import urlparse
import uuid

import pytest


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


def test_create_child_relationship_type(client, session, create_person):
    parent_id = create_person()
    child_id = create_person()

    new_relationship = {
        "relation_type": "child",
        "person_id_for_relation_type": child_id,
    }
    rv = client.post(f"/api/person/{parent_id}/relationship", json=new_relationship)
    assert rv.status_code == 201
    # assert rv.json["data"]["id"] == 1

    rv = client.get(f"/api/person/{parent_id}")
    assert child_id in rv.json["data"]["children"]
    rv = client.get(f"/api/person/{child_id}")
    assert parent_id in rv.json["data"]["parents"]


def test_create_parent_relationship_type(client, session, create_person):
    parent_id = create_person()
    child_id = create_person()

    new_relationship = {
        "relation_type": "parent",
        "person_id_for_relation_type": parent_id,
    }
    rv = client.post(f"/api/person/{child_id}/relationship", json=new_relationship)
    assert rv.status_code == 201
    # assert rv.json["data"]["id"] == 1

    rv = client.get(f"/api/person/{parent_id}")
    assert child_id in rv.json["data"]["children"]
    rv = client.get(f"/api/person/{child_id}")
    assert parent_id in rv.json["data"]["parents"]
