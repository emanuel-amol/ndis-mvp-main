from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.quotation import Quotation
from app.schemas.quotation import Quotation as QuoteSchema

router = APIRouter(prefix="/quotations", tags=["quotations"])

@router.post("/", response_model=QuoteSchema)
def create_quote(payload: QuoteSchema, db: Session = Depends(get_db_dep)):
    obj = Quotation(**payload.model_dump(exclude={"id"}))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[QuoteSchema])
def list_quotes(db: Session = Depends(get_db_dep)):
    return db.query(Quotation).order_by(Quotation.id.desc()).all()
