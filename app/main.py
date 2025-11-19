from fastapi import FastAPI
from app.models import Healthcheck
from app.routers import rate_router

app = FastAPI(
    title="BCV Exchange Rates",
    version="0.1.0",
    summary="API for querying daily and historical BCV Exchanges Rates",
    swagger_ui_parameters={"docExpansion": "none"},
)

app.include_router(rate_router)


@app.get("/health", tags=["Healthcheck"], response_model=Healthcheck, status_code=200)
async def health() -> Healthcheck:
    return Healthcheck()
