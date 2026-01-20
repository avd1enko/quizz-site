from fastapi import APIRouter, HTTPException
from starlette import status

from app.db.engine import check_db

router = APIRouter(tags=["Health"])

@router.get("/health")
def health() -> dict:
    return {"status": "ok"}

@router.get("/health/db")
def health_db() -> dict:
    try:
        check_db()
        return {"status": "oky"}
    except Exception:
        raise HTTPException(status_code=500, detail="Database connection error")
