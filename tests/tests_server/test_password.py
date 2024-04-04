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


def test_add_password_should_add(client):
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
    assert response.json() == {"message": "password added successfully"}


def test_add_password_should_fail_differnt_user(client):
    """should fail for more than one user now, as i didnt implement multiple user save.."""
    client.post("/api/v1/add-user", json={"user_name": "test_user", "password": "1234"})
    pass_json = {
        "usr": {"user_name": "test_user", "password": "1234"},
        "pas": {
            "website_user_name": "test",
            "website_password": "123548468768/76/89787887897897898989897",
            "website_url": "test@website",
        },
    }
    response = client.post("/api/v1/add-password", json=pass_json)
    assert response.status_code == 500


def test_add_password_should_fail_not_user(client):
    """should fail for non existing user.."""
    pass_json = {
        "usr": {"user_name": "test_user_3", "password": "1234"},
        "pas": {
            "website_user_name": "test",
            "website_password": "123548468768/76/89787887897897898989897",
            "website_url": "test@website",
        },
    }
    response = client.post("/api/v1/add-password", json=pass_json)
    assert response.status_code == 401


def test_decrypt_password_should_decrypt(client):
    usr_json = {"user_name": "leonm", "password": "1234"}
    response = client.post("/api/v1/decrypt-passwords", json=usr_json)
    assert response.status_code == 200


def test_decrypt_password_should_fail(client):
    """should fail for wrong password (used the default user)"""
    usr_json = {"user_name": "leonm", "password": "12345"}
    response = client.post("/api/v1/decrypt-passwords", json=usr_json)
    assert response.status_code == 401


def test_decrypt_password_should_fail_differnt_user(client):
    """should fail for more than one user now, as i didnt implement multiple user save.."""
    client.post("/api/v1/add-user", json={"user_name": "test_user", "password": "1234"})
    usr_json = {"user_name": "test_user", "password": "1234"}
    response = client.post("/api/v1/decrypt-passwords", json=usr_json)
    assert response.status_code == 500


def test_decrypt_password_should_fail_non_existing(client):
    """should fail for non existing user"""
    usr_json = {"user_name": "test_user_2", "password": "1234"}
    response = client.post("/api/v1/decrypt-passwords", json=usr_json)
    assert response.status_code == 401
