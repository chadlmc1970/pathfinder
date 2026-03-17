# PathFinder Backend - Claude 1 Recovery Prompt

**Role:** You are the Backend Lead for PathFinder MVP - a TikTok-style career exploration iOS app for Louisiana 8th graders.

---

## Project Structure

```
/Users/I870089/pathfinder/
├── backend/              # FastAPI Python API (YOUR RESPONSIBILITY)
├── mobile/               # Expo/React Native iOS app (Claude 2 or UI Expert)
├── admin-dashboard/      # Next.js 16 admin panel (Claude 2 or UI Expert)
├── STATUS.md             # Current status
├── SESSION.md            # Full project context (716 lines)
└── RECOVERY_PROMPT.md    # This file
```

---

## Critical Deployment Rules

### ⚠️ NEVER USE LOCALHOST ⚠️
- **Production Backend:** `https://pathfinder-api.onrender.com`
- **Production Database:** Neon PostgreSQL (connection string in `.env`)
- **Git Remote:** https://github.com/chadlmc1970/pathfinder.git
- **Branch:** `main` triggers auto-deploy on Render

### Deployment Workflow
1. Make changes in `/Users/I870089/pathfinder/backend/`
2. `git add -A && git commit -m "description"`
3. `git push origin main` → triggers Render auto-deploy (~2 min)
4. Test on `https://pathfinder-api.onrender.com` (NOT localhost)

---

## Tech Stack

**Backend:**
- FastAPI (Python 3.11)
- SQLAlchemy ORM + Alembic migrations
- Neon PostgreSQL database
- Anthropic Claude 4.6 for AI recommendations
- Pydantic v2 for schemas

**Database:**
- Provider: Neon PostgreSQL
- Connection: In `/Users/I870089/pathfinder/backend/.env`
- Migrations: `/Users/I870089/pathfinder/backend/alembic/`

**Deployment:**
- Platform: Render
- Config: `/Users/I870089/pathfinder/render.yaml`
- Auto-deploys on push to `main`

---

## What's Been Completed (100%)

### ✅ Database Schema
Located in `/Users/I870089/pathfinder/backend/app/models/`:
- `career.py` - Career profiles (title, description, salary, skills, pathway)
- `video.py` - Video metadata (blob_url, thumbnail, duration, transcript)
- `user.py` - User accounts (email, grade_level, school, preferences)
- `engagement.py` - Swipe events (user_id, career_id, action, timestamp)
- `recommendation.py` - AI recommendations (user_id, career_id, score, reasoning)

### ✅ Pydantic Schemas
Located in `/Users/I870089/pathfinder/backend/app/schemas/`:
- All models have Create/Update/Response schemas
- **IMPORTANT FIX:** `career.py` line 13: `skills: Optional[List[str]] = None` (was Dict, changed to List to match seed data)

### ✅ API Endpoints
Located in `/Users/I870089/pathfinder/backend/app/api/v1/`:

**Careers** (`careers.py`):
- `GET /api/v1/careers/` - List all (supports ?industry filter)
- `GET /api/v1/careers/{id}` - Get single career
- `POST /api/v1/careers/` - Create career
- `PUT /api/v1/careers/{id}` - Update career
- `DELETE /api/v1/careers/{id}` - Delete career

**Videos** (`videos.py`):
- `GET /api/v1/videos/` - List all (supports ?career_id filter)
- `GET /api/v1/videos/{id}` - Get single video
- `POST /api/v1/videos/` - Create video
- Full CRUD implemented

**Users** (`users.py`):
- `GET /api/v1/users/` - List all
- `GET /api/v1/users/{id}` - Get single user
- `POST /api/v1/users/` - Create user (validates unique email)
- Full CRUD implemented

**Engagement** (`engagement.py`):
- `GET /api/v1/engagement/` - List events (supports ?user_id and ?career_id filters)
- `POST /api/v1/engagement/` - Record swipe event (like/skip/save/share)

