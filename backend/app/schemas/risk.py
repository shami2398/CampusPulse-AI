"""Risk assessment schemas"""
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime


class RiskFactor(BaseModel):
    factor: str
    score: float
    weight: float
    description: str


class RiskAssessmentBase(BaseModel):
    overall_risk_score: float
    risk_level: str
    confidence: float
    academic_risk: float
    engagement_risk: float
    workload_risk: float


class RiskAssessmentCreate(RiskAssessmentBase):
    student_id: int
    factors: List[Dict]
    recommendations: List[str]
    intervention_priority: str


class RiskAssessmentResponse(RiskAssessmentBase):
    id: int
    student_id: int
    factors: List[Dict]
    recommendations: List[str]
    intervention_priority: str
    analysis_date: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class RiskAnalysisRequest(BaseModel):
    student_id: int
    include_recommendations: bool = True
