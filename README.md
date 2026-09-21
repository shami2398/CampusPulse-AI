# CampusPulse AI

Production-ready AI Academic Assistant Platform for student support and risk analysis.

## Features

- 🤖 **AI Assistant** - Real LLM integration (OpenAI/Anthropic) with academic tutoring
- 📊 **Risk Analysis** - ML-powered early intervention system  
- 📝 **Support Requests** - Complete ticketing system for student support
- 📈 **Dashboard** - Interactive metrics and insights
- 🔐 **Authentication** - JWT-based secure access
- 📚 **Documentation** - Complete setup and architecture guides

## Quick Start

See `QUICKSTART.md` for detailed setup instructions.

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python scripts/init_db.py
python scripts/seed_db.py
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Visit http://localhost:3000 and login with:
- Email: `student1@campuspulse.edu`
- Password: `demo123`

## Documentation

- **IMPLEMENTATION_REPORT.md** - Complete technical documentation
- **QUICKSTART.md** - Setup and deployment guide
- **TEST_PLAN.md** - Comprehensive test cases
- **ARCHITECTURE.md** - System architecture diagrams

## Tech Stack

**Backend:**
- FastAPI + Python 3.10
- PostgreSQL + SQLAlchemy
- OpenAI GPT-4 / Anthropic Claude
- NumPy, Pandas, scikit-learn

**Frontend:**
- Next.js 14 + React 18
- TypeScript + Tailwind CSS
- Zustand state management
- Axios API client

## License

MIT
