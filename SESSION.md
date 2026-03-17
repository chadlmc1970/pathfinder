# PathFinder MVP - Session Recovery Document

**Last Updated:** 2026-03-17
**Status:** Phase 1 Foundation Complete - Ready for Development
**Context:** Created after agent team failure, pivoted to direct building

---

## 🎯 Project Overview

**PathFinder** - TikTok-style career exploration mobile app for Louisiana 8th graders.

### Core Features
- Vertical video feed (like TikTok) showing career introduction videos
- Swipe interface with like/save/share/skip actions
- AI-powered career recommendations using Claude 4.6
- Interest DNA algorithm that learns from user behavior
- Admin dashboard for content management
- Real-time engagement analytics

### Target Users
- **Primary:** Louisiana 8th grade students (13-14 years old)
- **Secondary:** School counselors and administrators (admin dashboard)

---

## 📐 Architecture

```
pathfinder/
├── mobile/              # React Native/Expo iOS app (TikTok-style UI)
├── admin-dashboard/     # Next.js 16 admin interface (shadcn/ui)
├── backend/             # FastAPI Python API + Claude 4.6 AI
└── SESSION.md           # This file
```

### Tech Stack

**Mobile:**
- Expo SDK 55, React Native 0.83
- expo-router (file-based routing)
- expo-av (video playback)
- expo-linear-gradient (UI gradients)
- TypeScript

**Dashboard:**
- Next.js 16 (App Router, Turbopack)
- shadcn/ui components
- Tailwind CSS v4
- TypeScript
- Clerk authentication (via Vercel Marketplace)

**Backend:**
- FastAPI (Python)
- SQLAlchemy ORM
- Alembic migrations
- Neon Serverless PostgreSQL
- Claude 4.6 via Anthropic SDK
- Pydantic for schemas

**Infrastructure:**
- Database: Neon PostgreSQL (connection string in backend/.env.example)
- Video Storage: Vercel Blob
- AI: Claude 4.6 (Anthropic API)
- Deployment:
  - Backend → Render (auto-deploy from main branch)
  - Dashboard → Vercel
  - Mobile → Expo EAS

---

## ✅ Current State (Phase 1 Complete)

### What's Been Built

#### 1. Mobile App (/Users/I870089/pathfinder/mobile/)
**Status:** Scaffolded, not yet runnable (need npm install)

**Key Files:**
- `app/_layout.tsx` - Expo Router root layout
- `app/index.tsx` - TikTok-style feed with FlatList pagination
- `components/VideoCard.tsx` - Video card with career info overlay and action buttons
- `package.json` - Dependencies configured (expo-router, expo-av, axios)
- `app.json` - Expo config (iOS bundle ID, plugins)
- `tsconfig.json` - TypeScript config
- `.env.example` - API_URL template

**Features Implemented:**
- Vertical scroll video feed (paginated FlatList)
- Career info overlay (title, description, salary, education)
- Action buttons (like, save, share, skip) with state
- Linear gradient overlay for readability
- Placeholder thumbnail images (will replace with expo-av video player)

**Next Steps:**
- Run `npm install` to install dependencies
- Replace Image placeholders with expo-av Video components
- Connect to backend API for career data
- Implement actual engagement tracking (POST to /api/v1/engagement)

#### 2. Admin Dashboard (/Users/I870089/pathfinder/admin-dashboard/)
**Status:** Scaffolded and runnable (npm install already completed during creation)

**Key Files:**
- `app/page.tsx` - Dashboard homepage with metrics cards and quick actions
- `components/ui/` - shadcn/ui components (card, button, badge, input, label, select, dialog)
- `lib/utils.ts` - cn() utility for className merging
- `components.json` - shadcn config
- `next.config.ts` - Next.js 16 config
- `.env.local.example` - NEXT_PUBLIC_API_URL template

