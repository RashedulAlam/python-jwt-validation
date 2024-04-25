from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from app.core.jwt.verify_jwt import verify_jwt

jwt_validation_router = r = APIRouter()
security = HTTPBearer(auto_error=False)

@r.get(
    "/v1/check-jwt-validity"
)
async def check_jwt_validity(authorization_header: str | None = Depends(security)):
    """checks jwt token validity from request header.

    Returns:
        Whether token is valid or not and reason.
    """

    if authorization_header is None:
        return {"valid": False, "reason": "Invalid request header."}

    is_valid, reason = verify_jwt(authorization_header)

    if is_valid is True:
        return {"valid": True}

    return {"valid": is_valid, "reason": reason}


optional_oauth2_scheme = HTTPBearer()

@r.get(
    "/v2/check-jwt-validity"
)
async def check_jwt_validity(authorization_header: str | None = Depends(security)):
    """checks jwt token validity from request header.

    Returns:
        Whether token is valid or not and reason.
    """

    if authorization_header is None:
        return {"valid": False, "reason": "Invalid request header."}

    is_valid, reason = verify_jwt(authorization_header, True)

    if is_valid is True:
        return {"valid": True}

    return {"valid": is_valid, reason: reason}
