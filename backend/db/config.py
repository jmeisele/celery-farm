import os

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    DB_URL: str = os.environ["DB_URL"]
    DB_NAME: str = os.environ["DB_NAME"]


db_settings = DatabaseSettings()
