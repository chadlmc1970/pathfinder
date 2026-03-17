from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RecommendationBase(BaseModel):
    user_id: int
    career_id: int
    score: float
    reason: Optional[str] = None


class RecommendationCreate(RecommendationBase):
    pass


class RecommendationResponse(RecommendationBase):
    id: int
    shown_at: datetime
    clicked: bool

    model_config = {"from_attributes": True}
