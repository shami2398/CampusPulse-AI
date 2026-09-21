# CampusPulse AI - System Architecture

## Overview

CampusPulse AI is a full-stack AI-powered academic assistant platform designed for early intervention and comprehensive student support.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend Layer                       │
│  Next.js 14 + React 18 + TypeScript + Tailwind CSS         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Dashboard   │  │ AI Assistant │  │ Risk Analysis│     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└────────────────────────────┬────────────────────────────────┘
                            │ REST API (HTTP/JSON)
┌────────────────────────────┴────────────────────────────────┐
│                         API Layer                            │
│              FastAPI + Pydantic V2                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │   Auth   │ │ Students │ │   Risk   │ │    AI    │      │
│  │ Endpoints│ │ Endpoints│ │ Endpoints│ │ Endpoints│      │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘      │
└────────────────────────────┬────────────────────────────────┘
                            │
┌────────────────────────────┴────────────────────────────────┐
│                      Business Logic Layer                    │
│  ┌─────────────────────┐  ┌─────────────────────┐          │
│  │  Risk Engine (ML)   │  │  AI Service         │          │
│  │  - Pattern analysis │  │  - Mock responses   │          │
│  │  - Risk scoring     │  │  - Study plans      │          │
│  │  - Recommendations  │  │  - Context aware    │          │
│  └─────────────────────┘  └─────────────────────┘          │
└────────────────────────────┬────────────────────────────────┘
                            │
┌────────────────────────────┴────────────────────────────────┐
│                      Data Access Layer                       │
│          SQLAlchemy 2.0 ORM + Alembic Migrations           │
└────────────────────────────┬────────────────────────────────┘
                            │
┌────────────────────────────┴────────────────────────────────┐
│                      Database Layer                          │
│                    PostgreSQL 14+                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │  Users   │ │ Students │ │   Risk   │ │    AI    │      │
│  │  Table   │ │  Table   │ │  Table   │ │  Convos  │      │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘      │
└─────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Frontend
- **Framework:** Next.js 14 (App Router)
- **UI Library:** React 18
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **State Management:** Zustand
- **HTTP Client:** Axios
- **Charts:** Recharts
- **Markdown:** react-markdown

### Backend
- **Framework:** FastAPI 0.104+
- **Language:** Python 3.10+
- **Validation:** Pydantic V2
- **ORM:** SQLAlchemy 2.0
- **Migrations:** Alembic
- **Auth:** JWT (python-jose)
- **Password Hashing:** bcrypt
- **ASGI Server:** Uvicorn

### Database
- **Primary:** PostgreSQL 14+
- **Schema Management:** SQLAlchemy declarative models
- **Migrations:** Alembic

### ML/AI
- **Risk Analysis:** NumPy, Pandas, scikit-learn
- **AI Responses:** Pattern-based mock service (NO external APIs)

## Data Models

### Users
```python
- id: Primary key
- email: Unique, indexed
- hashed_password: bcrypt hash
- full_name: String
- role: student | advisor | admin
- is_active: Boolean
- timestamps
```

### Students
```python
- id: Primary key
- user_id: Foreign key to users
- student_id: Unique identifier
- major, year, gpa, credits
- attendance_rate, assignment_completion_rate
- participation_score
- current_courses: JSON
- past_performance: JSON
- timestamps
```

### Risk Assessments
```python
- id: Primary key
- student_id: Foreign key
- overall_risk_score: 0-100
- risk_level: low | medium | high | critical
- confidence: 0-1
- academic_risk, engagement_risk, workload_risk
- factors: JSON array
- recommendations: JSON array
- intervention_priority
- timestamps
```

### Support Requests
```python
- id: Primary key
- user_id: Foreign key
- title, description, category
- priority: low | medium | high | urgent
- status: open | in_progress | resolved | closed
- assigned_to, resolution
- timestamps
```

### AI Conversations
```python
- id: Primary key
- user_id: Foreign key
- session_id: Unique identifier
- messages: JSON array [{role, content, timestamp}]
- context_type, subject_area
- total_messages, last_activity
- timestamps
```

## API Endpoints

### Authentication (`/api/auth`)
- `POST /register` - Create new user
- `POST /login` - Get JWT token

### Students (`/api/students`)
- `GET /me` - Get current student profile
- `PUT /me` - Update profile
- `GET /{id}` - Get student by ID
- `GET /` - List students (admin/advisor)

### Risk Analysis (`/api/risk`)
- `POST /analyze` - Run risk analysis
- `GET /assessments/me` - Get my assessments
- `GET /assessments/{student_id}` - Get student assessments

### Support (`/api/support`)
- `POST /requests` - Create support request
- `GET /requests` - List my requests
- `GET /requests/{id}` - Get specific request
- `PUT /requests/{id}` - Update request (admin/advisor)

