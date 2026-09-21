"""Support request schemas"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class SupportPriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"


class SupportStatusEnum(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"


class SupportRequestBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1)
    category: str
    priority: SupportPriorityEnum = SupportPriorityEnum.medium


class SupportRequestCreate(SupportRequestBase):
    pass


class SupportRequestUpdate(BaseModel):
    status: Optional[SupportStatusEnum] = None
    assigned_to: Optional[str] = None
    resolution: Optional[str] = None


class SupportRequestResponse(SupportRequestBase):
    id: int
    user_id: int
    status: SupportStatusEnum
    assigned_to: Optional[str]
    resolution: Optional[str]
    resolved_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
