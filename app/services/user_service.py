from fastapi import Depends, Query, HTTPException
from models.user import UserRequest, User
from configs.database import get_session
from services import password_hash_service as pass_service
from sqlalchemy.orm import Session

async def register(userReq: UserRequest, session : Session = Depends(get_session)):
    hashed_password = pass_service.get_password_hash(userReq.password)
    try:
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

async def get_user_by_username(name: str = Query()) -> User:
    session = next(get_session())
    user = session.query(User).filter(User.username == name).first()
    if user is None:
        raise HTTPException(404, detail="User not found")
    return user