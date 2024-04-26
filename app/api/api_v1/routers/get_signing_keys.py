from fastapi import APIRouter

jwt_signing_keys_router = r = APIRouter()


@r.get(
    "/v1/signing-keys/cert"
)
async def get_jwt_token():
    """Gets the public key for JWT verification.

    Returns:
        returns the signing keys.
    """
    
    with open('public_key.pem', 'r') as file:
        public_certificate_content = file.read()

    return public_certificate_content
