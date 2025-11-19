from fastapi import FastAPI
from app.routers import rate_router

app = FastAPI()

app.include_router(rate_router)


@app.get("/health", tags=["Healthcheck"], response_model=Healthcheck, status_code=200)
async def health() -> Healthcheck:
    return Healthcheck()
