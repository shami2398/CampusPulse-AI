"""AI Assistant schemas"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime


class AIMessageBase(BaseModel):
    role: str = Field(..., pattern="^(user|assistant)$")
    content: str = Field(..., min_length=1)


class AIQueryRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    session_id: Optional[str] = None
    context_type: Optional[str] = None
    subject_area: Optional[str] = None


class AIQueryResponse(BaseModel):
    response: str
    session_id: str
    confidence: float
    context_used: bool
    timestamp: datetime


class AIConversationResponse(BaseModel):
    id: int
    user_id: int
    session_id: str
    messages: List[Dict]
    context_type: Optional[str]
    subject_area: Optional[str]
    total_messages: int
    last_activity: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class StudyPlanRequest(BaseModel):
    subject: str
    duration_weeks: int = Field(..., ge=1, le=16)
    difficulty_level: str = Field(..., pattern="^(beginner|intermediate|advanced)$")
    goals: Optional[List[str]] = None
