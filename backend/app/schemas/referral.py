from pydantic import BaseModel
from typing import Optional

class ReferralBase(BaseModel):
    participant_id: Optional[int] = None
    source: str
    notes: Optional[str] = None

class ReferralCreate(ReferralBase):
    pass

class ReferralRead(ReferralBase):
    id: int
    class Config:
        from_attributes = True
