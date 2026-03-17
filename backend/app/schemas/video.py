from pydantic import BaseModel
from typing import Optional


class VideoBase(BaseModel):
    career_id: int
    blob_url: str
    thumbnail_url: Optional[str] = None
    duration_seconds: int
    transcript: Optional[str] = None


class VideoCreate(VideoBase):
    pass


class VideoUpdate(BaseModel):
    blob_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    duration_seconds: Optional[int] = None
    transcript: Optional[str] = None


class VideoResponse(VideoBase):
    id: int

    model_config = {"from_attributes": True}
