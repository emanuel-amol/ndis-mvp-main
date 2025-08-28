from sqlalchemy.orm import Session
from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models import participant, referral, careplan, risk, document, home, room, quotation, invoice  # noqa

def init_db() -> None:
    # Simple startup create_all to avoid migration errors for now.
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
