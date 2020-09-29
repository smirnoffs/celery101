from fastapi import FastAPI
from pydantic import BaseModel
from tasks import send_confirmation

app = FastAPI()


class SubscribeRequest(BaseModel):
    name: str
    email: str


@app.post("/subscribe")
async def subscribe(request: SubscribeRequest):
    send_confirmation.delay(name=request.name, email=request.email)
    return {"name": request.name, "email": request.email, "subscribe": True}
