from celery import Celery
from celery_config import settings

app = Celery("workers", broker=settings.BROKER_URL, include=['workers.tasks'])

if __name__  == '__main__':
    app.start()