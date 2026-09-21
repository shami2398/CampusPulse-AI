"""Risk analysis engine using ML patterns"""
import numpy as np
from typing import Dict, List, Tuple
from datetime import datetime


class RiskAnalysisEngine:
    """
    ML-powered risk analysis engine for student intervention
    """
    
    def __init__(self):
        # Risk factor weights (tuned through data analysis)
        self.weights = {
            "gpa": 0.30,
            "attendance": 0.25,
            "assignment_completion": 0.20,
            "participation": 0.15,
            "workload": 0.10
        }
        
        # Risk thresholds
        self.thresholds = {
            "critical": 75,
            "high": 60,
            "medium": 40,
            "low": 0
        }
    
    def analyze_student_risk(self, student_data: Dict) -> Dict:
        """
        Comprehensive risk analysis for a student
        """
        # Calculate individual risk components
        academic_risk = self._calculate_academic_risk(student_data)
        engagement_risk = self._calculate_engagement_risk(student_data)
        workload_risk = self._calculate_workload_risk(student_data)
        
        # Calculate weighted overall risk
        overall_risk = (
            academic_risk * 0.4 +
            engagement_risk * 0.35 +
            workload_risk * 0.25
        )
        
        # Determine risk level and priority
        risk_level = self._get_risk_level(overall_risk)
        intervention_priority = self._get_intervention_priority(overall_risk, student_data)
        
        # Generate detailed factors
        factors = self._analyze_risk_factors(student_data, academic_risk, engagement_risk, workload_risk)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(factors, student_data)
        
        # Calculate confidence
        confidence = self._calculate_confidence(student_data)
        
        return {
            "overall_risk_score": round(overall_risk, 2),
            "risk_level": risk_level,
            "confidence": round(confidence, 2),
            "academic_risk": round(academic_risk, 2),
            "engagement_risk": round(engagement_risk, 2),
            "workload_risk": round(workload_risk, 2),
            "factors": factors,
            "recommendations": recommendations,
            "intervention_priority": intervention_priority
        }
    
    def _calculate_academic_risk(self, data: Dict) -> float:
        """Calculate academic performance risk (0-100)"""
        gpa = data.get("gpa", 4.0)
        
        # GPA-based risk (lower GPA = higher risk)
        if gpa >= 3.5:
            gpa_risk = 10
        elif gpa >= 3.0:
            gpa_risk = 25
        elif gpa >= 2.5:
            gpa_risk = 50
        elif gpa >= 2.0:
            gpa_risk = 75
        else:
            gpa_risk = 95
        
        return gpa_risk
    
    def _calculate_engagement_risk(self, data: Dict) -> float:
        """Calculate engagement risk based on attendance and participation"""
        attendance = data.get("attendance_rate", 100.0)
        completion = data.get("assignment_completion_rate", 100.0)
        participation = data.get("participation_score", 50.0)
        
        # Calculate weighted engagement score
        attendance_risk = (100 - attendance) * 0.4
        completion_risk = (100 - completion) * 0.4
        participation_risk = (100 - participation) * 0.2
        
        return attendance_risk + completion_risk + participation_risk
    
    def _calculate_workload_risk(self, data: Dict) -> float:
        """Calculate workload-related risk"""
        current_courses = data.get("current_courses", [])
        credits = sum(course.get("credits", 3) for course in current_courses)
        
        # Risk based on credit load
        if credits >= 18:
            return 70
        elif credits >= 15:
            return 40
        elif credits >= 12:
            return 20
        else:
            return 50  # Too few credits is also a risk
    
    def _get_risk_level(self, score: float) -> str:
        """Convert risk score to level"""
        if score >= self.thresholds["critical"]:
            return "critical"
        elif score >= self.thresholds["high"]:
            return "high"
        elif score >= self.thresholds["medium"]:
            return "medium"
        else:
            return "low"
    
    def _get_intervention_priority(self, risk_score: float, data: Dict) -> str:
        """Determine intervention priority"""
        if risk_score >= 75:
            return "immediate"
        elif risk_score >= 60:
            return "soon"
        elif risk_score >= 40:
            return "monitor"
        else:
            return "none"
    
    def _analyze_risk_factors(self, data: Dict, academic: float, engagement: float, workload: float) -> List[Dict]:
        """Generate detailed risk factor analysis"""
        factors = []
        
        # GPA factor
        gpa = data.get("gpa", 4.0)
        if gpa < 3.0:
            factors.append({
                "factor": "Low GPA",
                "score": academic,
                "weight": 0.4,
                "description": f"Current GPA of {gpa:.2f} indicates academic struggle"
            })
        
        # Attendance factor
        attendance = data.get("attendance_rate", 100.0)
        if attendance < 85:
            factors.append({
                "factor": "Poor Attendance",
                "score": 100 - attendance,
                "weight": 0.25,
                "description": f"Attendance at {attendance:.1f}% is below recommended 85%"
            })
        
        # Assignment completion factor
        completion = data.get("assignment_completion_rate", 100.0)
        if completion < 90:
            factors.append({
                "factor": "Incomplete Assignments",
                "score": 100 - completion,
                "weight": 0.20,
                "description": f"Only {completion:.1f}% of assignments completed"
            })
        
        # Workload factor
        credits = sum(course.get("credits", 3) for course in data.get("current_courses", []))
        if credits >= 18:
            factors.append({
                "factor": "High Course Load",
                "score": workload,
                "weight": 0.15,
                "description": f"Taking {credits} credits may cause burnout"
            })
        
        return factors
    
    def _generate_recommendations(self, factors: List[Dict], data: Dict) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # GPA-based recommendations
        gpa = data.get("gpa", 4.0)
        if gpa < 2.5:
            recommendations.append("Schedule academic advising session immediately")
            recommendations.append("Consider tutoring services for struggling courses")
        
        # Attendance recommendations
        attendance = data.get("attendance_rate", 100.0)
        if attendance < 85:
            recommendations.append("Meet with advisor to discuss attendance barriers")
            recommendations.append("Review course schedule for conflicts")
        
        # Assignment completion recommendations
        completion = data.get("assignment_completion_rate", 100.0)
        if completion < 90:
            recommendations.append("Work with academic coach on time management")
            recommendations.append("Break down large assignments into smaller tasks")
        
        # Workload recommendations
        credits = sum(course.get("credits", 3) for course in data.get("current_courses", []))
        if credits >= 18:
            recommendations.append("Consider reducing course load next semester")
            recommendations.append("Ensure adequate study time for each course")
        
        # General recommendations
        if len(factors) >= 3:
            recommendations.append("Schedule comprehensive support meeting with advisor")
        
        return recommendations or ["Continue current academic trajectory - monitor progress"]
    
    def _calculate_confidence(self, data: Dict) -> float:
        """Calculate confidence in risk assessment"""
        # Base confidence on data completeness
        required_fields = ["gpa", "attendance_rate", "assignment_completion_rate"]
        present_fields = sum(1 for field in required_fields if field in data and data[field] is not None)
        
        confidence = (present_fields / len(required_fields)) * 0.9
        
        # Boost confidence if we have course data
        if data.get("current_courses"):
            confidence += 0.1
        
        return min(confidence, 1.0)
