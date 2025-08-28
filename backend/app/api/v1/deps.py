from typing import Generator
from app.db.init_db import get_db
from sqlalchemy.orm import Session

def get_db_dep() -> Generator[Session, None, None]:
    yield from get_db()
