from typing import Optional
from app.core.config import settings
from pathlib import Path

# Minimal local fallback storage so app runs without IBM COS.
UPLOAD_ROOT = Path("/app/uploads")
UPLOAD_ROOT.mkdir(parents=True, exist_ok=True)

def save_file(filename: str, data: bytes) -> str:
    """
    If IBM_COS_ENABLED=false -> stores locally under /app/uploads and returns a file:// path.
    If true -> (stub) raise NotImplementedError to avoid runtime crashes from missing SDK.
    """
    if not settings.ibm_cos_enabled:
        dest = UPLOAD_ROOT / filename
        dest.write_bytes(data)
        return f"/uploads/{filename}"
    # Keep explicit to avoid half-implemented cloud writes:
    raise NotImplementedError("IBM COS upload not implemented in this stub. Set IBM_COS_ENABLED=false.")
