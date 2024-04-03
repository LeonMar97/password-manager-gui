from password_manager_gui.backend.server import app
from fastapi.testclient import TestClient


def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.text == "pong"
