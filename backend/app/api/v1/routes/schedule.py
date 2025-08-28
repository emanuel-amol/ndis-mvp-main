from fastapi import APIRouter

router = APIRouter(prefix="/schedule", tags=["schedule"])

@router.get("/ping")
def ping():
    return {"ok": True}