**Features Implemented:**
- Dashboard homepage with 3 metric cards (users, careers, engagement)
- Navigation bar (Careers, Users, Analytics links)
- Quick action buttons (Add Career, Upload Video, View Analytics)
- shadcn/ui component library initialized
- Dark mode support (automatic via shadcn)

**Next Steps:**
- Create CRUD pages for careers (`/careers`, `/careers/[id]`, `/careers/new`)
- Create video upload page with Vercel Blob integration
- Create user management page
- Create analytics dashboard with charts
- Add Clerk authentication (user must run `vercel integration add clerk` manually)
- Connect to backend API for data

#### 3. Backend API (/Users/I870089/pathfinder/backend/)
**Status:** Scaffolded, models created, migrations pending

**Key Files:**
- `app/main.py` - FastAPI app with CORS, health check endpoint
- `app/core/config.py` - Pydantic settings (DATABASE_URL, ANTHROPIC_API_KEY, CORS_ORIGINS)
- `app/core/database.py` - SQLAlchemy engine, session, Base, get_db()
- `app/models/user.py` - User model (email, interest_dna JSONB, engagement_score)
- `app/models/career.py` - Career model (title, industry, salary range, skills JSON, pathway JSON)
- `app/models/video.py` - Video model (career_id FK, blob_url, thumbnail_url, duration)
- `app/models/engagement.py` - Engagement tracking (user_id, video_id, action, watch_duration)
- `app/models/recommendation.py` - Recommendation model (user_id, career_id, score, reason)
- `app/api/v1/careers.py` - CRUD endpoints for careers (GET, POST, PUT, DELETE)
- `app/api/v1/__init__.py` - API router setup (includes careers router)
- `app/schemas/career.py` - Pydantic schemas (CareerCreate, CareerUpdate, CareerResponse)
- `app/schemas/user.py` - Pydantic schemas (UserCreate, UserUpdate, UserResponse)
- `app/services/recommendation.py` - Claude 4.6 integration (generate_career_recommendations, update_interest_dna)
- `requirements.txt` - All dependencies listed
- `.env.example` - Template with Neon connection string and placeholders
- `alembic.ini` - Alembic config
- `alembic/env.py` - Alembic environment with all models imported
- `alembic/script.py.mako` - Migration template

**Features Implemented:**
- FastAPI app with CORS middleware
- Health check endpoint (`GET /health`)
- SQLAlchemy models for all entities
- CRUD endpoints for careers (`/api/v1/careers`)
- Pydantic schemas with validation
- Claude 4.6 recommendation service (2 functions)
- Alembic migration setup (ready to run)
- Neon PostgreSQL connection configured

**Database Schema:**
- `users` - id, email, full_name, grade, school, interest_dna (JSONB), engagement_score (float), created_at, updated_at
- `careers` - id, title, industry, description, min_salary, max_salary, education_required, skills (JSON), pathway (JSON), created_at, updated_at
- `videos` - id, career_id (FK), blob_url, thumbnail_url, duration, created_at, updated_at
- `engagement` - id, user_id (FK), video_id (FK), action (enum: watched/liked/saved/skipped/shared), watch_duration, created_at
- `recommendations` - id, user_id (FK), career_id (FK), score, reason, created_at

**Next Steps:**
- Create `.env` from `.env.example` and add real ANTHROPIC_API_KEY
- Run `alembic upgrade head` to create database tables
- Create seed script to populate careers and videos
- Implement remaining endpoints (users, videos, engagement, recommendations)
- Test Claude 4.6 recommendation service
- Deploy to Render

#### 4. AI Recommendation Service
**Status:** Code written, not yet tested

**Location:** `backend/app/services/recommendation.py`

**Functions:**
1. `generate_career_recommendations(user_interest_dna, available_careers, top_n=5)`
   - Takes user's Interest DNA (dict) and list of careers
   - Sends prompt to Claude 4.6 (claude-opus-4-6)
   - Returns top N career matches with scores (0-100) and reasoning
   - JSON response parsed and returned

