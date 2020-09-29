from celery import Celery
import random
import time

app = Celery("tasks", broker="redis://localhost:6379/0")


@app.task
def send_confirmation(name, email):
    time.sleep(random.randint(1, 50) / 10)
    print(f"{name} <{email}> subscribed")


@app.task
def send_greetings(name, email):
    time.sleep(random.randint(1, 50) / 10)
    print(f"{name} <{email}> is greeted")