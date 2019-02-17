from urllib.parse import urlparse


def test_get_list_of_people(client, session):
    for i in range(5):
        test_person = {
            "first_name": "Test",
            "last_name": "User",
            "email": f"test{i}@user.com",
        }
        client.post("/api/person", json=test_person)

    rv = client.get("/api/person")

    assert rv.status_code == 200
    assert len(rv.json["data"]) == 5


def test_create_person(client, session):
    test_person = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@user.com",
    }

    rv = client.post("/api/person", json=test_person)

    assert rv.status_code == 201
    assert rv.json["data"]["id"] == 1
    headers = rv.headers
    assert "Location" in headers
    assert "/api/person/1" in headers["Location"]


def test_get_person(client, session):
    test_person = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@user.com",
    }
    rv = client.post("/api/person", json=test_person)
    loc = rv.headers["Location"]
    path = urlparse(loc).path

    rv = client.get(path)

    assert rv.status_code == 200
    result = rv.json["data"]
    for k, v in test_person.items():
        assert result[k] == v


def test_get_person_not_found(client, session):
    rv = client.get("/api/person/1",)

    assert rv.status_code == 404
    assert "Person not found" in rv.json["error"]["msg"]