2. `update_interest_dna(current_dna, engagement_history)`
   - Takes current Interest DNA and recent engagement events
   - Analyzes patterns (liked vs skipped, watched vs saved)
   - Returns updated Interest DNA reflecting behavior
   - Uses Claude 4.6 to identify emerging interests

**Interest DNA Structure (Example):**
```json
{
  "work_style": {
    "hands_on_vs_intellectual": 0.7,
    "people_vs_solo": 0.3,
    "creative_vs_analytical": 0.5
  },
  "environment": {
    "outdoor_vs_indoor": 0.6,
    "structured_vs_flexible": 0.4
  },
  "values": {
    "helping_others": 0.8,
    "high_salary": 0.5,
    "job_security": 0.7
  }
}
```

**Next Steps:**
- Test Claude 4.6 integration with sample data
- Verify JSON parsing is robust
- Add error handling for API failures
- Implement rate limiting if needed

---

## 🚫 What FAILED (Critical Context)

### Agent Team Approach - Complete Failure

**What Happened:**
1. Attempted to use Claude Code Agent SDK with team of 8 agents (4 original + 4 "-2" replacements)
2. All agents configured with:
   - `backendType: "in-process"` (tied to session)
   - `model: "claude-opus-4-6"` (most capable model)
   - Detailed prompts for mobile, dashboard, backend, AI/QA work
3. **All 8 agents stalled at permission request phase** for 1+ hours
4. Agents would NOT respond to:
   - Broadcast messages with explicit work commands
   - Shutdown requests
   - Any inter-agent communication
5. **ZERO code files created** despite detailed task assignments
6. **ZERO task ownership claims** via TaskUpdate

**Root Cause:**
- "in-process" agents with cautious permission mode = guaranteed stall
- Agents wait indefinitely for permission approvals
- Broadcast messages cannot unblock frozen agents
- Team coordination requires responsive agents (we had zombies)

**Lesson Learned:**
- **Direct building is faster and more reliable than agent teams for scaffolding work**
- Agent teams may work for other scenarios, but NOT for initial project setup
- When agents stall for >30 minutes with zero output, abort immediately
- User explicitly said "id rather you use the team" but after failure, pivoted to "run it solo. ridiculous"

**Team Files (can be deleted):**
- `/Users/I870089/.claude/teams/pathfinder-mvp/` (entire directory)
- `/Users/I870089/.claude/tasks/pathfinder-mvp/` (entire directory)

---

## 📋 Required Setup Steps

### 1. Install Dependencies

**Mobile:**
```bash
cd /Users/I870089/pathfinder/mobile
npm install
```

**Dashboard:**
```bash
cd /Users/I870089/pathfinder/admin-dashboard
npm install  # Already done during create-next-app
```

