from datetime import datetime
from typing import list
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status

from pymongo.collection import Collection

from app.dependencies import get_users_collection
from app.schemas import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, users_collection: Collection = Depends(get_users_collection)):
    if users_collection.find_one({"email": payload.email}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    user_doc = { "id": str(uuid4()), "name": payload.name, "email": payload.email, "created_at": datetime.utcnow()}
    users_collection.insert_one(user_doc)
    return user_doc
@router.get("", response_model=list[UserResponse])
def get_users(users_collection: Collection = Depends(get_users_collection)):
    return list(users_collection.find())
