# routers/user.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from uuid import UUID
from typing import Annotated, List
from ..config.database import get_session
from apps.models.models import User
from ..schema.user import  UserReadSimple, UserUpdate  
from auth_app.service.authenticate import current_active_user
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/users", tags=["Users"],dependencies=[Depends(current_active_user)] )


# -------------------------------
# READ LIST
# -------------------------------
@router.get("/get_users/", response_model=List[User])
def read_users(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

# -------------------------------
# READ SINGLE
# -------------------------------
@router.get("/user/{user_id}", response_model=UserReadSimple)
def read_user(user_id: UUID, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user or user.statut == "delete":
        raise HTTPException(status_code=404, detail="User not found")
    return user

# -------------------------------
# UPDATE
# -------------------------------
@router.patch("/user/{user_id}", response_model=UserReadSimple)

def update_user(user_id: UUID, user_update: UserUpdate, session: Session = Depends(get_session)):
    db_user = session.get(User, user_id)
    if not db_user or db_user.statut == "delete":
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_update.model_dump(exclude_unset=True)

    # Vérifier si l'email est déjà pris par un autre utilisateur
    if "email" in update_data and update_data["email"] != db_user.email:
        existing_user = session.exec(
            select(User).where(User.email == update_data["email"], User.id != user_id)
        ).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already in use")

    # Mise à jour des champs
    for key, value in update_data.items():
        setattr(db_user, key, value)

    try:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="Unique constraint violation")

    return db_user

# -------------------------------
# DELETE
# -------------------------------
@router.delete("/user/{user_id}")
async def delete_user(user_id: UUID, session: Session = Depends(get_session)):
    db_user = session.get(User, user_id)
    if not db_user or db_user.statut == "delete":
        raise HTTPException(status_code=404, detail="User not found")
    db_user.statut = "delete"
    session.add(db_user)
    session.commit()
    return {"ok": True}
 