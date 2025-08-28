from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.risk import RiskAssessment
from app.schemas.risk import RiskAssessment as RiskSchema

router = APIRouter(prefix="/risk", tags=["risk"])

@router.post("/", response_model=RiskSchema)
def save_risk(payload: RiskSchema, db: Session = Depends(get_db_dep)):
    obj = RiskAssessment(**payload.model_dump(exclude={"id"}))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/{participant_id}", response_model=list[RiskSchema])
def get_risks(participant_id: int, db: Session = Depends(get_db_dep)):
    return db.query(RiskAssessment).filter(RiskAssessment.participant_id == participant_id).all()
