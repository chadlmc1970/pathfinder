from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.engagement import Engagement
from app.schemas.engagement import EngagementCreate, EngagementResponse

router = APIRouter()


@router.get("/", response_model=List[EngagementResponse])
def get_engagements(
    skip: int = 0,
    limit: int = 100,
    user_id: int = None,
    career_id: int = None,
    db: Session = Depends(get_db)
):
    """Get engagement events with optional filtering."""
    query = db.query(Engagement)
    if user_id:
        query = query.filter(Engagement.user_id == user_id)
    if career_id:
        query = query.filter(Engagement.career_id == career_id)
    engagements = query.order_by(Engagement.timestamp.desc()).offset(skip).limit(limit).all()
    return engagements


@router.post("/", response_model=EngagementResponse, status_code=status.HTTP_201_CREATED)
def create_engagement(engagement: EngagementCreate, db: Session = Depends(get_db)):
    """Record a new engagement event."""
    db_engagement = Engagement(**engagement.model_dump())
    db.add(db_engagement)
    db.commit()
    db.refresh(db_engagement)
    return db_engagement