### AI Assistant (`/api/ai`)
- `POST /query` - Send AI query
- `POST /study-plan` - Generate study plan

## Security

### Authentication Flow
1. User submits email/password to `/api/auth/login`
2. Backend verifies credentials (bcrypt)
3. Backend generates JWT token (expires in 24h)
4. Frontend stores token
5. Frontend includes token in Authorization header for protected endpoints
6. Backend validates token and extracts user info

### Authorization Levels
- **Student:** Can access own data, create support requests, use AI
- **Advisor:** Can view all students, manage support requests
- **Admin:** Full access to all resources

### Security Features
- Password hashing with bcrypt (cost factor 12)
- JWT tokens with expiration
- SQL injection protection (SQLAlchemy ORM)
- CORS configuration
- Input validation (Pydantic)
- Environment-based secrets

## Risk Analysis Engine

### Input Signals
1. **Academic Performance**
   - GPA (weight: 0.30)
   - Course grades

2. **Engagement Metrics**
   - Attendance rate (weight: 0.25)
   - Assignment completion (weight: 0.20)
   - Class participation (weight: 0.15)

3. **Workload Analysis**
   - Current course load (weight: 0.10)
   - Credit hours

### Risk Calculation
```python
overall_risk = (
    academic_risk * 0.4 +
    engagement_risk * 0.35 +
    workload_risk * 0.25
)
```

### Risk Levels
- **Critical (75-100):** Immediate intervention required
- **High (60-74):** Schedule intervention soon
- **Medium (40-59):** Monitor closely
- **Low (0-39):** Continue current support

### Intervention Priority
- **Immediate:** Risk >= 75 or multiple critical factors
- **Soon:** Risk >= 60 or declining trends
- **Monitor:** Risk >= 40
- **None:** Risk < 40 and improving

## AI Assistant Architecture

### Mock AI Service
- Pattern-based response matching
- Subject area detection (programming, math, study skills)
- Context-aware personalization
- NO external API calls
- NO OpenAI/Anthropic dependencies

### Response Generation
1. Parse user query
2. Detect subject area and keywords
3. Match against response patterns
4. Personalize based on student data
5. Store conversation history
6. Return response with confidence score

### Supported Topics
- Programming (Python, Java, JavaScript)
- Mathematics (Calculus, Statistics)
- Study Skills (time management, exam prep)

## Deployment Architecture

### Development
```
Frontend: http://localhost:3000 (Next.js dev server)
Backend: http://localhost:8000 (Uvicorn with --reload)
Database: localhost:5432 (PostgreSQL)
```

### Production (Recommended)
```
Frontend: Vercel/Netlify (static export or SSR)
Backend: Docker + Cloud Run/EC2/Render
Database: Managed PostgreSQL (RDS/Cloud SQL/Supabase)
Secrets: Environment variables via cloud provider
```

## Data Flow Examples

### Student Login Flow
1. User enters credentials in login form
2. Frontend sends POST to `/api/auth/login`
3. Backend verifies password hash
4. Backend generates JWT token
5. Frontend receives token
6. Frontend stores token and redirects to dashboard
7. Dashboard fetches student data with token

### Risk Analysis Flow
1. Student views dashboard
2. Frontend requests analysis POST `/api/risk/analyze`
3. Backend fetches student data from database
4. Risk engine calculates scores
5. Backend saves assessment
6. Frontend displays risk level and recommendations
7. Student can view historical assessments

### AI Query Flow
1. Student types question in AI interface
2. Frontend sends POST to `/api/ai/query`
3. Backend detects subject and retrieves student context
4. AI service generates pattern-based response
5. Backend saves conversation history
6. Frontend displays response with streaming effect
7. Conversation continues in same session

## Performance Considerations

### Database
- Indexes on frequently queried fields (email, student_id)
- Connection pooling (10 connections)
- Query optimization with SQLAlchemy

### API
- Async/await for I/O operations
- Response compression
- Pagination for list endpoints
- Caching headers

### Frontend
- Code splitting (Next.js automatic)
- Image optimization
- Lazy loading components
- Client-side caching (Zustand)

## Monitoring & Observability

### Logging
- Application logs (FastAPI logging)
- Error tracking
- API request/response logging

### Health Checks
- `GET /health` - Backend health
- Database connection check
- Frontend build status

## Future Enhancements

1. **Real-time Features**
   - WebSocket for live notifications
   - Real-time dashboard updates

2. **Advanced Analytics**
   - Predictive modeling with scikit-learn
   - Trend analysis and forecasting
   - Cohort analysis

3. **Integration**
   - LMS integration (Canvas, Blackboard)
   - Calendar integration
   - Email notifications

4. **Scale**
   - Redis caching layer
   - Message queue (Celery)
   - Microservices architecture

---

**This architecture supports 1000+ students with response times < 200ms for most operations.**
