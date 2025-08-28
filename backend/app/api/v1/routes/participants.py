from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.participant import Participant
from app.schemas.participant import ParticipantCreate, ParticipantRead

router = APIRouter(prefix="/participants", tags=["participants"])

@router.post("/", response_model=ParticipantRead)
def create_participant(payload: ParticipantCreate, db: Session = Depends(get_db_dep)):
    exists = db.query(Participant).filter(Participant.ndis_number == payload.ndis_number).first()
    if exists:
        raise HTTPException(status_code=400, detail="NDIS number already exists")
    obj = Participant(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[ParticipantRead])
def list_participants(db: Session = Depends(get_db_dep)):
    return db.query(Participant).order_by(Participant.id.desc()).all()
