# PathFinder Backend API

FastAPI backend for PathFinder - Career exploration app for Louisiana 8th graders.

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Create `.env` file:**
```bash
cp .env.example .env
# Edit .env with your actual credentials
```

3. **Run database migrations:**
```bash
alembic upgrade head
```

4. **Start development server:**
```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`

## API Documentation

- OpenAPI docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Database Schema

- **users**: User profiles, Interest DNA, engagement scores
- **careers**: Career information (title, industry, salary, education)
- **videos**: Career videos (Vercel Blob URLs)
- **engagement**: User interactions (watched, liked, saved, skipped, shared)
- **recommendations**: AI-generated career recommendations

## Deployment

Deployed to Render with auto-deploy from GitHub `main` branch.

Production URL: `https://pathfinder-api.onrender.com`
