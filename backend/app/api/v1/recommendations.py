from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from typing import List
import json
from anthropic import Anthropic

from app.core.database import get_db
from app.core.config import settings
from app.models.recommendation import Recommendation
from app.models.engagement import Engagement
from app.models.career import Career
from app.models.user import User
from app.schemas.recommendation import RecommendationCreate, RecommendationResponse

router = APIRouter()

# Initialize Anthropic client
client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)


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


@router.post("/generate", response_model=List[RecommendationResponse])
def generate_recommendations(
    user_id: int,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Generate AI-powered personalized career recommendations for a user.

    Algorithm:
    1. Analyze user's engagement history (likes, saves, watches)
    2. Build "Interest DNA" profile from engagement patterns
    3. Call Claude 4.6 to generate personalized career matches
    4. Score recommendations (0-100)
    5. Store reasoning for each recommendation
    6. Return top N careers ordered by score
    """
    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Get user's engagement history
    engagements = (
        db.query(Engagement)
        .filter(Engagement.user_id == user_id)
        .all()
    )

    if not engagements:
        raise HTTPException(
            status_code=400,
            detail="User has no engagement history yet. Watch some career videos first!"
        )

    # Build Interest DNA from engagement patterns
    liked_career_ids = [e.career_id for e in engagements if e.action in ['liked', 'saved']]
    skipped_career_ids = [e.career_id for e in engagements if e.action == 'skipped']
    watched_career_ids = [e.career_id for e in engagements if e.action == 'watched']

    # Get career details for liked/saved careers
    liked_careers = db.query(Career).filter(Career.id.in_(liked_career_ids)).all() if liked_career_ids else []

    # Calculate engagement patterns
    total_engagements = len(engagements)
    like_rate = len(liked_career_ids) / total_engagements if total_engagements > 0 else 0
    skip_rate = len(skipped_career_ids) / total_engagements if total_engagements > 0 else 0

    # Build Interest DNA profile
    interest_dna = {
        "total_engagements": total_engagements,
        "like_rate": round(like_rate, 2),
        "skip_rate": round(skip_rate, 2),
        "liked_careers": [c.title for c in liked_careers],
        "liked_industries": list(set([c.industry_sector for c in liked_careers])),
        "liked_salary_ranges": [f"${c.salary_range_min//1000}k-${c.salary_range_max//1000}k" for c in liked_careers],
        "preferred_education": [c.education_required for c in liked_careers],
    }

    # Update user's Interest DNA profile
    user.interest_dna = interest_dna
    db.commit()

    # Get all careers (excluding ones user already liked/saved)
    all_careers = (
        db.query(Career)
        .filter(~Career.id.in_(liked_career_ids))
        .all()
    )

    if not all_careers:
        raise HTTPException(
            status_code=400,
            detail="No new careers to recommend. You've engaged with all available careers!"
        )

    # Prepare data for Claude
    liked_careers_summary = "\n".join([
        f"- {c.title} ({c.industry_sector}, ${c.salary_range_min//1000}k-${c.salary_range_max//1000}k, {c.education_required})"
        for c in liked_careers
    ])

    careers_to_score = "\n".join([
        f"ID {c.id}: {c.title} ({c.industry_sector}, ${c.salary_range_min//1000}k-${c.salary_range_max//1000}k, {c.education_required}) - {c.description[:150]}..."
        for c in all_careers[:30]  # Limit to 30 to fit in context
    ])

    # Build prompt for Claude 4.6
    prompt = f"""You are PathFinder's AI Career Advisor for Louisiana 8th graders.

USER PROFILE:
- Grade: {user.grade_level}th grade
- School: {user.school or 'Not specified'}
- Total Engagements: {total_engagements}
- Like Rate: {like_rate*100:.0f}%

CAREERS THE STUDENT LIKED/SAVED:
{liked_careers_summary if liked_careers_summary else 'None yet'}

INTEREST DNA:
- Liked Industries: {', '.join(interest_dna['liked_industries']) if interest_dna['liked_industries'] else 'None yet'}
- Education Preferences: {', '.join(set(interest_dna['preferred_education'])) if interest_dna['preferred_education'] else 'Unknown'}

TASK: Generate {limit} personalized career recommendations from the list below. For each career, provide:
1. Career ID (from the list)
2. Match Score (0-100, where 100 = perfect match)
3. Reasoning (1-2 sentences explaining why this career matches the student's interests)

AVAILABLE CAREERS TO RECOMMEND:
{careers_to_score}

OUTPUT FORMAT (JSON):
{{
  "recommendations": [
    {{
      "career_id": 21,
      "score": 95,
      "reason": "Based on your interest in [X industry], this career offers [Y benefit] and requires [Z education level]."
    }}
  ]
}}

Generate exactly {limit} recommendations, ranked by match score (highest first)."""

    # Call Claude 4.6 API
    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",  # Latest Claude model
            max_tokens=2000,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Parse response
        response_text = response.content[0].text

        # Extract JSON from response (handle markdown code blocks)
        if "```json" in response_text:
            json_start = response_text.index("```json") + 7
            json_end = response_text.rindex("```")
            response_text = response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.index("```") + 3
            json_end = response_text.rindex("```")
            response_text = response_text[json_start:json_end].strip()

        recommendations_data = json.loads(response_text)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI recommendation generation failed: {str(e)}"
        )

    # Save recommendations to database
    db_recommendations = []
    for rec_data in recommendations_data.get("recommendations", [])[:limit]:
        # Validate career exists
        career = db.query(Career).filter(Career.id == rec_data["career_id"]).first()
        if not career:
            continue

        # Check if recommendation already exists
        existing = (
            db.query(Recommendation)
            .filter(
                Recommendation.user_id == user_id,
                Recommendation.career_id == rec_data["career_id"]
            )
            .first()
        )

        if existing:
            # Update existing recommendation
            existing.score = rec_data["score"] / 100.0  # Normalize to 0-1
            existing.reason = rec_data["reason"]
            db.commit()
            db.refresh(existing)
            db_recommendations.append(existing)
        else:
            # Create new recommendation
            db_recommendation = Recommendation(
                user_id=user_id,
                career_id=rec_data["career_id"],
                score=rec_data["score"] / 100.0,  # Normalize to 0-1
                reason=rec_data["reason"]
            )
            db.add(db_recommendation)
            db.commit()
            db.refresh(db_recommendation)
            db_recommendations.append(db_recommendation)

    return db_recommendations


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
