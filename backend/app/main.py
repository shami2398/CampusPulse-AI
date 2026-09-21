"""
FastAPI application entry point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine, Base

# Import routers
from app.api import auth, students, risk, support, ai

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CampusPulse AI API",
    description="AI-powered academic assistant and student support platform",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(students.router, prefix="/api/students", tags=["Students"])
app.include_router(risk.router, prefix="/api/risk", tags=["Risk Analysis"])
app.include_router(support.router, prefix="/api/support", tags=["Support"])
app.include_router(ai.router, prefix="/api/ai", tags=["AI Assistant"])


@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "CampusPulse AI API",
        "version": "1.0.0",
        "status": "operational"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
