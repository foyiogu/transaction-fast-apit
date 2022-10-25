from fastapi import FastAPI, HTTPException

from .models import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/api/v1/transactions")
async def post_transactions(user: User):
    if user.id == 1:
        raise HTTPException(status_code=400, detail="User with this id already exists")
    return {"message": " Hello World"}
