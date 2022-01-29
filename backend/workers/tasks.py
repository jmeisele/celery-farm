from time import sleep

from .main import celery_app


@celery_app.task
def reverse(text):
    sleep(5)
    return text[::-1]
