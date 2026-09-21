# CampusPulse AI - Quick Start Guide

Get CampusPulse AI running in under 10 minutes!

## Prerequisites

- Python 3.10 or higher
- Node.js 18+ and npm
- PostgreSQL 14+
- Git

## Backend Setup (5 minutes)

### 1. Clone and Navigate
```bash
git clone https://github.com/shami2398/CampusPulse-AI
cd CampusPulse-AI/backend
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database
```bash
# Create PostgreSQL database
createdb campuspulse_db

# Or using psql:
psql -U postgres -c "CREATE DATABASE campuspulse_db;"
```

### 5. Configure Environment
```bash
# Copy example env file
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac

# Edit .env and update DATABASE_URL if needed:
# DATABASE_URL=postgresql://YOUR_USER:YOUR_PASSWORD@localhost:5432/campuspulse_db
```

### 6. Initialize Database
```bash
python scripts/init_db.py
python scripts/seed_db.py
```

### 7. Start Backend Server
```bash
uvicorn app.main:app --reload --port 8000
```

✅ Backend running at **http://localhost:8000**
📚 API docs at **http://localhost:8000/docs**

## Frontend Setup (3 minutes)

### 1. Navigate to Frontend
```bash
cd ../frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Configure Environment
```bash
# Copy example env file (if exists)
# Or create .env.local with:
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
```

### 4. Start Frontend
```bash
npm run dev
```

✅ Frontend running at **http://localhost:3000**

## Login and Test

### Demo Accounts

**Student Account:**
- Email: `student1@campuspulse.edu`
- Password: `demo123`

**High-Performing Student:**
- Email: `student2@campuspulse.edu`
- Password: `demo123`

**Advisor Account:**
- Email: `advisor@campuspulse.edu`
- Password: `advisor123`

## Quick Test Checklist

1. ✅ Visit http://localhost:3000
2. ✅ Login with student1@campuspulse.edu / demo123
3. ✅ Check Dashboard - see student metrics
4. ✅ Try AI Assistant - ask "How do I learn Python?"
5. ✅ View Risk Analysis - see your risk assessment
6. ✅ Create Support Request
7. ✅ Check API docs at http://localhost:8000/docs

## Troubleshooting

### Backend Issues

**Database connection error:**
```bash
# Check PostgreSQL is running
# Windows: Check Services
# Linux: sudo systemctl status postgresql
# Mac: brew services list

# Verify database exists
psql -U postgres -l | grep campuspulse
```

**Module not found:**
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend Issues

**Port already in use:**
```bash
# Use different port
npm run dev -- -p 3001
```

**API connection error:**
- Verify backend is running on port 8000
- Check NEXT_PUBLIC_API_URL in .env.local

## Next Steps

- Read [ARCHITECTURE.md](docs/ARCHITECTURE.md) for system design
- Check [TEST_PLAN.md](docs/TEST_PLAN.md) for testing guide
- Explore API documentation at http://localhost:8000/docs

## Common Commands

```bash
# Backend
uvicorn app.main:app --reload          # Start with hot reload
python scripts/seed_db.py              # Reset demo data
pytest                                  # Run tests

# Frontend
npm run dev                             # Development server
npm run build                           # Production build
npm run lint                            # Lint code
```

## Support

For issues or questions:
1. Check the [TROUBLESHOOTING](docs/TROUBLESHOOTING.md) guide
2. Review API docs at http://localhost:8000/docs
3. Check application logs

---

**Ready to explore? Login and start using CampusPulse AI!** 🚀
