from .main import app
from time import sleep

@app.task
def hello():
    return "Hello world"

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]

