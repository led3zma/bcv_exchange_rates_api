from datetime import date, timedelta
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Rate


def _get_weekend_valid_date(value_date: date) -> date:
    # The saturday's and sunday's valid rate is the same for friday's rate
    return {
        5: value_date - timedelta(days=1),
        6: value_date - timedelta(days=2),
    }.get(value_date.weekday(), value_date)


def get_rate_by_date(session: Session, value_date: date) -> Rate | None:
    rate = session.scalars(
        select(Rate).where(Rate.value_date == _get_weekend_valid_date(value_date))
    ).first()
    return rate


def get_rate_from_to_date(
    session: Session, from_date: date, to_date: date
) -> list[Rate] | None:
    rates = session.scalars(
        select(Rate).where(
            Rate.value_date >= _get_weekend_valid_date(from_date),
            Rate.value_date <= _get_weekend_valid_date(to_date),
        )
    )
    return list(rates.all())
