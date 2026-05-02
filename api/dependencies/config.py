import os

class Settings:
    PROJECT_NAME: str = "Online Restaurant Ordering System"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./restaurant.db")

settings = Settings()