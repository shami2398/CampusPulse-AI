"""AI conversation model"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class AIConversation(Base):
    __tablename__ = "ai_conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Conversation details
    session_id = Column(String, unique=True, index=True, nullable=False)
    messages = Column(JSON, default=list)  # [{role, content, timestamp}]
    
    # Context
    context_type = Column(String, nullable=True)  # academic, study_plan, general
    subject_area = Column(String, nullable=True)  # programming, math, etc.
    
    # Metadata
    total_messages = Column(Integer, default=0)
    last_activity = Column(DateTime, default=datetime.utcnow)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="ai_conversations")
