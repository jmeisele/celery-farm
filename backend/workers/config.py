import os
from pydantic import BaseSettings

class CelerySettings(BaseSettings):
    # BROKER_URL: str = os.environ["BROKER_URL"]
    # BACKEND_URL: str = os.environ["BACKEND_URL"]
    BROKER_URL: str = 'redis://localhost:6379/0'
    BACKEND_URL: str = 'redis://localhost:6379/0'

class Settings(CelerySettings):
    pass

settings = Settings()