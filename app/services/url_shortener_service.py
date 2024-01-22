from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from configs.database import get_session
from models.url import UrlRequest, Url
from models.user import User
from services import auth_service
from typing import List


def get_long_url(url_id: str, session: Session = Depends(get_session)) -> Url:
    
    long_url = session.query(Url).filter(Url.id == url_id).first()

    if long_url is None:
        raise HTTPException(409, detail="Could not get redirect URL")

    return long_url

def shorten(url: UrlRequest, session: Session = Depends(get_session)) -> str:
    shortened = Url(id=get_url_id(url.user_id), original_url=url.url, owner_id=url.user_id)
    
    while(session.query(Url).filter_by(id=shortened.id).first() is not None):
        shortened.id = get_url_id(url.user_id)
    
    try:
        session.add(shortened)
        session.commit()
    except IntegrityError as e:
        raise HTTPException(409, detail="Could not shorten URL")
    
    return build_url_for_id(shortened.id)

def get_url_id(user_id: str) -> str:
    import os
    import base64
    
    id = base64.b64encode(f'{os.urandom(32)}:{user_id}'.encode())
    return id.decode()[:10]

def get_user_urls(user: User = Depends(auth_service.get_current_active_user),
                  session: Session = Depends(get_session)) -> List[str]:
    
    urls = session.query(Url).filter(Url.owner_id == user.id).all()
    return [build_url_for_id(url.id) for url in urls]

def build_url_for_id(url_id: str) -> str:
    return f'http://127.0.0.1:8000/{url_id}'