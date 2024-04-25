from fastapi import FastAPI
from starlette.requests import Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.routers.check_jwt_validity import jwt_validation_router

app = FastAPI(
    title="Python JWT Validation", docs_url="/api/docs", openapi_url="/api"
)

app.include_router(jwt_validation_router, prefix="/api", tags=["jwt-validation"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload = True)
