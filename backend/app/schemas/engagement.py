from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EngagementBase(BaseModel):
    user_id: int
    career_id: int
    video_id: int
    action: str  # "watched", "liked", "saved", "skipped", "shared"
    watch_duration_seconds: Optional[float] = None


class EngagementCreate(EngagementBase):
    pass


class EngagementResponse(EngagementBase):
    id: int
    timestamp: datetime

    model_config = {"from_attributes": True}
