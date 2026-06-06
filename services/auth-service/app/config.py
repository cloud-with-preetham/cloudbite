from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CloudBite Auth Service"
    app_version: str = "1.0.0"
    environment: str = "development"

    database_url: str = "postgresql://cloudbite:cloudbite@postgres:5432/cloudbite_auth"

    jwt_secret_key: str = "change-this-secret-key"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
