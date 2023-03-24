from fastapi import FastAPI
from pydantic import BaseModel

class RequestBody(BaseModel):
    name: str

app = FastAPI()

@app.post("/hello")
async def hello(requestBody: RequestBody):
    name = requestBody.name
    return {"message": "Hello {}".format(name)}
