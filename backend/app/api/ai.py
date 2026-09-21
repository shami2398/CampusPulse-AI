"""AI Assistant API endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import uuid

from app.database import get_db
from app.models.user import User
from app.models.student import Student
from app.models.ai_conversation import AIConversation
from app.schemas.ai import AIQueryRequest, AIQueryResponse, StudyPlanRequest
from app.dependencies import get_current_active_user
from app.ai.ai_service import ai_service

router = APIRouter()


@router.post("/query", response_model=AIQueryResponse)
async def ai_query(
    query: AIQueryRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Send a query to the AI assistant"""
    
    # Get student data for context
    student = db.query(Student).filter(Student.user_id == current_user.id).first()
    student_data = {
        "gpa": student.gpa,
        "year": student.year,
        "major": student.major
    } if student else None
    
    # Generate session ID if not provided
    session_id = query.session_id or str(uuid.uuid4())
    
    # Get AI response
    ai_response = await ai_service.get_response(
        message=query.message,
        context={"type": query.context_type, "subject": query.subject_area},
        student_data=student_data
    )
    
    # Save conversation
    conversation = db.query(AIConversation).filter(
        AIConversation.session_id == session_id
    ).first()
    
    if not conversation:
        conversation = AIConversation(
            user_id=current_user.id,
            session_id=session_id,
            context_type=query.context_type,
            subject_area=query.subject_area,
            messages=[]
        )
        db.add(conversation)
    
    # Add messages
    conversation.messages.append({
        "role": "user",
        "content": query.message,
        "timestamp": datetime.utcnow().isoformat()
    })
    conversation.messages.append({
        "role": "assistant",
        "content": ai_response["response"],
        "timestamp": datetime.utcnow().isoformat()
    })
    
    conversation.total_messages = len(conversation.messages)
    conversation.last_activity = datetime.utcnow()
    
    db.commit()
    
    return AIQueryResponse(
        response=ai_response["response"],
        session_id=session_id,
        confidence=ai_response["confidence"],
        context_used=ai_response["context_used"],
        timestamp=datetime.utcnow()
    )


@router.post("/study-plan")
async def generate_study_plan(
    plan_request: StudyPlanRequest,
    current_user: User = Depends(get_current_active_user)
):
    """Generate a personalized study plan"""
    
    study_plan = await ai_service.generate_study_plan(
        subject=plan_request.subject,
        duration_weeks=plan_request.duration_weeks,
        difficulty=plan_request.difficulty_level,
        goals=plan_request.goals
    )
    
    return study_plan
