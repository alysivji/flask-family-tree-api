from urllib.parse import urlparse
import pytest

# TODO could write more fixtures to build out testing tools (i.e. test user json),
# but being pragmtic. It's not worth the time required at the moment


def test_get_list_of_people(client, session):
    for i in range(5):
        test_person = {
            "first_name": "Test",
            "last_name": "User",
            "email": f"test{i}@user.com",
        }
        client.post("/api/v1/person", json=test_person)

    rv = client.get("/api/v1/person")

    assert rv.status_code == 200
    assert len(rv.json["data"]) == 5


def test_create_person(client, session):
    test_person = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@user.com",
    }

    rv = client.post("/api/v1/person", json=test_person)

    assert rv.status_code == 201
    assert rv.json["data"]["id"] == 1
    headers = rv.headers
    assert "Location" in headers
    assert "/api/v1/person/1" in headers["Location"]


def test_get_person(client, session):
    test_person = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@user.com",
    }
    rv = client.post("/api/v1/person", json=test_person)
    loc = rv.headers["Location"]
    path = urlparse(loc).path

    rv = client.get(path)

    assert rv.status_code == 200
    result = rv.json["data"]
    for k, v in test_person.items():
        assert result[k] == v


def test_post_person(client, session):
    test_person = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@user.com",
    }
    rv = client.post("/api/v1/person", json=test_person)
    loc = rv.headers["Location"]
    path = urlparse(loc).path

    updated_test_person = dict(test_person)
    updated_test_person["first_name"] = "Updated Test"
    rv = client.put(path, json=updated_test_person)
    assert rv.status_code == 200

    # confirm record is updated
    rv = client.get(path)
    assert rv.status_code == 200
    result = rv.json["data"]
    for k, v in updated_test_person.items():
        assert result[k] == v


def test_delete_person(client, session):
    test_person = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@user.com",
    }
    rv = client.post("/api/v1/person", json=test_person)
    loc = rv.headers["Location"]
    path = urlparse(loc).path

    rv = client.delete(path)
    assert rv.status_code == 200

    # confirm deletion
    rv = client.get(path)
    assert rv.status_code == 404


@pytest.mark.parametrize("http_method", ["get", "put", "delete"])
def test_person_not_found(client, session, http_method):
    test_client_dot_http_method = getattr(client, http_method)

    rv = test_client_dot_http_method("/api/v1/person/1",)

    assert rv.status_code == 404
    assert "Person not found" in rv.json["error"]["msg"]
