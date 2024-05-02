from fastapi import APIRouter, Request
from app.core.jwt.generate_token import generate_token, generate_invalid_cert_token, generate_expired_token, generate_invalid_header_token, generate_invalid_payload_at_token, generate_invalid_payload_exp_token

jwt_token_router = r = APIRouter()


@r.get(
    "/v1/get-token"
)
async def get_jwt_token(request: Request):
    """Gets sample jwt for debug.

    Returns:
        Generated JWT token.
    """
    request_url = request.url

    return {"token": generate_token(request_url)}


@r.get(
    "/v1/get-expired-token"
)
async def get_expired_jwt_token(request: Request):
    """Gets sample expired jwt for debug.

    Returns:
        Generated JWT token.
    """
    request_url = request.url

    return {"token": generate_expired_token(request_url)}


@r.get(
    "/v1/get-invalid-cert-token"
)
async def get_invalid_cert_jwt_token(request: Request):
    """Gets sample jwt for invalid certificate token for debug.

    Returns:
        Generated JWT token.
    """
    request_url = request.url

    return {"token": generate_invalid_cert_token(request_url)}


@r.get(
    "/v1/get-invalid-header-token"
)
async def get_invalid_header_jwt_token(request: Request):
    """Gets sample jwt for invalid header token for debug.

    Returns:
        Generated JWT token.
    """
    request_url = request.url

    return {"token": generate_invalid_header_token(request_url)}


@r.get(
    "/v1/get-invalid-at-payload-token"
)
async def get_invalid_at_payload_jwt_token(request: Request):
    """Gets sample jwt for invalid payload token for debug.

    Returns:
        Generated JWT token.
    """
    request_url = request.url

    return {"token": generate_invalid_payload_at_token(request_url)}

@r.get(
    "/v1/get-invalid-exp-payload-token"
)
async def get_invalid_exp_payload_jwt_token(request: Request):
    """Gets sample jwt for invalid payload token for debug.

    Returns:
        Generated JWT token.
    """
    request_url = request.url

    return {"token": generate_invalid_payload_exp_token(request_url)}
