from typing import Callable

import redis
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import api_settings


def _startup_mongodb_client(app: FastAPI) -> None:
    app.mongodb_client = AsyncIOMotorClient(api_settings.DB_URL)
    app.mongodb = app.mongodb_client[api_settings.DB_NAME]


def _startup_redis_client(app: FastAPI) -> None:
    app.redis_client = redis.Redis(host=api_settings.REDIS_URL, port=6379, db=0)


def _shutdown_mongodb_client(app: FastAPI) -> None:
    app.mongodb_client.close()


def _shutdown_redis_client(app: FastAPI) -> None:
    app.redis_client = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        _startup_mongodb_client(app)
        _startup_redis_client(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_mongodb_client(app)
        _shutdown_redis_client(app)

    return shutdown
