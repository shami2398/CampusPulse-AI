"""Support request API endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database import get_db
from app.models.user import User
from app.models.support_request import SupportRequest
from app.schemas.support import SupportRequestCreate, SupportRequestResponse, SupportRequestUpdate
from app.dependencies import get_current_active_user

router = APIRouter()


@router.post("/requests", response_model=SupportRequestResponse, status_code=status.HTTP_201_CREATED)
def create_support_request(
    request_data: SupportRequestCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a new support request"""
    support_request = SupportRequest(
        user_id=current_user.id,
        **request_data.model_dump()
    )
    db.add(support_request)
    db.commit()
    db.refresh(support_request)
    return support_request


@router.get("/requests", response_model=List[SupportRequestResponse])
def list_my_requests(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get current user's support requests"""
    requests = db.query(SupportRequest).filter(
        SupportRequest.user_id == current_user.id
    ).order_by(SupportRequest.created_at.desc()).all()
    return requests


@router.get("/requests/{request_id}", response_model=SupportRequestResponse)
def get_support_request(
    request_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get a specific support request"""
    support_request = db.query(SupportRequest).filter(
        SupportRequest.id == request_id
    ).first()
    
    if not support_request:
        raise HTTPException(status_code=404, detail="Support request not found")
    
    # Check authorization
    if support_request.user_id != current_user.id and current_user.role not in ["admin", "advisor"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    return support_request


@router.put("/requests/{request_id}", response_model=SupportRequestResponse)
def update_support_request(
    request_id: int,
    update_data: SupportRequestUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update a support request (admin/advisor only)"""
    if current_user.role not in ["admin", "advisor"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    support_request = db.query(SupportRequest).filter(
        SupportRequest.id == request_id
    ).first()
    
    if not support_request:
        raise HTTPException(status_code=404, detail="Support request not found")
    
    # Update fields
    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(support_request, field, value)
    
    if update_data.status == "resolved" and not support_request.resolved_at:
        support_request.resolved_at = datetime.utcnow()
    
    db.commit()
    db.refresh(support_request)
    return support_request
