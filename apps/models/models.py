from typing import Optional
from datetime import datetime, timezone 
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from pydantic import EmailStr
from fastapi_users_db_sqlmodel import  SQLModelBaseUserDB 

# Classe abstraite (utile pour FastAPI Users)
class User(SQLModelBaseUserDB, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str
    numero: Optional[str] = None
    statut: str = Field(default="active", nullable=False,)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False)
    role: str = Field(default="user", nullable=False,)