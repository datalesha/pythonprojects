from sqlalchemy.engine import URL, create_engine
from config import settings
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from typing import Annotated
from sqlalchemy import String

sync_engine = create_engine(
        url=settings.DATABASE_URL_psycopg,
        echo=True,
        pool_size=5,
        max_overflow=10)

# Session нужна для транзакций, sessionmaker - фабрика сессий (вместо использования просто Session
session_factory = sessionmaker(sync_engine)

str_256 = Annotated[str, 256]
class Base(DeclarativeBase):
        type_annotion_map = {
                str_256: String(256)
        }
        pass



