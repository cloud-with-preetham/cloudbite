from fastapi import FastAPI
from sqlalchemy import text

from app.config import settings
from app.database import Base, SessionLocal, engine
from app.routes import router
from app import models


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Authentication service for the CloudBite food delivery platform.",
)


@app.get("/health")
def health_check():
    return {
        "service": "auth-service",
        "status": "healthy",
        "environment": settings.environment,
    }


@app.get("/health/db")
def database_health_check():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
        return {
            "service": "auth-service",
            "database": "postgresql",
            "status": "connected",
        }
    finally:
        db.close()


app.include_router(router, prefix="/api/v1/auth", tags=["auth"])
