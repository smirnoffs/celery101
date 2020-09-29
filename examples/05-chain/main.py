from fastapi import FastAPI
from pydantic import BaseModel
from tasks import send_confirmation, send_greetings
from celery import chain

app = FastAPI()


class SubscribeRequest(BaseModel):
    name: str
    email: str


@app.post("/subscribe")
async def subscribe(request: SubscribeRequest):
    # Here’s a simple chain, the first task executes passing its
    # return value to the next task in the chain, and so on.
    confirmation = send_confirmation.s(request.name, request.email)
    greetings = send_greetings.s()
    # https://docs.celeryproject.org/en/v4.4.7/userguide/canvas.html#the-primitives
    # The result of the first task will be passed as a first argument of the second.
    ch = chain(confirmation, greetings)()
    return {"name": request.name, "email": request.email, "subscribe": True}