**Recommendations** (`recommendations.py`):
- `GET /api/v1/recommendations/?user_id={id}` - Get recommendations for user
- `POST /api/v1/recommendations/generate?user_id={id}&limit=10` - **AI-powered generation** (Claude 4.6)
- `POST /api/v1/recommendations/` - Create recommendation (manual)
- `PUT /api/v1/recommendations/{id}/clicked` - Mark as clicked

### ✅ Seed Data
File: `/Users/I870089/pathfinder/backend/seed_data.py`

**20 Louisiana Careers Seeded:**
1. Petroleum Engineer - $85k-$150k (Energy)
2. Chef / Culinary Artist - $35k-$75k (Hospitality)
3. Marine Biologist - $50k-$95k (Science)
4. Nurse Practitioner - $95k-$130k (Healthcare)
5. Port Operations Manager - $60k-$110k (Logistics)
6. Oil Rig Technician - $55k-$95k (Energy)
7. Jazz Musician - $30k-$80k (Arts)
8. Coastal Restoration Engineer - $65k-$105k (Environment)
9. Casino Dealer - $25k-$50k (Gaming)
10. Fisheries Manager - $55k-$90k (Agriculture)
11. Chemical Plant Operator - $60k-$95k (Manufacturing)
12. Tourism Marketing Specialist - $45k-$75k (Hospitality)
13. Paramedic - $40k-$65k (Healthcare)
14. Electrician - $45k-$80k (Skilled Trades)
15. Video Game Developer - $60k-$120k (Technology)
16. Shrimp Boat Captain - $40k-$85k (Agriculture)
17. Elementary School Teacher - $45k-$65k (Education)
18. Wildlife Biologist - $50k-$85k (Science)
19. Cybersecurity Analyst - $75k-$130k (Technology)
20. Construction Manager - $70k-$120k (Construction)

**5 Placeholder Videos:**
- IDs 1-5 linked to career IDs 21-25
- Placeholder URLs (need real Louisiana career videos)

### ✅ Configuration Files
- `/Users/I870089/pathfinder/backend/.env` - Database connection, API keys
- `/Users/I870089/pathfinder/backend/app/core/config.py` - Settings management
- `/Users/I870089/pathfinder/render.yaml` - Render deployment config
- `/Users/I870089/pathfinder/backend/alembic.ini` - Migration config

### ✅ Recent Fixes (March 17, 2026)
- **Commit c15e693:** Fixed `career.py` schema - changed `skills` from `Dict` to `List[str]`
- **Reason:** Seed data has skills as array `["Math", "Physics"]`, not dict `{"technical": [...], "soft": [...]}`
- **Result:** `GET /api/v1/careers/` now returns valid JSON (was throwing 500 error)
- **Commit e8c62c6:** Added AI-powered recommendations engine with Claude 4.6
- **Result:** `POST /api/v1/recommendations/generate` now generates personalized career matches

### ✅ AI Recommendations Engine (COMPLETE - March 17, 2026)
**File:** `/Users/I870089/pathfinder/backend/app/api/v1/recommendations.py`

**Endpoint:** `POST /api/v1/recommendations/generate?user_id={id}&limit=10`

**Algorithm:**
1. **Analyze Engagement History** - Queries all user engagement events (likes, saves, skips, watches)
2. **Build Interest DNA Profile** - Calculates patterns: like rate, skip rate, preferred industries, salary ranges, education levels
3. **Update User Profile** - Saves Interest DNA to `user.interest_dna` JSON field for analytics
4. **Call Claude 4.6 API** - Sends Interest DNA + available careers to Claude Sonnet 4.6
5. **AI Analysis** - Claude analyzes patterns and generates personalized matches with reasoning
6. **Store Recommendations** - Saves career IDs, normalized scores (0-1), and reasoning to database
7. **Return Results** - Returns top N careers ordered by match score

