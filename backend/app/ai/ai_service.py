"""
AI service - Mock/Pattern-based responses ONLY (NO OpenAI)
"""
import re
from typing import Dict, List, Optional
from datetime import datetime


class AIService:
    """Mock AI assistant with pattern-based responses"""
    
    def __init__(self):
        self.patterns = self._load_patterns()
    
    def _load_patterns(self) -> Dict:
        """Load response patterns for common questions"""
        return {
            "programming": {
                "python": [
                    "Python is a great language for beginners! Start with variables, data types, and control flow.",
                    "For Python, I recommend practicing with small projects and using the official documentation.",
                    "Python's syntax is clean and readable. Focus on understanding functions and classes first."
                ],
                "java": [
                    "Java is object-oriented. Master classes, inheritance, and polymorphism.",
                    "Java requires understanding of types. Practice with simple OOP projects.",
                    "Start with basic syntax, then move to collections and exception handling."
                ],
                "javascript": [
                    "JavaScript is essential for web development. Learn ES6+ features.",
                    "Practice with DOM manipulation and async programming (promises, async/await).",
                    "Understanding closures and scope is crucial for JavaScript mastery."
                ]
            },
            "math": {
                "calculus": [
                    "Calculus builds on algebra. Master derivatives and integrals step by step.",
                    "Practice limits first, then derivatives, then integrals. Work through examples daily.",
                    "Khan Academy and Paul's Online Math Notes are excellent calculus resources."
                ],
                "statistics": [
                    "Statistics requires understanding probability distributions and hypothesis testing.",
                    "Focus on descriptive statistics first, then inferential statistics.",
                    "Practice with real datasets to understand statistical concepts better."
                ]
            },
            "study": {
                "time_management": [
                    "Use the Pomodoro Technique: 25 minutes of focused work, 5 minute breaks.",
                    "Create a weekly schedule allocating specific time blocks for each subject.",
                    "Prioritize tasks using the Eisenhower Matrix (urgent/important)."
                ],
                "exam_prep": [
                    "Start studying at least one week before exams. Review notes daily.",
                    "Create practice tests and work through past papers.",
                    "Form study groups to discuss difficult concepts with peers."
                ]
            }
        }
    
    async def get_response(
        self,
        message: str,
        context: Optional[Dict] = None,
        student_data: Optional[Dict] = None
    ) -> Dict:
        """Generate response using pattern matching"""
        
        message_lower = message.lower()
        
        # Detect subject area
        subject = self._detect_subject(message_lower)
        
        # Get relevant response
        response_text = self._get_pattern_response(subject, message_lower)
        
        # Add context if available
        if student_data:
            response_text = self._personalize_response(response_text, student_data)
        
        return {
            "response": response_text,
            "confidence": 0.75,
            "subject_detected": subject,
            "context_used": bool(student_data)
        }
    
    def _detect_subject(self, message: str) -> str:
        """Detect subject area from message"""
        if any(word in message for word in ["python", "java", "javascript", "code", "programming", "function", "class"]):
            return "programming"
        elif any(word in message for word in ["calculus", "derivative", "integral", "math", "algebra", "statistics"]):
            return "math"
        elif any(word in message for word in ["study", "exam", "test", "prepare", "time management"]):
            return "study"
        else:
            return "general"
    
    def _get_pattern_response(self, subject: str, message: str) -> str:
        """Get response based on patterns"""
        
        # Programming responses
        if "python" in message:
            return self.patterns["programming"]["python"][0]
        elif "java" in message:
            return self.patterns["programming"]["java"][0]
        elif "javascript" in message:
            return self.patterns["programming"]["javascript"][0]
        
        # Math responses
        elif "calculus" in message:
            return self.patterns["math"]["calculus"][0]
        elif "statistics" in message or "stats" in message:
            return self.patterns["math"]["statistics"][0]
        
        # Study tips
        elif "time management" in message or "organize" in message:
            return self.patterns["study"]["time_management"][0]
        elif "exam" in message or "test" in message:
            return self.patterns["study"]["exam_prep"][0]
        
        # Default response
        else:
            return ("I can help with programming (Python, Java, JavaScript), "
                   "mathematics (Calculus, Statistics), and study strategies. "
                   "What would you like to know more about?")
    
    def _personalize_response(self, response: str, student_data: Dict) -> str:
        """Add personalization based on student data"""
        gpa = student_data.get("gpa", 0)
        
        if gpa < 2.5:
            response += "\n\nI notice you might be facing some academic challenges. Would you like specific study strategies?"
        elif gpa >= 3.5:
            response += "\n\nYou're doing great academically! Keep up the excellent work."
        
        return response
    
    async def generate_study_plan(
        self,
        subject: str,
        duration_weeks: int,
        difficulty: str,
        goals: Optional[List[str]] = None
    ) -> Dict:
        """Generate a study plan"""
        
        weeks = []
        topics_per_week = 3 if difficulty == "beginner" else 4
        
        for week_num in range(1, duration_weeks + 1):
            week = {
                "week": week_num,
                "topics": [f"{subject} Topic {week_num}.{i}" for i in range(1, topics_per_week + 1)],
                "activities": [
                    "Read course materials",
                    "Complete practice exercises",
                    "Review and summarize key concepts"
                ],
                "estimated_hours": 8 + (2 if difficulty == "advanced" else 0)
            }
            weeks.append(week)
        
        return {
            "subject": subject,
            "duration_weeks": duration_weeks,
            "difficulty": difficulty,
            "weeks": weeks,
            "total_estimated_hours": sum(w["estimated_hours"] for w in weeks),
            "recommendations": [
                "Set aside dedicated study time each day",
                "Review previous week's material before starting new topics",
                "Practice regularly with exercises and problems"
            ]
        }


# Global instance
ai_service = AIService()
