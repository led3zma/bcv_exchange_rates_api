from datetime import date
from pydantic import BaseModel
from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base

""" SQLAlchemy Models """


class Rate(Base):
    __tablename__ = "rate"

    id: Mapped[int] = mapped_column(primary_key=True)
    value_date: Mapped[date]
    rate: Mapped[float] = mapped_column(Float(4))


""" Pydantic schemas """


class RatePublic(BaseModel):
    value_date: date
    rate: float
