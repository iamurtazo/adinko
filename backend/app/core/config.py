from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """Application configuration settings."""
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/adinko_db"
    )
    
    # Server
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AidKo - Community Q&A Platform"
    
    # JWT
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "your-super-secret-key-change-in-production"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8000",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
