from celery import Celery, group
import random
import time

app = Celery("tasks", broker="redis://localhost:6379/0")


@app.task
def subscribe_user(name, email):
    res = group(
        send_confirmation.s(name=name, email=email),
        send_greetings.s(name=name, email=email),
    )()
    results = res.get()
    print("RESULTS OF SUBSCRIPTION:", results)


@app.task
def send_confirmation(name, email):
    time.sleep(random.randint(1, 50) / 10)
    print(f"{name} <{email}> subscribed")
    return {"success": True}


@app.task
def send_greetings(name, email):
    time.sleep(random.randint(1, 50) / 10)
    print(f"{name} <{email}> is greeted")
    return {"success": True}