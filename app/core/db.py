from typing import Annotated, Generator
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from app.core.config import get_settings

settings = get_settings()

engine = create_engine(url=settings.database_url, echo=True)


def get_db_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db_session)]


class Base(DeclarativeBase):
    pass
