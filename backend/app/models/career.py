from sqlalchemy import Column, Integer, String, Text, Float, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Career(Base):
    __tablename__ = "careers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    industry_sector = Column(String, nullable=False, index=True)  # Healthcare, Skilled Trades, etc.
    description = Column(Text, nullable=False)
    salary_range_min = Column(Integer, nullable=False)  # Annual salary in USD
    salary_range_max = Column(Integer, nullable=False)
    education_required = Column(String, nullable=False)  # High School, Associate, Bachelor's, etc.
    skills = Column(JSON, nullable=True)  # {"technical": ["..."], "soft": ["..."]}
    pathway = Column(JSON, nullable=True)  # Career pathway steps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    videos = relationship("Video", back_populates="career")
    engagement = relationship("Engagement", back_populates="career")
    recommendations = relationship("Recommendation", back_populates="career")