**Backend:**
```bash
cd /Users/I870089/pathfinder/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Environment Variables

**Backend (.env):**
```bash
cd /Users/I870089/pathfinder/backend
cp .env.example .env
# Edit .env and add:
# - ANTHROPIC_API_KEY=sk-ant-... (get from https://console.anthropic.com/)
```

**Mobile (.env):**
```bash
cd /Users/I870089/pathfinder/mobile
cp .env.example .env
# API_URL=http://localhost:8000 (or production URL)
```

**Dashboard (.env.local):**
```bash
cd /Users/I870089/pathfinder/admin-dashboard
cp .env.local.example .env.local
# NEXT_PUBLIC_API_URL=http://localhost:8000 (or production URL)
```

### 3. Database Setup

**Run Migrations:**
```bash
cd /Users/I870089/pathfinder/backend
source venv/bin/activate
alembic upgrade head
```

**Verify Connection:**
```bash
# In Python REPL:
python3
>>> from app.core.database import engine
>>> engine.connect()
# Should succeed with Neon PostgreSQL
```

### 4. Start Development Servers

**Terminal 1 - Backend:**
```bash
cd /Users/I870089/pathfinder/backend
source venv/bin/activate
uvicorn app.main:app --reload
# http://localhost:8000
# http://localhost:8000/docs (OpenAPI)
```

**Terminal 2 - Dashboard:**
```bash
cd /Users/I870089/pathfinder/admin-dashboard
npm run dev
# http://localhost:3000
```

**Terminal 3 - Mobile:**
```bash
cd /Users/I870089/pathfinder/mobile
npm start
# Scan QR code with Expo Go app
```

---

## 🎯 Next Development Tasks (Phase 2)

### Priority 1: Data & Content
1. **Create seed script** for careers data
   - Populate ~20-30 diverse career profiles
   - Include accurate salary ranges, education requirements
   - Louisiana-specific career pathways (e.g., oil/gas, tourism, healthcare)

2. **Upload sample videos**
   - Create Vercel Blob upload endpoint in backend
   - Upload 5-10 career introduction videos
   - Link videos to career profiles in database

3. **Test Claude 4.6 recommendations**
   - Create test script with sample Interest DNA
   - Verify recommendation quality
   - Tune prompts if needed

### Priority 2: Mobile Integration
1. **Implement expo-av video player**
   - Replace Image placeholders in VideoCard.tsx
   - Add video controls (play/pause, scrubbing)
   - Track watch duration for engagement

2. **Connect to backend API**
   - Create API client service (axios)
   - Fetch career video feed from `/api/v1/videos`
   - POST engagement events to `/api/v1/engagement`

3. **Implement user authentication**
   - Decide on auth approach (Clerk, custom, etc.)
   - Store user_id in AsyncStorage
   - Send user_id with engagement events

### Priority 3: Admin Dashboard CRUD
1. **Career management pages**
   - `/careers` - List all careers (table with search/filter)
   - `/careers/[id]` - View/edit single career
   - `/careers/new` - Create new career profile
   - Forms with validation using react-hook-form

2. **Video upload page**
   - `/videos/upload` - Upload to Vercel Blob
   - Link video to career profile
   - Generate thumbnail from video

3. **User analytics page**
   - `/users` - List all users with engagement scores
   - `/users/[id]` - View user's Interest DNA and engagement history
   - Visualize Interest DNA (radar chart)

4. **Analytics dashboard**
   - `/analytics` - Charts for engagement metrics
   - Most popular careers
   - Watch time trends
   - User growth over time

### Priority 4: Deployment
1. **Backend to Render**
   - Create Render.com account
   - Connect GitHub repo (chadlmc1970/pathfinder)
   - Set environment variables in Render dashboard
   - Auto-deploy on push to main

2. **Dashboard to Vercel**
   - Connect GitHub repo to Vercel
   - Add Clerk integration via Vercel Marketplace
   - Set NEXT_PUBLIC_API_URL to Render backend URL
   - Auto-deploy on push to main

3. **Mobile to Expo EAS**
   - Set up Expo EAS Build
   - Configure iOS signing
   - Submit to TestFlight for internal testing

---

## 🔧 Critical Commands Reference

### Database
```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# View migration history
alembic history
```

### Backend
```bash
# Start dev server
uvicorn app.main:app --reload

# Start with specific host/port
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Run tests (when created)
pytest

# Check OpenAPI docs
open http://localhost:8000/docs
```

### Dashboard
```bash
# Start dev server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Add shadcn component
npx shadcn@latest add <component-name>
```

### Mobile
```bash
# Start Expo dev server
npm start

# Start with specific platform
npm run ios
npm run android
npm run web

# Clear cache
npm start -- --clear
```

---

## 🗄️ Database Connection Info

**Provider:** Neon Serverless PostgreSQL
**Connection String:** (in backend/.env.example)
```
postgresql://neondb_owner:npg_xZF8lLS2RiGP@ep-round-morning-amlgi5xs-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

**Features:**
- Serverless (scales to zero)
- Connection pooling built-in
- Auto-suspend after inactivity
- PostgreSQL 16 compatible

