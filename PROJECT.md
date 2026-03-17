# PathFinder - Project Coordination Hub

**Last Updated:** 2026-03-17
**Team Size:** 3 Agents (Backend Lead, Backend Dev, UI Expert)
**Status:** Backend deploying, Frontends complete

---

## 🎯 Project Mission

TikTok-style career exploration iOS app for Louisiana 8th graders. Students swipe through short career videos, get AI-powered recommendations from Claude 4.6.

---

## 👥 Team Structure

### Agent 1 - Backend Lead (Project Organizer)
**Role:** FastAPI backend architecture, Claude 4.6 AI integration, deployment coordination
**Status:** ✅ AI recommendations engine complete, managing deployment
**Documents:**
- `/Users/I870089/pathfinder/RECOVERY_PROMPT.md` - Recovery context
- `/Users/I870089/pathfinder/STATUS.md` - Project status

### Agent 2 - Backend Developer
**Role:** Backend development, deployment monitoring
**Status:** 🔄 Active - Monitoring Render deployment
**Current Task:** Fixing Render deployment (Blueprint creation, service ID: srv-d6sr8e4hg0os73fdsllg)

### Agent 3 - UI Expert
**Role:** React Native mobile app + Next.js admin dashboard
**Status:** ✅ Work complete - Both frontends built and integrated
**Documents:**
- `/Users/I870089/pathfinder/SESSION_UI_COMPLETE.md` - Complete UI implementation details
- `/Users/I870089/pathfinder/COORDINATION_NOTE.md` - Handoff to Agent 1

---

## 📊 Completion Status

### ✅ Backend (100% Complete)
- FastAPI + SQLAlchemy + Alembic
- Neon PostgreSQL database
- 20 Louisiana careers seeded
- Claude 4.6 AI recommendations engine
- All CRUD endpoints implemented
- **Deployment:** 🔄 In progress (Render Blueprint)

### ✅ Mobile App (100% Complete)
- React Native + Expo SDK 55
- TikTok-style video feed with expo-av
- Engagement tracking (like, save, skip, share)
- AI recommendations screen
- API integration complete
- **Deployment:** ⏳ Waiting for backend URL

### ✅ Admin Dashboard (100% Complete)
- Next.js 16 + shadcn/ui
- Real-time analytics dashboard
- Career CRUD (create, read, delete)
- User management
- Professional UI with color-coded metrics
- **Deployment:** ⏳ Waiting for backend URL

---

## 🔗 Current Infrastructure

### Production URLs
- **Backend API:** https://pathfinder-api.onrender.com ⚠️ (Wrong app deployed - needs fix)
- **Admin Dashboard:** Not deployed yet
- **Mobile App:** Not deployed yet (Expo Go testing only)

### Git Repository
- **Repo:** https://github.com/chadlmc1970/pathfinder.git
- **Branch:** `main` (auto-deploys to Render)
- **Latest Commit:** 2da9c6f

### Database
- **Provider:** Neon PostgreSQL
- **Connection:** In `/Users/I870089/pathfinder/backend/.env`
- **Status:** ✅ Live with 20 careers seeded

---

## 🚨 Critical Deployment Issue

**Problem:** Wrong backend app is deployed at `https://pathfinder-api.onrender.com`
- Current: "Route Solver Test" HTML page
- Expected: FastAPI PathFinder API with `/health`, `/api/v1/careers/`, etc.

**Cause:** Render service was manually created via UI, not via Blueprint
**Solution:** Agent 2 deleted service and recreated as Blueprint (service ID: srv-d6sr8e4hg0os73fdsllg)
**Status:** 🔄 Build in progress (commit 2da9c6f)

---

## 📋 Priority Tasks

### P0 - BLOCKING (Must Fix Now)
1. **Fix Render Deployment** - Get correct PathFinder backend live at production URL
   - **Owner:** Agent 2
   - **Status:** 🔄 Active

### P1 - HIGH (Unblocks Everything Else)
2. **Verify Backend Deployment** - Test all endpoints once deployment completes
   - **Owner:** Agent 1
   - **Status:** ⏳ Waiting on P0

3. **Update Frontend API URLs** - Point mobile + dashboard to correct backend URL
   - **Owner:** Agent 1
   - **Status:** ⏳ Waiting on P0

4. **Deploy Admin Dashboard** - Get dashboard live on Vercel
   - **Owner:** Agent 1
   - **Status:** ⏳ Waiting on P1

### P2 - MEDIUM (Polish & Features)
5. **Add Test Seed Data** - Create realistic users with engagement history
6. **Implement Video Upload** - Vercel Blob integration
7. **Add Authentication** - Clerk for dashboard, custom for mobile
8. **Career Edit Page** - Complete CRUD in admin dashboard
9. **Upload Real Videos** - Replace 5 placeholders with Louisiana career videos

### P3 - LOW (Nice to Have)
10. **Charts in Analytics** - Add recharts/chart.js
11. **Pagination** - For large datasets
12. **Backend Tests** - pytest suite
13. **API Documentation** - Customize FastAPI `/docs`

