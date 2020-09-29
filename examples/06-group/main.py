from fastapi import FastAPI
from pydantic import BaseModel
from tasks import subscribe_user


app = FastAPI()


class SubscribeRequest(BaseModel):
    name: str
    email: str


@app.post("/subscribe")
async def subscribe(request: SubscribeRequest):
    subscribe_user.delay(request.name, request.email)
    return {"name": request.name, "email": request.email, "subscribe": True}
