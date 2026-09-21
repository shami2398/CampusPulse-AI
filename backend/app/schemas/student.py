"""Student schemas"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime


class StudentBase(BaseModel):
    student_id: str
    major: str
    year: int = Field(..., ge=1, le=4)
    gpa: float = Field(..., ge=0.0, le=4.0)


class StudentCreate(StudentBase):
    user_id: int


class StudentUpdate(BaseModel):
    major: Optional[str] = None
    year: Optional[int] = Field(None, ge=1, le=4)
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0)
    credits_completed: Optional[int] = None
    attendance_rate: Optional[float] = None
    assignment_completion_rate: Optional[float] = None
    participation_score: Optional[float] = None


class StudentResponse(StudentBase):
    id: int
    user_id: int
    credits_completed: int
    attendance_rate: float
    assignment_completion_rate: float
    participation_score: float
    current_courses: List[Dict]
    past_performance: Dict
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
