from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def auth_root():
    return {
        "service": "auth-service",
        "message": "Auth API is running",
    }
