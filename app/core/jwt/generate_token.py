from datetime import datetime, timedelta, timezone
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import jwt


def generate_token():

    with open('private_key.pem', 'r') as file:
        private_certificate_content = file.read()

    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": int((datetime.now(timezone.utc) - timedelta(hours=1)).timestamp()),
        "exp": int((datetime.now(timezone.utc) + timedelta(hours=1)).timestamp())
    }

    certificate = load_pem_private_key(private_certificate_content.encode(), '123456'.encode())

    signed_token = jwt.encode(payload, certificate, algorithm="RS256", headers={
                              "x5u": "invalid-url"})
    
    return signed_token