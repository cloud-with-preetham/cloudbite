from fastapi import FastAPI
from app.config import settings
from app.routes import router


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


app.include_router(router, prefix="/api/v1/auth", tags=["auth"])
