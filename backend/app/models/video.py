from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    career_id = Column(Integer, ForeignKey("careers.id"), nullable=False)
    blob_url = Column(String, nullable=False)  # Vercel Blob URL
    thumbnail_url = Column(String, nullable=True)
    duration_seconds = Column(Integer, nullable=False)
    transcript = Column(Text, nullable=True)

    # Relationships
    career = relationship("Career", back_populates="videos")
    engagement = relationship("Engagement", back_populates="video")
