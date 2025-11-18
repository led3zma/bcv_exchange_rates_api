from fastapi import FastAPI
from app.routers import rate_router

app = FastAPI()

app.include_router(rate_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
