from celery import Celery

from .config import settings

celery_app = Celery(
    "workers",
    broker=settings.BROKER_URL,
    include=["workers.tasks"],
    backend=settings.BACKEND_URL,
)
