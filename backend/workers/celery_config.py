import os
from pydantic import BaseSettings

class CelerySettings(BaseSettings):
    BROKER_URL: str = os.environ["BROKER_URL"]

class Settings(CelerySettings):
    pass

settings = Settings()