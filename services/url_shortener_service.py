from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_session
from entities.models.url import UrlRequest, Url
import base64
import zlib


def get_long_url(url_id: str, session: Session = Depends(get_session)):
    
    long_url = session.query(Url).filter(Url.id == url_id).first()

    if long_url is None:
        raise HTTPException(409, detail="Could not get redirect URL")

    return long_url

def shorten(url: UrlRequest, session: Session = Depends(get_session)): #TO-DO: Better handle of shortened url id.
    id = base64.b64encode(f'{url.url}|{url.user_id}'.encode('ascii'))
    id_s = id.decode('ascii')
    shortened = Url(id=id_s, original_url=url.url, owner_id=url.user_id)
    session.add(shortened)
    session.commit()
    return shortened
