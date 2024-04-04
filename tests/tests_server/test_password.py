def test_ping_endpoint_returns_pong(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "pong"


def test_add_password_should_fail(client):
    pass_json = {
        "usr": {"user_name": "leonm", "password": "123456"},
        "pas": {
            "website_user_name": "test",
            "website_password": "123548468768/76/89787887897897898989897",
            "website_url": "test@website",
        },
    }
    response = client.post("/api/v1/add-password", json=pass_json)
    assert response.status_code == 401
    assert response.json() == {"detail": "password for user leonm is incorect"}


def test_add_password_should_apply(client):
    pass_json = {
        "usr": {"user_name": "leonm", "password": "1234"},
        "pas": {
            "website_user_name": "test",
            "website_password": "123548468768/76/89787887897897898989897",
            "website_url": "test@website",
        },
    }
    response = client.post("/api/v1/add-password", json=pass_json)
    assert response.status_code == 201
    # assert response.json() == {"detail": "password for user leonm is incorect"}