---

## 📚 Key Documentation Links

- **Expo:** https://docs.expo.dev/
- **Expo Router:** https://docs.expo.dev/router/introduction/
- **expo-av:** https://docs.expo.dev/versions/latest/sdk/av/
- **Next.js 16:** https://nextjs.org/docs
- **shadcn/ui:** https://ui.shadcn.com/
- **FastAPI:** https://fastapi.tiangolo.com/
- **SQLAlchemy:** https://docs.sqlalchemy.org/
- **Alembic:** https://alembic.sqlalchemy.org/
- **Anthropic API:** https://docs.anthropic.com/
- **Neon:** https://neon.tech/docs/
- **Vercel Blob:** https://vercel.com/docs/storage/vercel-blob
- **Clerk:** https://clerk.com/docs

---

## 💡 Design Decisions & Rationale

### Why Expo over React Native CLI?
- Faster development cycle
- Managed workflow (no Xcode/Android Studio config)
- OTA updates via Expo Updates
- Easier deployment to TestFlight/Play Store via EAS

### Why Next.js 16 for Admin Dashboard?
- App Router for nested layouts
- Server Components for performance
- Turbopack for instant HMR
- Built-in API routes (not needed, but nice to have)
- Vercel deployment optimized

### Why shadcn/ui over other component libraries?
- Copy/paste components (own the code)
- Built on Radix UI (accessibility)
- Tailwind CSS integration
- Dark mode support out of the box
- Active development and community

### Why FastAPI over Django/Flask?
- Modern async Python framework
- Automatic OpenAPI docs
- Pydantic validation
- Type hints throughout
- Fast development and runtime performance

### Why Neon over other PostgreSQL providers?
- Serverless (no idle costs)
- Connection pooling built-in
- Git-like branching (for preview deployments)
- Generous free tier
- Low latency for Render deployments

### Why Claude 4.6 for Recommendations?
- Most capable model available
- Excellent at reasoning and explanation
- Can handle nuanced career matching
- Provides human-readable reasoning
- Opus tier for best quality

### Why Vercel Blob for Video Storage?
- Integrated with Vercel deployment
- Simple upload API
- CDN-backed (fast global delivery)
- No separate S3 bucket management
- Generous free tier

---

## 🎓 Interest DNA Algorithm Explained

**Concept:** Multi-dimensional preference profile that evolves with user behavior.

**Dimensions:**
1. **Work Style**
   - Hands-on vs Intellectual (0.0 = hands-on, 1.0 = intellectual)
   - People-focused vs Solo (0.0 = solo, 1.0 = people)
   - Creative vs Analytical (0.0 = creative, 1.0 = analytical)

2. **Environment**
   - Outdoor vs Indoor (0.0 = outdoor, 1.0 = indoor)
   - Structured vs Flexible (0.0 = structured, 1.0 = flexible)

3. **Values**
   - Helping Others (0.0 = not important, 1.0 = very important)
   - High Salary (0.0 = not important, 1.0 = very important)
   - Job Security (0.0 = not important, 1.0 = very important)

**Initial DNA:** Set during onboarding questionnaire (not yet built).

**DNA Updates:** After every 10 engagement events, call `update_interest_dna()`:
- Liked videos → strengthen matching dimensions
- Saved videos → reinforce interest
- Watched to completion → positive signal
- Skipped quickly → negative signal
- Patterns across multiple skips → adjust DNA away from those traits

**Recommendation Matching:**
- Each career has a "DNA fingerprint" (same structure)
- Match user DNA to career DNA using cosine similarity or weighted euclidean distance
- Claude 4.6 adds semantic layer (understands context beyond numbers)
- Return top N matches with human-readable reasoning

---

## 🚨 Known Issues & Workarounds

