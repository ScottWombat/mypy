from pydantic import BaseModel

class ServiceHealth(BaseModel):
    http_ok: bool = True
    database_ok: bool = False