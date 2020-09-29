from celery import Celery
import random
import time

app = Celery("tasks", broker="redis://localhost:6379/0")


@app.task
def send_confirmation(name, email):
    time.sleep(random.randint(1, 50) / 10)
    print(f"{name} <{email}> subscribed")
    return {"name": name, "email": email}


@app.task
def send_greetings(parent_result):
    time.sleep(random.randint(1, 50) / 10)
    print(f"{parent_result['name']} <{parent_result['email']}> is greeted")