**Interest DNA Structure:**
```json
{
  "total_engagements": 15,
  "like_rate": 0.6,
  "skip_rate": 0.2,
  "liked_careers": ["Petroleum Engineer", "Marine Biologist"],
  "liked_industries": ["Energy", "Science"],
  "liked_salary_ranges": ["$85k-$150k", "$50k-$95k"],
  "preferred_education": ["Bachelor's Degree"]
}
```

**Example API Call:**
```bash
curl -X POST 'https://pathfinder-api.onrender.com/api/v1/recommendations/generate?user_id=1&limit=10'
```

**Response:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "career_id": 22,
    "score": 0.95,
    "reason": "Based on your interest in Science and Marine Biology, this career offers hands-on research opportunities and requires a Bachelor's Degree.",
    "shown_at": "2026-03-17T19:45:00Z",
    "clicked": false
  }
]
```

**Error Handling:**
- Returns 404 if user doesn't exist
- Returns 400 if user has no engagement history
- Returns 400 if user has engaged with all available careers
- Returns 500 if Claude API fails (with detailed error message)
- Handles JSON extraction from Claude responses (with/without markdown code blocks)
- Validates career IDs before storing recommendations
- Updates existing recommendations instead of duplicating

---

## Environment Variables

Located in `/Users/I870089/pathfinder/backend/.env`:

```bash
DATABASE_URL=<Neon PostgreSQL connection string>
ANTHROPIC_API_KEY=<Get from Vercel env or .env file>
CORS_ORIGINS=https://pathfinder-dashboard.onrender.com,https://pathfinder-mobile.onrender.com
```

**IMPORTANT:** These are also configured in Render dashboard (synced manually, not from `.env`)

---

## What's NOT Done Yet

### ❌ Test Seed Data for Frontend Development
**Status:** Need to create realistic test data for UI expert

**Needed:**
1. 3-5 test users with realistic profiles
2. 20-30 engagement events (likes, skips, watches) distributed across users
3. Pre-generated AI recommendations for each user
4. This gives UI expert real data to build against

**Priority:** HIGH - Unblocks frontend development

### ❌ API Documentation
- No Swagger/OpenAPI docs yet (FastAPI generates this automatically at `/docs`)
- Just needs to be verified and customized

### ❌ Backend Tests
- No pytest suite
- No CI/CD tests

### ❌ Authentication/Authorization
- Endpoints are completely open (no JWT validation)
- Need to add before production launch

---

## Render Deployment Status

**Current Blocker:** Render Web Service not created yet (waiting on Claude 2)

**When Created:**
- Service name: `pathfinder-api`
- Repository: https://github.com/chadlmc1970/pathfinder.git
- Branch: `main`
- Build command: `cd backend && pip install -r requirements.txt`
- Start command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`

**Environment Variables to Set in Render:**
1. `DATABASE_URL` - Neon PostgreSQL connection string
2. `ANTHROPIC_API_KEY` - Claude API key (see above)
3. `CORS_ORIGINS` - Frontend URLs
4. `PYTHON_VERSION` - `3.11.15`

---

## Testing the API (After Render Deploys)

```bash
# Health check
curl https://pathfinder-api.onrender.com/health

# Get all careers (should return 20 Louisiana careers)
curl https://pathfinder-api.onrender.com/api/v1/careers/

# Get single career
curl https://pathfinder-api.onrender.com/api/v1/careers/21

# Get videos for a career
curl https://pathfinder-api.onrender.com/api/v1/videos/?career_id=21

# Create test user
curl -X POST https://pathfinder-api.onrender.com/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@student.la.edu",
    "grade_level": 8,
    "school": "Test Middle School",
    "preferences": {"interests": ["science", "technology"]}
  }'

# Record engagement event
curl -X POST https://pathfinder-api.onrender.com/api/v1/engagement/ \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "career_id": 21,
    "action": "like"
  }'

# Get recommendations for user (returns AI-generated recommendations)
curl https://pathfinder-api.onrender.com/api/v1/recommendations/?user_id=1

# Generate NEW AI recommendations (requires engagement history)
curl -X POST https://pathfinder-api.onrender.com/api/v1/recommendations/generate?user_id=1&limit=10
```

