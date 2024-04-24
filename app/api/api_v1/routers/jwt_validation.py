from fastapi import APIRouter

validate_jwt_router = r = APIRouter()


@r.put(
    "/v1/validate-jwt"
)
async def validate_jwt():
    """
    validates jwt token
    """

    return {}