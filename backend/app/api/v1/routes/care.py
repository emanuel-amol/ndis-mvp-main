from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.careplan import CarePlan
from app.schemas.careplan import CarePlan as CarePlanSchema  # simple schema: id, participant_id, goals, supports

router = APIRouter(prefix="/care", tags=["care"])

@router.post("/", response_model=CarePlanSchema)
def save_care_plan(payload: CarePlanSchema, db: Session = Depends(get_db_dep)):
    obj = CarePlan(**payload.model_dump(exclude={"id"}))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/{participant_id}", response_model=list[CarePlanSchema])
def get_care_plans(participant_id: int, db: Session = Depends(get_db_dep)):
    return db.query(CarePlan).filter(CarePlan.participant_id == participant_id).all()
