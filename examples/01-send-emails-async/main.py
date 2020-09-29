from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import random

app = FastAPI()


class SubscribeRequest(BaseModel):
    name: str
    email: str


@app.post("/subscribe")
async def subscribe(request: SubscribeRequest):
    # Here is a call to the SMTP or email provider API
    # which has a response time between 100ms and 5s.
    await asyncio.sleep(random.randint(1, 50) / 10)
    return {"name": request.name, "email": request.email, "subscribe": True}
