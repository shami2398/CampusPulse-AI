"""Risk assessment model"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class RiskAssessment(Base):
    __tablename__ = "risk_assessments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    
    # Risk metrics
    overall_risk_score = Column(Float, nullable=False)  # 0-100
    risk_level = Column(String, nullable=False)  # low, medium, high, critical
    confidence = Column(Float, nullable=False)  # 0-1
    
    # Individual risk factors
    academic_risk = Column(Float, nullable=False)
    engagement_risk = Column(Float, nullable=False)
    workload_risk = Column(Float, nullable=False)
    
    # Detailed analysis
    factors = Column(JSON, default=list)  # [{factor, score, weight, description}]
    recommendations = Column(JSON, default=list)  # [recommendation strings]
    intervention_priority = Column(String, nullable=False)  # immediate, soon, monitor, none
    
    # Analysis metadata
    analysis_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    student = relationship("Student", back_populates="risk_assessments")
