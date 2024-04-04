def test_ping_endpoint_returns_pong(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "pong"


def test_add_user_creates_new_user(client):
    response = client.post("/api/v1/add-user", json={"user_name": "test_user", "password": "1234"})
    assert response.status_code == 201


def test_add_user_fails_on_duplicate_username(client):
    response = client.post("/api/v1/add-user", json={"user_name": "leonm", "password": "1234"})
    assert response.status_code == 409