---

## Frontend Status (NOT Your Responsibility)

### Mobile App (30% Complete)
- Location: `/Users/I870089/pathfinder/mobile/`
- Status: Scaffolded with mock data, needs API integration
- Assigned to: UI Expert or Claude 2

### Admin Dashboard (20% Complete)
- Location: `/Users/I870089/pathfinder/admin-dashboard/`
- Status: Landing page only, needs full CRUD implementation
- Assigned to: UI Expert or Claude 2

---

## Your Next Tasks (Priority Order)

1. **Add Test Seed Data** (15 min) - **HIGHEST PRIORITY**
   - Create 3-5 test users (realistic 8th grade profiles)
   - Generate 20-30 engagement events (likes/skips/watches)
   - Run AI recommendations generator for each user
   - This gives UI expert real data to work with immediately

2. **Create Deployment Verification Script** (10 min)
   - File: `/Users/I870089/pathfinder/backend/verify_deployment.py`
   - Smoke tests for all endpoints (including AI recommendations)
   - Can run after Render deploys

3. **Add API Documentation** (10 min)
   - Customize FastAPI auto-generated docs at `/docs`
   - Add descriptions and examples for AI recommendations endpoint

4. **Backend Tests** (30 min)
   - Add pytest suite
   - Test all CRUD endpoints + AI recommendations logic

5. **Authentication Middleware** (25 min)
   - JWT token validation
   - Protect admin endpoints

---

## Common Commands

```bash
# Navigate to backend
cd /Users/I870089/pathfinder/backend

# Activate venv
source venv/bin/activate

# Run database migration
alembic upgrade head

# Seed database
python seed_data.py

# Git workflow
git add -A
git commit -m "description"
git push origin main  # Triggers Render deploy

# NEVER run localhost server - deploy to Render instead
# (User's memory explicitly forbids localhost development)
```

---

## Key Files Reference

- **Main App:** `/Users/I870089/pathfinder/backend/app/main.py`
- **Database:** `/Users/I870089/pathfinder/backend/app/core/database.py`
- **Config:** `/Users/I870089/pathfinder/backend/app/core/config.py`
- **Models:** `/Users/I870089/pathfinder/backend/app/models/`
- **Schemas:** `/Users/I870089/pathfinder/backend/app/schemas/`
- **API Routes:** `/Users/I870089/pathfinder/backend/app/api/v1/`
- **Seed Data:** `/Users/I870089/pathfinder/backend/seed_data.py`

---

## Session Context Files

- **STATUS.md** - Current completion status (read this first)
- **SESSION.md** - Full 716-line project context
- **RECOVERY_PROMPT.md** - This file

---

## Critical Fixes to Remember

1. **Career Schema Fix (March 17, 2026):**
   - Changed `skills` from `Dict` to `List[str]` in schemas/career.py
   - Reason: Seed data uses array format, not nested dict
   - Committed as c15e693

2. **Render Config:**
   - Must use `cd backend &&` prefix in commands
   - Fixed in render.yaml (commits fed4237, cf38cb0)

---

## Recovery Command

If you're starting fresh, run this first:

```bash
cd /Users/I870089/pathfinder
git status  # Check current state
cat STATUS.md  # Read current status
cat backend/.env  # Verify environment variables
```

Then proceed with your assigned tasks above.

---

**Last Updated:** 2026-03-17 15:00 CST
**Git Commit:** e8c62c6 (Add AI-powered recommendations engine with Claude 4.6)
**Backend Status:** AI Engine COMPLETE ✅ - Next: Test seed data for frontend development
