from fastapi import FastAPI
from pydantic import BaseModel
from tasks import send_confirmation, send_greetings

app = FastAPI()


class SubscribeRequest(BaseModel):
    name: str
    email: str


@app.post("/subscribe")
async def subscribe(request: SubscribeRequest):
    # First create a signiture for the task
    greetings = send_greetings.s({"name": request.name, "email": request.email})
    # https://docs.celeryproject.org/en/stable/userguide/canvas.html#callbacks
    # Then pass the signiture as the link to the apply_async keyword argument.
    send_confirmation.apply_async(
        None, {"name": request.name, "email": request.email}, link=greetings
    )
    return {"name": request.name, "email": request.email, "subscribe": True}
