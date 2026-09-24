#Define the Pydantic model that the FastAPI app will use to validate the request body for creating a new user.
from datetime import datetime
import typing
typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="The name of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., min_length=8, description="The password of the user")
    role: UserRole = Field(default=UserRole.EMPLOYEE, description="The role of the user")

class UserResponse(BaseModel):
    #shape the response model for the user data returned by the API
    id: str 
    name: str 
    email: EmailStr
    role: UserRole
    created_at: datetime
    