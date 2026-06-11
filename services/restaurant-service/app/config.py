from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CloudBite Restaurant Service"

    database_url: str = (
        "postgresql://cloudbite:cloudbite@restaurant-postgres:5432/cloudbite_restaurant"
    )

    class Config:
        env_file = ".env"


settings = Settings()
