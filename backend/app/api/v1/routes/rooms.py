from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.room import Room
from app.schemas.room import Room as RoomSchema

router = APIRouter(prefix="/rooms", tags=["sil"])

@router.post("/", response_model=RoomSchema)
def create_room(payload: RoomSchema, db: Session = Depends(get_db_dep)):
    obj = Room(**payload.model_dump(exclude={"id"}))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/by_home/{home_id}", response_model=list[RoomSchema])
def list_rooms(home_id: int, db: Session = Depends(get_db_dep)):
    return db.query(Room).filter(Room.home_id == home_id).all()
