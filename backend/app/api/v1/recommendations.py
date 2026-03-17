from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.recommendation import Recommendation
from app.schemas.recommendation import RecommendationCreate, RecommendationResponse

router = APIRouter()


@router.get("/", response_model=List[RecommendationResponse])
def get_recommendations(
    user_id: int,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Get personalized recommendations for a user."""
    recommendations = (
        db.query(Recommendation)
        .filter(Recommendation.user_id == user_id)
        .order_by(Recommendation.score.desc())
        .limit(limit)
        .all()
    )
    return recommendations


@router.post("/", response_model=RecommendationResponse, status_code=status.HTTP_201_CREATED)
def create_recommendation(recommendation: RecommendationCreate, db: Session = Depends(get_db)):
    """Create a new recommendation."""
    db_recommendation = Recommendation(**recommendation.model_dump())
    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)
    return db_recommendation


@router.put("/{recommendation_id}/clicked", response_model=RecommendationResponse)
def mark_clicked(recommendation_id: int, db: Session = Depends(get_db)):
    """Mark a recommendation as clicked."""
    db_recommendation = db.query(Recommendation).filter(Recommendation.id == recommendation_id).first()
    if not db_recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")

    db_recommendation.clicked = True
    db.commit()
    db.refresh(db_recommendation)
    return db_recommendation
