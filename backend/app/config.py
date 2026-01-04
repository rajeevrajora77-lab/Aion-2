from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"
    PROJECT_NAME: str = "AION"
    API_VERSION: str = "v1"

    class Config:
        env_file = ".env"

settings = Settings()
