import pytest
from fastapi.testclient import TestClient
import typing as t
from app.main import app

@pytest.fixture
def client():
    """
    Get a TestClient instance that reads/write to the test database.
    """

    yield TestClient(app)
