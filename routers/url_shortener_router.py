from fastapi import APIRouter, Depends, status
from fastapi.responses import RedirectResponse, Response
from entities.models.url import UrlRequest
from services import url_shortener_service
from typing import List

from services import url_shortener_service

router = APIRouter(
    tags=["url_shortener"]
)

@router.get("/{url_id}")
async def redirect(url_id: str, long_url = Depends(url_shortener_service.get_long_url)) -> RedirectResponse:
    redirect = long_url.original_url 
    return RedirectResponse(url = redirect, status_code=302)

@router.post("/api/shorten", status_code=status.HTTP_201_CREATED)
async def shorten(url: UrlRequest, shortened = Depends(url_shortener_service.shorten)) -> str:
    return shortened

@router.get("/api/shortens")
async def get_shortens(shortens: List[str] = Depends(url_shortener_service.get_user_urls)):
    if len(shortens) == 0:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return shortens