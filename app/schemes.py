from typing import Optional
from pydantic import BaseModel


class Payload(BaseModel):
    entity: str
    filter: dict
    fields: Optional[list] = []
    include: Optional[dict] = []

