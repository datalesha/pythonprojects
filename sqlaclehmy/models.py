import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, BigInteger, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_256
import enum
from typing import Annotated
"""
В метадата хранятся данные обо всех таблицах, созданных на стороне python
"""
metadata_obj = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]
created_dt = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_dt = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.utcnow()
)]


class WorkersOrm(Base):
    __tablename__ = "workers"
    # id: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[intpk] #так можно делать, когда создал Annodated тип данных - упрощает код
    username: Mapped[str] = mapped_column()

class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class ResumesOrm(Base):
    __tablename__ = "resumes"
    # id: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[intpk]
    # title: Mapped[str] = mapped_column(String(256))
    title: Mapped[str_256]
    # compensation: Mapped[int] = mapped_column(nullable=True)
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    # ondelete - удаляем все записи, ассоциированные с id
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete='CASCADE'))
    # created_dt: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    # created_dt: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    # updated_dt: Mapped[datetime.datetime] = mapped_column(
    #     server_default=text("TIMEZONE('utc', now())"),
    #     onupdate=datetime.datetime.utcnow())
    created_dt: Mapped[created_dt]
    updated_dt: Mapped[updated_dt]















# императивный стиль создания моделей
workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String)
)

sbercl_table = Table(
    "sber_clients",
    metadata_obj,
    Column('epk_id', BigInteger, primary_key=True),
    Column('surname', String),
    Column('name', String),
    Column('age', Integer)

)

