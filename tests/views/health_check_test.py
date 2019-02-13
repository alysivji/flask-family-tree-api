def test_health_check(client):
    rv = client.get("/api/health_check")
    assert rv.status_code == 200
    assert rv.json is True
