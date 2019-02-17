def test_get_list_of_people(client, session):
    for i in range(5):
        test_person = {
            "first_name": "Test",
            "last_name": "User",
            "email": f"test{i}@user.com",
        }
        client.post("/api/person", json=test_person)

    rv = client.get("/api/person")

    result = rv.json["data"]
    assert rv.status_code == 200
    assert len(result) == 5


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
