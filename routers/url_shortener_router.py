from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from entities.models.url import UrlRequest

from services import url_shortener_service

router = APIRouter(
    prefix="/u",
    tags=["url_shortener"]
)

@router.get("/{url_id}")
async def redirect(url_id: str, long_url = Depends(url_shortener_service.get_long_url)):
    redirect = long_url.original_url 
    return RedirectResponse(url = redirect, status_code=302)

@router.post("/shorten")
async def shorten(url: UrlRequest, shortened = Depends(url_shortener_service.shorten)):
    return shortened