---

## 🔄 Team Coordination Protocol

### When Starting Work
1. Read **PROJECT.md** (this file) for current status
2. Check your agent-specific recovery document
3. Announce what you're working on (update this file)
4. Check for conflicts with other agents

### When Completing Work
1. Update **PROJECT.md** with completion status
2. Create handoff document for dependent tasks
3. Notify other agents if they're blocked on your work

### When Blocked
1. Update **PROJECT.md** with blocker details
2. Notify blocking agent
3. Switch to non-blocking tasks if available

---

## 📁 Project Structure

```
/Users/I870089/pathfinder/
├── backend/                          # FastAPI Python API (Agents 1 & 2)
│   ├── app/
│   │   ├── main.py                   # FastAPI app
│   │   ├── api/v1/                   # Endpoints (careers, videos, users, engagement, recs)
│   │   ├── models/                   # SQLAlchemy models
│   │   ├── schemas/                  # Pydantic schemas
│   │   └── services/                 # Claude 4.6 service
│   ├── alembic/                      # Database migrations
│   ├── seed_data.py                  # 20 Louisiana careers
│   ├── requirements.txt
│   └── .env                          # DATABASE_URL, ANTHROPIC_API_KEY
│
├── mobile/                           # React Native iOS app (Agent 3 - Complete)
│   ├── services/api.ts               # API client
│   ├── app/
│   │   ├── index.tsx                 # Video feed
│   │   └── recommendations.tsx       # AI recs screen
│   └── components/VideoCard.tsx      # Video player + engagement
│
├── admin-dashboard/                  # Next.js 16 admin panel (Agent 3 - Complete)
│   ├── lib/api.ts                    # API client
│   ├── app/
│   │   ├── page.tsx                  # Dashboard homepage
│   │   ├── careers/                  # Career CRUD
│   │   ├── analytics/                # Analytics dashboard
│   │   └── users/                    # User management
│   └── components/ui/                # shadcn/ui components
│
├── PROJECT.md                        # THIS FILE - Team coordination hub
├── RECOVERY_PROMPT.md                # Agent 1 recovery context
├── SESSION_UI_COMPLETE.md            # Agent 3 complete implementation details
├── COORDINATION_NOTE.md              # Agent 3 → Agent 1 handoff
├── STATUS.md                         # Current completion status
└── README.md                         # Project overview
```

---

## 🛠️ Tech Stack

### Backend
- FastAPI (Python 3.11)
- SQLAlchemy + Alembic
- Neon PostgreSQL
- Claude 4.6 (claude-opus-4-6)
- Render deployment

### Mobile
- React Native 0.83
- Expo SDK 55
- expo-av (video playback)
- axios (HTTP client)

### Admin Dashboard
- Next.js 16 (App Router, Turbopack)
- shadcn/ui (Radix + Tailwind CSS v4)
- TypeScript

---

## 🚀 Deployment Workflow

### Backend (Render)
1. Make changes in `/Users/I870089/pathfinder/backend/`
2. `git commit -m "description" && git push origin main`
3. Render auto-deploys from Blueprint (~2 min)
4. Test: `curl https://pathfinder-api.onrender.com/health`

### Admin Dashboard (Vercel)
1. `cd /Users/I870089/pathfinder/admin-dashboard`
2. `vercel link` (one-time setup)
3. `vercel deploy --prod`

### Mobile App (Expo)
1. `cd /Users/I870089/pathfinder/mobile`
2. `npm start` for Expo Go testing
3. `eas build` for TestFlight (future)

---

## 📝 Environment Variables

### Backend (Render)
```bash
DATABASE_URL=<Neon PostgreSQL connection string>
ANTHROPIC_API_KEY=<Claude API key>
CORS_ORIGINS=https://pathfinder-dashboard.onrender.com
PYTHON_VERSION=3.11.15
```

### Mobile (Hardcoded in `services/api.ts`)
```typescript
const API_URL = 'https://pathfinder-api.onrender.com';
```

### Admin Dashboard (Hardcoded in `lib/api.ts`)
```typescript
const API_URL = 'https://pathfinder-api.onrender.com';
```

---

## ⚠️ Critical Rules

1. **NO LOCALHOST** - Always use production URLs
2. **NO LOCAL DEV SERVERS** - Test against deployed backend
3. **Render auto-deploys** - Push to `main` → automatic deployment
4. **Frontend API URLs are hardcoded** - Must update if backend URL changes

---

## 🆘 If You're Lost

1. **Read PROJECT.md** (this file)
2. **Check your agent-specific document:**
   - Agent 1: `RECOVERY_PROMPT.md`
   - Agent 2: (TBD - create if needed)
   - Agent 3: `SESSION_UI_COMPLETE.md`
3. **Ask:** "What's blocking the project right now?"
4. **Coordinate:** Update this file when you start/complete work

---

**🚦 Current Blocker:** Render deployment (wrong app deployed) - Agent 2 fixing now
**🎯 Next Milestone:** Get correct backend live → verify endpoints → deploy dashboard
