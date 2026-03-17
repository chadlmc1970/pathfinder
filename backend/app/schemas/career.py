from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime


class CareerBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    industry_sector: str = Field(..., min_length=1, max_length=100)
    description: str
    salary_range_min: Optional[int] = None
    salary_range_max: Optional[int] = None
    education_required: str
    skills: Optional[List[str]] = None  # List of skill strings
    pathway: Optional[Dict] = None


class CareerCreate(CareerBase):
    pass


class CareerUpdate(CareerBase):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    industry_sector: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    education_required: Optional[str] = None


class CareerResponse(CareerBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
