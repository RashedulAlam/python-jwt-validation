from fastapi import APIRouter
from app.core.jwt.generate_token import generate_token

jwt_token_router = r = APIRouter()


@r.get(
    "/v1/get-token"
)
async def get_jwt_token():
    """Gets sample jwt for debug.

    Returns:
        Generated JWT token.
    """

    return {"token": generate_token()}
