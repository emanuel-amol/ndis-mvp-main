from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.home import Home
from app.schemas.home import Home as HomeSchema

router = APIRouter(prefix="/homes", tags=["sil"])

@router.post("/", response_model=HomeSchema)
def create_home(payload: HomeSchema, db: Session = Depends(get_db_dep)):
    obj = Home(**payload.model_dump(exclude={"id"}))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[HomeSchema])
def list_homes(db: Session = Depends(get_db_dep)):
    return db.query(Home).order_by(Home.id.desc()).all()
