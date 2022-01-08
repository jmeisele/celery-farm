from .celery import app

@app.task
def hello():
    return "Hello world"

@app.task
def reverse(text):
    return text[::-1]

