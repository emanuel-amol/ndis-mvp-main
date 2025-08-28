from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.api.v1.deps import get_db_dep
from app.models.document import Document
from app.schemas.document import Document as DocumentSchema
from app.services.ibm_cos import save_file

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload", response_model=DocumentSchema)
async def upload_document(participant_id: int | None = None, file: UploadFile = File(...), db: Session = Depends(get_db_dep)):
    data = await file.read()
    url = save_file(file.filename, data)
    doc = Document(participant_id=participant_id, filename=file.filename, url=url)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

@router.get("/", response_model=list[DocumentSchema])
def list_documents(db: Session = Depends(get_db_dep)):
    return db.query(Document).order_by(Document.id.desc()).all()
