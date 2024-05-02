from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api.api_v1.routers.get_token import jwt_token_router
from app.api.api_v1.routers.get_signing_keys import jwt_signing_keys_router

load_dotenv()

app = FastAPI(
    title="Python JWT Validation", docs_url="/api/docs", openapi_url="/api"
)

app.include_router(jwt_token_router, prefix="/api", tags=["jwt-token"])
app.include_router(jwt_signing_keys_router, prefix="/api", tags=["jwt-signing-keys"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload = True)
