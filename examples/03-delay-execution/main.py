from fastapi import FastAPI
from pydantic import BaseModel
from tasks import send_confirmation, send_greetings

app = FastAPI()


class SubscribeRequest(BaseModel):
    name: str
    email: str


@app.post("/subscribe")
async def subscribe(request: SubscribeRequest):
    send_confirmation.delay(name=request.name, email=request.email)
    # https://docs.celeryproject.org/en/stable/userguide/canvas.html#signatures
    # A signature() wraps the arguments, keyword arguments, and execution options.
    # It can be passed to the other process or function or call it as a task.
    # It's a Celety analogue of Python partial.
    send_greetings.signature(
        kwargs={"name": request.name, "email": request.email}, countdown=10
    ).apply_async()
    return {"name": request.name, "email": request.email, "subscribe": True}
