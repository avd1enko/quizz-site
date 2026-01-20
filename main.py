from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings  # noqa: F401
from app.api.v1.router import health_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
@app.get("/health_check")
async def health_check():
    return {"status": "okay"}