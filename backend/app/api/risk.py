"""Risk analysis API endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.user import User
from app.models.student import Student
from app.models.risk_assessment import RiskAssessment
from app.schemas.risk import RiskAnalysisRequest, RiskAssessmentResponse
from app.dependencies import get_current_active_user
from app.ml.risk_engine import RiskAnalysisEngine

router = APIRouter()
risk_engine = RiskAnalysisEngine()


@router.post("/analyze", response_model=RiskAssessmentResponse)
def analyze_student_risk(
    request: RiskAnalysisRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Perform risk analysis for a student"""
    
    # Get student data
    student = db.query(Student).filter(Student.id == request.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check authorization
    if student.user_id != current_user.id and current_user.role not in ["admin", "advisor"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    # Prepare data for analysis
    student_data = {
        "gpa": student.gpa,
        "attendance_rate": student.attendance_rate,
        "assignment_completion_rate": student.assignment_completion_rate,
        "participation_score": student.participation_score,
        "current_courses": student.current_courses,
        "year": student.year,
        "major": student.major
    }
    
    # Perform analysis
    analysis_result = risk_engine.analyze_student_risk(student_data)
    
    # Save assessment
    assessment = RiskAssessment(
        student_id=student.id,
        **analysis_result
    )
    db.add(assessment)
    db.commit()
    db.refresh(assessment)
    
    return assessment


@router.get("/assessments/me", response_model=List[RiskAssessmentResponse])
def get_my_assessments(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get current user's risk assessments"""
    
    student = db.query(Student).filter(Student.user_id == current_user.id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student profile not found")
    
    assessments = db.query(RiskAssessment).filter(
        RiskAssessment.student_id == student.id
    ).order_by(RiskAssessment.analysis_date.desc()).limit(10).all()
    
    return assessments


@router.get("/assessments/{student_id}", response_model=List[RiskAssessmentResponse])
def get_student_assessments(
    student_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get risk assessments for a specific student (admin/advisor)"""
    
    if current_user.role not in ["admin", "advisor"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    assessments = db.query(RiskAssessment).filter(
        RiskAssessment.student_id == student_id
    ).order_by(RiskAssessment.analysis_date.desc()).all()
    
    return assessments
