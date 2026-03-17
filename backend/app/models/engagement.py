from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Engagement(Base):
    __tablename__ = "engagement"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    career_id = Column(Integer, ForeignKey("careers.id"), nullable=False)
    video_id = Column(Integer, ForeignKey("videos.id"), nullable=False)
    action = Column(String, nullable=False)  # "watched", "liked", "saved", "skipped", "shared"
    watch_duration_seconds = Column(Float, nullable=True)  # How long they watched
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="engagement")
    career = relationship("Career", back_populates="engagement")
    video = relationship("Video", back_populates="engagement")
