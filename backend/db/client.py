from motor.motor_asyncio import AsyncIOMotorClient

from .config import db_settings

mongodb_client = AsyncIOMotorClient(db_settings.DB_URL)
mongodb = mongodb_client[db_settings.DB_NAME]
