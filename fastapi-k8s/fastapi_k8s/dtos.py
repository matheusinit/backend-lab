from typing import Optional
from datetime import datetime

from pydantic import BaseModel
import uuid


class BookCreate(BaseModel):
    name: str
    description: str


class BookUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class BookResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]


class Message(BaseModel):
    message: str
