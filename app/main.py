from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.routers.check_jwt_validity import jwt_validation_router
from app.api.api_v1.routers.get_token import jwt_token_router

app = FastAPI(
    title="Python JWT Validation", docs_url="/api/docs", openapi_url="/api"
)

app.include_router(jwt_validation_router, prefix="/api", tags=["jwt-validation"])
app.include_router(jwt_token_router, prefix="/api", tags=["jwt-token"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload = True)
