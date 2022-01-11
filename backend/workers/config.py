import os

from pydantic import BaseSettings

class CelerySettings(BaseSettings):
    BROKER_URL: str = os.environ["BROKER_URL"]
    BACKEND_URL: str = os.environ["BACKEND_URL"]

settings = CelerySettings()