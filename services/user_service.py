from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from entities.models.user import UserRequest, User
from config.database import get_session
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def register(userReq: UserRequest, session : Session = Depends(get_session)):
    try:
        hashed_password = pwd_context.hash(userReq.password)
        user = User(username=userReq.username, hashed_password=hashed_password)
        session.add(user)
        session.commit()
    except Exception:
        return False
    return True

async def get_user(id: str, session : Session = Depends(get_session)):
    user = session.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(404, detail="User not found")
    return user

async def get_user_by_username(username: str, session : Session = Depends(get_session)):
    user = session.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(404, detail="User not found")
    return user