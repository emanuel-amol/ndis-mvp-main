from app.core.config import settings

def create_invoice_stub(participant_id: int, amount_cents: int) -> dict:
    """
    If XERO_ENABLED=false -> return a local stub invoice payload.
    If true -> (stub) raise NotImplementedError to avoid SDK/credentials issues.
    """
    if not settings.xero_enabled:
        return {
            "external": "xero",
            "status": "DRAFT",
            "participant_id": participant_id,
            "amount_cents": amount_cents,
            "note": "Xero integration stubbed. Set XERO_ENABLED=true to wire a real call."
        }
    raise NotImplementedError("Xero API integration not implemented in this stub.")
