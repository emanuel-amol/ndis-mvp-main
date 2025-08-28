from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class CarePlan(Base):
    __tablename__ = "care_plans"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(Integer, ForeignKey("participants.id"), nullable=False)
    goals = Column(String(4000), nullable=True)
    supports = Column(String(4000), nullable=True)

    participant = relationship("Participant")
