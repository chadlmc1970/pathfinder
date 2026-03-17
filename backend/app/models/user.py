from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    grade_level = Column(Integer, nullable=False)  # 8 for 8th grade
    school = Column(String, nullable=True)
    interest_dna = Column(JSON, nullable=True)  # Interest DNA profile
    engagement_score = Column(Float, default=0.0)

    # Relationships
    engagement = relationship("Engagement", back_populates="user")
    recommendations = relationship("Recommendation", back_populates="user")
