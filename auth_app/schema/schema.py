import uuid

from fastapi_users import schemas  # type: ignore


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str
    email: str
    numero: str | None = None
    statut: str
    role : str


class UserCreate(schemas.BaseUserCreate):
    username: str
    numero: str | None = None
  

class UserUpdate(schemas.BaseUserUpdate):
    username: str | None = None
    email: str | None = None
    numero: str | None = None
    statut: str | None = None
    role : str | None = None