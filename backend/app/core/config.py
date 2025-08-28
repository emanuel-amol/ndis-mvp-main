from pydantic import BaseModel
import os

class Settings(BaseModel):
    database_dsn: str = os.getenv("DATABASE_DSN", "postgresql+psycopg2://postgres:postgres@localhost:5432/ndis")
    cors_origins: str = os.getenv("BACKEND_CORS_ORIGINS", "http://localhost:5173")

    ibm_cos_enabled: bool = os.getenv("IBM_COS_ENABLED", "false").lower() == "true"
    ibm_cos_endpoint: str = os.getenv("IBM_COS_ENDPOINT", "")
    ibm_cos_api_key: str = os.getenv("IBM_COS_API_KEY", "")
    ibm_cos_instance_crn: str = os.getenv("IBM_COS_INSTANCE_CRN", "")
    ibm_cos_bucket: str = os.getenv("IBM_COS_BUCKET", "")

    xero_enabled: bool = os.getenv("XERO_ENABLED", "false").lower() == "true"
    xero_client_id: str = os.getenv("XERO_CLIENT_ID", "")
    xero_client_secret: str = os.getenv("XERO_CLIENT_SECRET", "")
    xero_redirect_uri: str = os.getenv("XERO_REDIRECT_URI", "")

settings = Settings()
