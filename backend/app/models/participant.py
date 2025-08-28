from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    ndis_number = Column(String(32), unique=True, index=True, nullable=False)
    dob = Column(Date, nullable=True)
