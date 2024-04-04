from password_manager_gui.backend.server import app
from fastapi.testclient import TestClient
import pytest


# having a fixture to create a 'client' factory for all of the tests to use
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
