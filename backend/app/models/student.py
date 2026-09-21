"""Student model for academic data"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    student_id = Column(String, unique=True, index=True, nullable=False)
    
    # Academic info
    major = Column(String, nullable=False)
    year = Column(Integer, nullable=False)  # 1-4
    gpa = Column(Float, nullable=False)
    credits_completed = Column(Integer, default=0)
    
    # Engagement metrics
    attendance_rate = Column(Float, default=100.0)
    assignment_completion_rate = Column(Float, default=100.0)
    participation_score = Column(Float, default=0.0)
    
    # Course data (JSON)
    current_courses = Column(JSON, default=list)  # [{course_id, name, grade, credits}]
    past_performance = Column(JSON, default=dict)  # {semester: {courses, gpa}}
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="student")
    risk_assessments = relationship("RiskAssessment", back_populates="student")
