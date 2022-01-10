from .main import celery_app
from time import sleep

@celery_app.task
def hello():
    return "Hello world"

@celery_app.task
def reverse(text):
    sleep(5)
    return text[::-1]

