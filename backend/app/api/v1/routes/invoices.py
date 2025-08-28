from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.invoice import Invoice
from app.schemas.invoice import Invoice as InvoiceSchema
from app.services.xero_stub import create_invoice_stub

router = APIRouter(prefix="/invoices", tags=["invoices"])

@router.post("/", response_model=InvoiceSchema)
def create_invoice(payload: InvoiceSchema, db: Session = Depends(get_db_dep)):
    # Save locally first
    obj = Invoice(**payload.model_dump(exclude={"id"}))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    # Return stub info to UI (to display)
    stub = create_invoice_stub(obj.participant_id, obj.amount_cents)
    return InvoiceSchema(id=obj.id, participant_id=obj.participant_id, amount_cents=obj.amount_cents, status=stub["status"])
