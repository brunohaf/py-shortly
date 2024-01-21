from fastapi import APIRouter, Depends, status
from services import auth_service
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/token",
    tags=["authentication"]
)

@router.post("",status_code=status.HTTP_200_OK)
async def login(token = Depends(auth_service.get_access_token)):
    return token