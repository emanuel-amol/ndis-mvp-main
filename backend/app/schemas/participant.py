from pydantic import BaseModel
from typing import Optional
from datetime import date

class ParticipantBase(BaseModel):
    first_name: str
    last_name: str
    ndis_number: str
    dob: Optional[date] = None

class ParticipantCreate(ParticipantBase):
    pass

class ParticipantRead(ParticipantBase):
    id: int
    class Config:
        from_attributes = True
