from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.init_db import init_db
from app.api.v1.routes import participants, referrals, care, risk, documents, quotations, homes, rooms, schedule, invoices
from app.openapi_tags import TAGS

app = FastAPI(title="NDIS API", version="1.0.0", openapi_tags=TAGS)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(participants.router, prefix="/api/v1")
app.include_router(referrals.router,   prefix="/api/v1")
app.include_router(care.router,        prefix="/api/v1")
app.include_router(risk.router,        prefix="/api/v1")
app.include_router(documents.router,   prefix="/api/v1")
app.include_router(quotations.router,  prefix="/api/v1")
app.include_router(homes.router,       prefix="/api/v1")
app.include_router(rooms.router,       prefix="/api/v1")
app.include_router(schedule.router,    prefix="/api/v1")
app.include_router(invoices.router,    prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/healthz")
def healthz():
    return {"ok": True}
