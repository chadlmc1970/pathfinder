from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict


class UserBase(BaseModel):
    email: EmailStr
    grade_level: int = Field(..., ge=6, le=12)
    school: Optional[str] = None
    interest_dna: Optional[Dict] = None


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    grade_level: Optional[int] = Field(None, ge=6, le=12)
    school: Optional[str] = None
    interest_dna: Optional[Dict] = None
    engagement_score: Optional[float] = None


class UserResponse(UserBase):
    id: int
    engagement_score: float

    model_config = {"from_attributes": True}
