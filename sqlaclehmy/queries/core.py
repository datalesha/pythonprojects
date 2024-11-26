from sqlalchemy import text, insert, select, update
from database import sync_engine
from models import metadata_obj, workers_table, Base

class SyncCore:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with sync_engine.connect() as conn:
            stmt = insert(workers_table).values(
                [
                    {"username": "Jack"},
                    {"username": "Michael"}
                ]
            )
            conn.execute(stmt)
            conn.commit()
    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_table) # SELECT * FROM WORKERS
            result = conn.execute(query)
            print(result.all())
            conn.commit()

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = 'Misha'):
        with sync_engine.connect() as conn:
            # 1-вариант - использование raw-sql
            # не стоит использовать f-строки для подстановки в statementб лучше использовать bindparams
            # stmt = text("UPDATE workers SET username=:username WHERE id=:worker_id")
            # stmt = stmt.bindparams(username=new_username, worker_id=worker_id)

            # второй вариант обновить таблицу - использование 'пионячьего стиля'
            stmt = (
                update(workers_table)
                .values(username=new_username)
                # .where(workers_table.c.id == worker_id)
                .filter_by(id=worker_id)
            )
            conn.execute(stmt)
            conn.commit()


