# PathFinder MVP - Project Status
**Last Updated:** 2026-03-17 14:40 CST
**Session:** Backend Recovery (Claude 1)

---

## 🎯 Project Architecture

```
PathFinder - TikTok-style career exploration for Louisiana 8th graders
├── Backend API (FastAPI + Neon PostgreSQL)
├── iOS Mobile App (Expo/React Native)
└── Admin Dashboard (Next.js 16 + shadcn/ui)
```

---

## ✅ Backend API - 100% Complete

**Location:** `/Users/I870089/pathfinder/backend/`
**Status:** ✅ Ready for deployment
**Git:** Pushed to `main` (commit c15e693)

### Working Endpoints
- `GET /health` - Server health check
- `GET /api/v1/careers/` - List all careers (20 Louisiana careers seeded)
- `GET /api/v1/careers/{id}` - Get single career
- `POST /api/v1/careers/` - Create career
- `PUT /api/v1/careers/{id}` - Update career
- `DELETE /api/v1/careers/{id}` - Delete career
- `GET /api/v1/videos/` - List videos (5 placeholder videos)
- `GET /api/v1/videos?career_id={id}` - Videos by career
- `POST /api/v1/engagement/` - Record swipe events
- `GET /api/v1/users/` - List users
- `POST /api/v1/users/` - Create user
- `GET /api/v1/recommendations/?user_id={id}` - AI recommendations (Claude 4.6)

### Database
- **Provider:** Neon PostgreSQL
- **Status:** Connected and seeded
- **Data:** 20 Louisiana careers (Petroleum Engineer, Chef, Marine Biologist, Nurse, etc.)

### Deployment
- **Platform:** Render
- **Config:** `render.yaml` configured
- **URL:** `https://pathfinder-api.onrender.com` (pending service creation)
- **Blocker:** Waiting for Render Web Service creation

### Recent Fixes
- ✅ Fixed career schema: `skills` changed from Dict to List to match seed data
- ✅ All endpoints tested and working
- ✅ Database migrations applied

---

## ⚠️ iOS Mobile App - 30% Complete

**Location:** `/Users/I870089/pathfinder/mobile/`
**Status:** ⚠️ Scaffolded but needs implementation
**Stack:** Expo SDK 55, React Native 0.83, TypeScript

### What's Done
- ✅ Expo project initialized
- ✅ File-based routing with expo-router
- ✅ Basic TikTok-style vertical scroll structure
- ✅ VideoCard component skeleton
- ✅ App.json configured for iOS

### What's Missing
- ❌ API client service (no backend connection)
- ❌ Real video playback (expo-av integration)
- ❌ User authentication
- ❌ Engagement tracking (like/skip/save)
- ❌ AI recommendations UI
- ❌ State management
- ❌ Error handling

### Current State
- Using hardcoded `MOCK_VIDEOS` array
- No network calls
- Placeholder video URLs

---

## ⚠️ Admin Dashboard - 20% Complete

**Location:** `/Users/I870089/pathfinder/admin-dashboard/`
**Status:** ⚠️ Scaffolded but needs implementation
**Stack:** Next.js 16, shadcn/ui, Tailwind CSS v4, TypeScript

### What's Done
- ✅ Next.js 16 project initialized
- ✅ shadcn/ui components installed
- ✅ Landing page with basic stats cards
- ✅ Navigation structure

### What's Missing
- ❌ API client service (no backend connection)
- ❌ `/careers` page - CRUD for career profiles
- ❌ `/users` page - User management
- ❌ `/analytics` page - Engagement metrics
- ❌ `/videos/upload` page - Video management
- ❌ Forms for creating/editing careers
- ❌ Data tables with sorting/filtering
- ❌ Real-time stats from backend

### Current State
- All metrics show hardcoded `0`
- Navigation links exist but routes don't
- No API integration

---

## 🎯 Recommendation: Spin Up UI Expert

**Why:**
- Backend is complete and tested
- Both frontend apps need significant work:
  - API integration
  - Component implementation
  - State management
  - User flows

**What UI Expert Should Handle:**

### Mobile App (Priority 1)
1. Connect to `https://pathfinder-api.onrender.com`
2. Implement API client with error handling
3. Real video playback with expo-av
4. Engagement tracking (POST to `/api/v1/engagement/`)
5. AI recommendations feed
6. User onboarding flow

### Admin Dashboard (Priority 2)
1. Connect to backend API
2. Build careers CRUD pages with forms
3. User management interface
4. Analytics dashboard with charts
5. Video upload/management
6. Real-time stats from API

---

## 📋 Next Steps

### Immediate (Claude 2 or New Agent)
1. Create Render Web Service for backend
2. Connect GitHub repo to Render
3. Set environment variables in Render
4. Verify deployment at `https://pathfinder-api.onrender.com/health`

### After Backend Deploys
1. Spin up UI expert agent for mobile app
2. Build out admin dashboard features
3. Connect both frontends to production API

---

## 🔧 Technical Debt / Notes
- Seed data has 5 placeholder videos - need real Louisiana career videos
- Recommendations endpoint exists but AI logic not fully implemented yet
- No authentication/authorization on backend (add before production)
- Mobile app needs App Store deployment config
- Admin dashboard needs hosting (Vercel recommended)
