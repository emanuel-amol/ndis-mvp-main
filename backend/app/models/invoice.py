from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(Integer, ForeignKey("participants.id"), nullable=False)
    amount_cents = Column(Integer, nullable=False, default=0)
    status = Column(String(50), nullable=False, default="DRAFT")

    participant = relationship("Participant")
