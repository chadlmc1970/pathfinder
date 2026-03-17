from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    career_id = Column(Integer, ForeignKey("careers.id"), nullable=False)
    score = Column(Float, nullable=False)  # 0-1 recommendation score
    reason = Column(String, nullable=True)  # Why this was recommended
    shown_at = Column(DateTime, default=datetime.utcnow)
    clicked = Column(Boolean, default=False)

    # Relationships
    user = relationship("User", back_populates="recommendations")
    career = relationship("Career", back_populates="recommendations")
