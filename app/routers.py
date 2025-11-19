from datetime import date
from fastapi import APIRouter, HTTPException, status

from app.core.db import SessionDep
from app.models import RatePublic
from app.crud import get_rate_by_date, get_rate_from_to_date

rate_router = APIRouter(prefix="/rate")


@rate_router.get("/", response_model=RatePublic)
async def get_rate(session: SessionDep, value_date: date | None = None) -> RatePublic:
    if not value_date:
        value_date = date.today()
    rate = get_rate_by_date(session, value_date)
    if not rate:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rate not found"
        )
    return rate


@rate_router.get("/historical", response_model=list[RatePublic])
async def get_historical_rate(
    session: SessionDep, from_date: date, to_date: date | None = None
) -> list[RatePublic]:
    if not to_date:
        to_date = date.today()
    rates = get_rate_from_to_date(session, from_date, to_date)
    if not rates:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Empty search"
        )
    return rates
