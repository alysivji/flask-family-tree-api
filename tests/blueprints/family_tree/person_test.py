def test_create_person(client, session):
    test_person = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@user.com",
    }

    rv = client.post("/api/person", json=test_person)
    result = rv.json["data"]

    assert rv.status_code == 201
    assert result["id"] == 1
