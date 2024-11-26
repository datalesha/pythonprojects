from sqlalchemy import text, insert, select
from database import sync_engine, session_factory, Base
from models import WorkersOrm


class SyncORM:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_michael = WorkersOrm(username="Michael")
            session.add_all([worker_jack, worker_michael])
            session.flush() # команда отправляет все изменения, которые есть в текущей сессии, в базу
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            # при таком подходе можем получить только 1 запись
            worker_id = 1
            # worker_jack = session.get(WorkersOrm, worker_id)
            query = select(WorkersOrm)  # вместо workers_table в core
            result = session.execute(query)
            # print(result.all()) # вернёт кортежи с объектами
            print(result.scalars().all())

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
        with session_factory() as session:
            worker_michael = session.get(WorkersOrm, worker_id)
            worker_michael.username = new_username
            session.expire_all() # отменяет все незакомиченные изменения
            session.refresh(worker_michael) # позволяет получить текущие состояние данных в базе
            session.commit()