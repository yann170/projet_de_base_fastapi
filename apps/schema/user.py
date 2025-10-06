from typing import Optional, Union, Sequence
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone 
from uuid import UUID, uuid4
from typing import List
from pydantic import EmailStr



class UserCreate(SQLModel):
    username: str
    password: str  
    email: Optional[EmailStr] = None
    numero: Optional[str] = None

class UserReadSimple(SQLModel):
    id: UUID  
    username: str
    email: Optional[EmailStr] = None
    created_at: datetime
    numero: Optional[str] = None
    statut: str
    role :  str 


class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    numero: Optional[str] = None
    statut: Optional[str] = None

class UserDelete(SQLModel):
    id: UUID  
