"""Seed database with demo data"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.models.student import Student
from app.core.security import get_password_hash


def seed_database():
    """Seed database with demo users and data"""
    db: Session = SessionLocal()
    
    try:
        print("Seeding database with demo data...")
        
        # Check if demo users already exist
        existing = db.query(User).filter(User.email == "student1@campuspulse.edu").first()
        if existing:
            print("Demo data already exists. Skipping...")
            return
        
        # Create demo students
        demo_users = [
            {
                "email": "student1@campuspulse.edu",
                "password": "demo123",
                "full_name": "Alex Johnson",
                "role": "student",
                "student_data": {
                    "student_id": "CS2024001",
                    "major": "Computer Science",
                    "year": 3,
                    "gpa": 3.2,
                    "credits_completed": 75,
                    "attendance_rate": 85.0,
                    "assignment_completion_rate": 78.0,
                    "participation_score": 70.0,
                    "current_courses": [
                        {"course_id": "CS301", "name": "Algorithms", "grade": "B", "credits": 3},
                        {"course_id": "CS350", "name": "Database Systems", "grade": "B+", "credits": 3},
                        {"course_id": "MATH310", "name": "Discrete Math", "grade": "C+", "credits": 3}
                    ]
                }
            },
            {
                "email": "student2@campuspulse.edu",
                "password": "demo123",
                "full_name": "Sarah Martinez",
                "role": "student",
                "student_data": {
                    "student_id": "CS2024002",
                    "major": "Computer Science",
                    "year": 2,
                    "gpa": 3.8,
                    "credits_completed": 45,
                    "attendance_rate": 95.0,
                    "assignment_completion_rate": 98.0,
                    "participation_score": 90.0,
                    "current_courses": [
                        {"course_id": "CS201", "name": "Data Structures", "grade": "A", "credits": 4},
                        {"course_id": "CS250", "name": "Web Development", "grade": "A-", "credits": 3}
                    ]
                }
            }
        ]
        
        # Create advisor
        advisor = User(
            email="advisor@campuspulse.edu",
            hashed_password=get_password_hash("advisor123"),
            full_name="Dr. Emily Chen",
            role="advisor"
        )
        db.add(advisor)
        
        # Create users and students
        for user_data in demo_users:
            user = User(
                email=user_data["email"],
                hashed_password=get_password_hash(user_data["password"]),
                full_name=user_data["full_name"],
                role=user_data["role"]
            )
            db.add(user)
            db.flush()  # Get user ID
            
            # Create student profile
            student = Student(
                user_id=user.id,
                **user_data["student_data"]
            )
            db.add(student)
        
        db.commit()
        
        print("✅ Database seeded successfully!")
        print("\n🔐 Demo Credentials:")
        print("Student 1:")
        print("  Email: student1@campuspulse.edu")
        print("  Password: demo123")
        print("\nStudent 2:")
        print("  Email: student2@campuspulse.edu")
        print("  Password: demo123")
        print("\nAdvisor:")
        print("  Email: advisor@campuspulse.edu")
        print("  Password: advisor123")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
