from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Rate


def get_rate_by_date(session: Session, value_date: date) -> Rate | None:
    rate = session.scalars(select(Rate).where(Rate.value_date == value_date)).first()
    return rate
