from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.career import Career
from app.schemas.career import CareerCreate, CareerUpdate, CareerResponse

router = APIRouter()


@router.get("/", response_model=List[CareerResponse])
def get_careers(
    skip: int = 0,
    limit: int = 50,
    industry: str = None,
    db: Session = Depends(get_db)
):
    """Get all careers with optional filtering."""
    query = db.query(Career)
    if industry:
        query = query.filter(Career.industry_sector == industry)
    careers = query.offset(skip).limit(limit).all()
    return careers


@router.get("/{career_id}", response_model=CareerResponse)
def get_career(career_id: int, db: Session = Depends(get_db)):
    """Get a single career by ID."""
    career = db.query(Career).filter(Career.id == career_id).first()
    if not career:
        raise HTTPException(status_code=404, detail="Career not found")
    return career


@router.post("/", response_model=CareerResponse, status_code=status.HTTP_201_CREATED)
def create_career(career: CareerCreate, db: Session = Depends(get_db)):
    """Create a new career profile."""
    db_career = Career(**career.model_dump())
    db.add(db_career)
    db.commit()
    db.refresh(db_career)
    return db_career


@router.put("/{career_id}", response_model=CareerResponse)
def update_career(
    career_id: int,
    career: CareerUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing career profile."""
    db_career = db.query(Career).filter(Career.id == career_id).first()
    if not db_career:
        raise HTTPException(status_code=404, detail="Career not found")

    for key, value in career.model_dump(exclude_unset=True).items():
        setattr(db_career, key, value)

    db.commit()
    db.refresh(db_career)
    return db_career


@router.delete("/{career_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_career(career_id: int, db: Session = Depends(get_db)):
    """Delete a career profile."""
    db_career = db.query(Career).filter(Career.id == career_id).first()
    if not db_career:
        raise HTTPException(status_code=404, detail="Career not found")

    db.delete(db_career)
    db.commit()
    return None
