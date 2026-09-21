"""Initialize database with tables"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import engine, Base
from app.models import User, Student, RiskAssessment, SupportRequest, AIConversation

def init_database():
    """Create all database tables"""
    print("Creating database tables...")
    
    Base.metadata.create_all(bind=engine)
    
    print("✅ Database tables created successfully!")
    print("\nCreated tables:")
    print("- users")
    print("- students")
    print("- risk_assessments")
    print("- support_requests")
    print("- ai_conversations")


if __name__ == "__main__":
    init_database()
