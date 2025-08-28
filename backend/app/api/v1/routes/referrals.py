from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.referral import Referral
from app.schemas.referral import ReferralCreate, ReferralRead

router = APIRouter(prefix="/referrals", tags=["referrals"])

@router.post("/", response_model=ReferralRead)
def create_referral(payload: ReferralCreate, db: Session = Depends(get_db_dep)):
    obj = Referral(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[ReferralRead])
def list_referrals(db: Session = Depends(get_db_dep)):
    return db.query(Referral).order_by(Referral.id.desc()).all()
