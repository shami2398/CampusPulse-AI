# CampusPulse AI

Production-ready AI Academic Assistant Platform for comprehensive student support, risk analysis, and early intervention.

##  Features

-  **AI Assistant** - Context-aware academic tutoring (Programming, CS, Math)
-  **Risk Analysis** - ML-powered early intervention system with pattern detection  
-  **Support Requests** - Complete ticketing system for student support
-  **Interactive Dashboard** - Real-time metrics, insights, and analytics
-  **Secure Authentication** - JWT-based access control
-  **Comprehensive Documentation** - Setup, testing, and architecture guides

##  Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 14+

### Backend Setup
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt

# Create database
createdb campuspulse_db

# Initialize and seed
python scripts/init_db.py
python scripts/seed_db.py

# Start server
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Visit **http://localhost:3000**

### Demo Credentials
- Email: `student1@campuspulse.edu`
- Password: `demo123`

##  Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Detailed setup instructions
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture and data flow
- **[TEST_PLAN.md](TEST_PLAN.md)** - Comprehensive test cases
- **[IMPLEMENTATION_REPORT.md](IMPLEMENTATION_REPORT.md)** - Technical documentation

##  Tech Stack

### Backend
- FastAPI + Python 3.10
- PostgreSQL + SQLAlchemy 2.0
- Pydantic V2 for validation
- NumPy, Pandas, scikit-learn for analytics
- JWT authentication

### Frontend
- Next.js 14 + React 18
- TypeScript + Tailwind CSS
- Zustand for state management
- Axios for API calls
- react-markdown for content rendering

##  Project Structure

```
CampusPulse-AI/
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── models/       # Database models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── core/         # Security utilities
│   │   ├── ml/           # Risk analysis engine
│   │   └── ai/           # AI service layer
│   ├── scripts/          # Database setup scripts
│   └── requirements.txt
├── frontend/
│   ├── app/              # Next.js pages
│   ├── components/       # React components
│   ├── lib/              # Utilities and API client
│   └── hooks/            # Custom React hooks
└── docs/                 # Documentation
```

##  Security

- JWT token-based authentication
- Password hashing with bcrypt
- SQL injection protection (SQLAlchemy ORM)
- CORS configuration
- Environment-based secrets management

##  Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

##  Key Components

### Risk Analysis Engine
- Pattern detection across multiple signals
- Configurable thresholds and weights
- Confidence scoring
- Trend analysis
- Early intervention triggers

### AI Assistant
- Context-aware responses
- Student-specific data integration
- Academic question answering
- Study plan generation
- Pattern-based fallback responses

### Analytics Dashboard
- Real-time student metrics
- Risk visualizations
- Performance tracking
- Workload management
- Attendance monitoring

##  Contributing

This is an academic project. For contributions:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

##  License

MIT License - See LICENSE file for details

##  Authors

Team Leader: Sai Spoorthy Eturu

Member: Hari Hansika Kommera

Member: Katakam Sahithi Rithvika

Member: Shamithri Gowravarapu

Developed as part of academic research in AI-powered student support systems.

##  Acknowledgments

- FastAPI for the excellent web framework
- Next.js team for the React framework
- PostgreSQL community
- Open-source AI/ML libraries

---

**For detailed setup instructions, see [QUICKSTART.md](QUICKSTART.md)**
