from motor.motor_asyncio import AsyncIOMotorClient

from .config import DatabaseSettings

mongodb_client = AsyncIOMotorClient(DatabaseSettings.DB_URL)
mongodb = mongodb_client[DatabaseSettings.DB_NAME]
