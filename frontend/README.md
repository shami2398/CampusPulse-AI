# CampusPulse AI Frontend

Next.js 14 frontend for the CampusPulse AI platform.

## Tech Stack

- **Next.js 14** - React framework with App Router
- **React 18** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Zustand** - State management
- **Axios** - API calls
- **Recharts** - Data visualization
- **react-markdown** - Markdown rendering

## Getting Started

### Install Dependencies
```bash
npm install
```

### Run Development Server
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

### Build for Production
```bash
npm run build
npm start
```

## Environment Variables

Create `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Project Structure

```
frontend/
├── app/                # Next.js App Router pages
├── components/         # React components
├── lib/               # Utilities and API client
├── hooks/             # Custom React hooks
├── types/             # TypeScript type definitions
├── public/            # Static assets
└── package.json       # Dependencies
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

## Features

- 🔐 JWT Authentication
- 📊 Interactive Dashboard
- 🤖 AI Assistant Chat Interface
- 📈 Risk Analysis Visualization
- 📝 Support Request Management
- 📱 Responsive Design

## API Integration

Frontend communicates with FastAPI backend at `http://localhost:8000/api`

All API calls use Axios with automatic token injection.

## Demo Credentials

- Student: `student1@campuspulse.edu` / `demo123`
- Advisor: `advisor@campuspulse.edu` / `advisor123`
