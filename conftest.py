from datetime import datetime, timedelta, timezone
import jwt
import pytest
from fastapi.testclient import TestClient
import typing as t
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from app.main import app

public_certificate_content = None
private_certificate_content = None

with open('public_key.pem', 'r') as file:
        public_certificate_content = file.read()
        
with open('private_key.pem', 'r') as file:
        private_certificate_content = file.read()
        


@pytest.fixture
def client():
    """
    Get a TestClient instance that reads/write to the test database.
    """

    yield TestClient(app)

@pytest.fixture
def mock_requests_get(mocker):
    mock_get = mocker.patch("requests.get")
    
    yield mock_get
    

@pytest.fixture
def mock_public_key():
    return public_certificate_content


@pytest.fixture
def mock_jwt_token():
    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": int((datetime.now(timezone.utc) - timedelta(hours=1)).timestamp()),
        "exp": int((datetime.now(timezone.utc) + timedelta(hours=1)).timestamp())
    }

    certificate = load_pem_private_key(private_certificate_content.encode(), '123456'.encode())

    signed_token = jwt.encode(payload, certificate, algorithm="RS256", headers={
                              "x5u": "https://example.com/cert.pem"})
    
    return signed_token
