from fastapi import APIRouter, Depends, status
from models.user import UserRequest
from services import user_service

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# TO-DO: Add authorization (admin roles) to the endpoints

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(userReq: UserRequest, has_succeded = Depends(user_service.register)):
    return f"{userReq.username} registered successfully" if has_succeded else f"{userReq.username} could not be registered"

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_user(id: int, user = Depends(user_service.get_user)):
    return user

@router.get("", status_code=status.HTTP_200_OK)
async def get_user_by_username(user = Depends(user_service.get_user_by_username)):
    return user