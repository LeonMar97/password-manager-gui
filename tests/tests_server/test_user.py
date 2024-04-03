from password_manager_gui.backend.server import app
from fastapi.testclient import TestClient


# using with for testclient for lifespan generator to create the local db
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.text == "pong"


def test_add():
    with TestClient(app) as client:
        response = client.post("/api/v1/add-user", json={"user_name": "leonm", "password": "1234"})
        assert response.status_code == 201


def test_same_user_name():
    with TestClient(app) as client:
        response = client.post("/api/v1/add-user", json={"user_name": "leon", "password": "1234"})
        assert response.status_code == 409
