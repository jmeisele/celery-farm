import os
from pydantic import BaseSettings

class CommonSettings(BaseSettings):
    APP_NAME: str = "Celery FaRM"
    DEBUG_MODE: bool = False
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/task"

class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000

class DatabaseSettings(BaseSettings):
    DB_URL: str = os.environ["DB_URL"]
    DB_NAME: str = os.environ["DB_NAME"]

class RedisSettings(BaseSettings):
    REDIS_URL: str = os.environ["REDIS_URL"]

class Settings(CommonSettings, ServerSettings, DatabaseSettings, RedisSettings):
    pass

api_settings = Settings()