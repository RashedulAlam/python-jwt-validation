from fastapi import APIRouter

jwt_validation_router = r = APIRouter()


@r.get(
    "/v1/check-jwt-validity"
)
async def check_jwt_validity():
    """
    validates jwt token. \n
    returns valid when token is valid. \n
    returns invalid and resson when token is invalid.
    """

    return {}