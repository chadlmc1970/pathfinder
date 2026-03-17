from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.video import Video
from app.schemas.video import VideoCreate, VideoUpdate, VideoResponse

router = APIRouter()


@router.get("/", response_model=List[VideoResponse])
def get_videos(
    skip: int = 0,
    limit: int = 50,
    career_id: int = None,
    db: Session = Depends(get_db)
):
    """Get all videos with optional filtering by career."""
    query = db.query(Video)
    if career_id:
        query = query.filter(Video.career_id == career_id)
    videos = query.offset(skip).limit(limit).all()
    return videos


@router.get("/{video_id}", response_model=VideoResponse)
def get_video(video_id: int, db: Session = Depends(get_db)):
    """Get a single video by ID."""
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video


@router.post("/", response_model=VideoResponse, status_code=status.HTTP_201_CREATED)
def create_video(video: VideoCreate, db: Session = Depends(get_db)):
    """Create a new video."""
    db_video = Video(**video.model_dump())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


@router.put("/{video_id}", response_model=VideoResponse)
def update_video(
    video_id: int,
    video: VideoUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing video."""
    db_video = db.query(Video).filter(Video.id == video_id).first()
    if not db_video:
        raise HTTPException(status_code=404, detail="Video not found")

    for key, value in video.model_dump(exclude_unset=True).items():
        setattr(db_video, key, value)

    db.commit()
    db.refresh(db_video)
    return db_video


@router.delete("/{video_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_video(video_id: int, db: Session = Depends(get_db)):
    """Delete a video."""
    db_video = db.query(Video).filter(Video.id == video_id).first()
    if not db_video:
        raise HTTPException(status_code=404, detail="Video not found")

    db.delete(db_video)
    db.commit()
    return None