### Issue: shadcn add failed with ENOTFOUND
**Status:** Partial failure during dashboard setup
**Affected:** Some shadcn components (form, dialog may be incomplete)
**Workaround:** Re-run `npx shadcn@latest add <component>` individually when needed
**Root Cause:** Network issue during batch component install

### Issue: Alembic migrations not yet run
**Status:** Database tables don't exist yet
**Impact:** Backend API will fail on database queries
**Fix:** Run `alembic upgrade head` in backend directory

### Issue: ANTHROPIC_API_KEY not set
**Status:** Claude 4.6 recommendation service will fail
**Impact:** Cannot test AI recommendations until key is added
**Fix:** Get API key from https://console.anthropic.com/ and add to backend/.env

### Issue: No seed data
**Status:** Database is empty (no careers or videos)
**Impact:** Mobile app will show empty feed
**Fix:** Create seed script to populate initial content

---

## 🔄 Recovery Instructions (If Context Lost)

If you're a new Claude instance reading this after context compaction:

1. **Read this file first** - You're doing it right now ✓
2. **Check current state:**
   ```bash
   tree -L 2 -I 'node_modules|__pycache__|venv|.git' /Users/I870089/pathfinder
   ```
3. **Verify what's runnable:**
   ```bash
   # Backend
   cd /Users/I870089/pathfinder/backend && ls -la .env 2>/dev/null && echo "✓ Backend env configured" || echo "✗ Need to create .env"

   # Dashboard
   cd /Users/I870089/pathfinder/admin-dashboard && ls -la node_modules 2>/dev/null && echo "✓ Dashboard deps installed" || echo "✗ Need npm install"

   # Mobile
   cd /Users/I870089/pathfinder/mobile && ls -la node_modules 2>/dev/null && echo "✓ Mobile deps installed" || echo "✗ Need npm install"
   ```
4. **Ask user:** "What would you like to work on next?"
   - If starting from scratch: Follow "Required Setup Steps" section
   - If continuing development: Follow "Next Development Tasks" section
   - If debugging: Check "Known Issues & Workarounds" section

5. **DO NOT attempt to use agent teams** - Direct building has proven faster and more reliable

---

## 📝 Session Notes

**Session Date:** 2026-03-17
**Duration:** ~2 hours total (1h agent failure, 15min direct building)
**Outcome:** Phase 1 foundation complete, all 4 components scaffolded
**User Sentiment:** Frustrated with agent team failure, satisfied with direct building approach

**Key Quotes:**
- User: "id rather you use the team" (initial preference for agent approach)
- User: "run it solo. ridiculous" (pivot after agent failure)
- User: "recovery prompt to clear ctx window. bw thorough. I do not want to have to guide you back." (this document's creation)

**Future Sessions:**
- Continue with Phase 2 development tasks
- Prioritize getting a working end-to-end demo (seed data → mobile feed → engagement tracking)
- Deploy early to get user feedback from actual 8th graders

---

## 🎯 Success Criteria

**Phase 1 (Complete):** ✅
- All 4 components scaffolded
- Database models defined
- AI recommendation service coded
- Project structure established

**Phase 2 (Next):**
- [ ] Database tables created (alembic upgrade head)
- [ ] Seed data populated (20+ careers, 10+ videos)
- [ ] Mobile app connects to backend API
- [ ] Video playback working in mobile app
- [ ] Claude 4.6 recommendations tested and working
- [ ] Admin dashboard CRUD for careers functional

**Phase 3 (Deployment):**
- [ ] Backend deployed to Render
- [ ] Dashboard deployed to Vercel with Clerk auth
- [ ] Mobile app submitted to TestFlight
- [ ] 10 beta testers using the app
- [ ] Feedback collected and prioritized

**Phase 4 (Production):**
- [ ] 1000+ career videos in library
- [ ] Deployed to all Louisiana 8th grade schools
- [ ] Analytics dashboard showing usage metrics
- [ ] Regular content updates from school counselors

---

**END OF SESSION RECOVERY DOCUMENT**
