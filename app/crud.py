from datetime import date, timedelta
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Rate


def get_rate_by_date(session: Session, value_date: date) -> Rate | None:
    # The saturday's and sunday's valid rate is the same for friday's rate
    target_date = {
        5: value_date - timedelta(days=1),
        6: value_date - timedelta(days=2),
    }.get(value_date.weekday(), value_date)
    rate = session.scalars(select(Rate).where(Rate.value_date == target_date)).first()
    return rate
