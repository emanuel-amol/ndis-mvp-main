from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Home(Base):
    __tablename__ = "homes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    address = Column(String(500), nullable=True)
