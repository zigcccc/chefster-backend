from sqlmodel import Session

from db import database


async def get_db():
    with Session(database.engine) as session:
        try:
            yield session

        finally:
            session.close()
