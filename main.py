from fastapi import FastAPI
from routers import event

app = FastAPI()

app.include_router(event.router)

@app.get("/")
def home():
    return {"message": "Welcome to Campus API"}
