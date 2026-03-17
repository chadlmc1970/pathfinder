# C3 (Frontend Developer) - HOLD Instructions

**Status:** ⏸️ **BLOCKED - DO NOT START YET**

## Current Situation

C1 (DevOps Lead) is fixing a **critical blocker**:
- Render service is deploying **wrong application** (TSP Route Solver instead of PathFinder)
- Repository connection needs to be fixed in Render dashboard
- Backend API is NOT live yet
- Admin dashboard NOT deployed to Vercel yet

## Your Assignments

You have 3 phases assigned:

### Phase 3: Career Edit Page (After C1 completes Phase 2)
- Admin dashboard career editing interface
- Form with validation for all career fields
- AI recommendation testing UI
- Integration with backend API

### Phase 4: Video Upload (After Phase 3)
- iOS mobile app video upload component
- Camera integration with expo-camera
- Video preview and confirmation
- Upload to backend API

### Phase 5.2: Login UI (After C2 completes Phase 5.1)
- Admin dashboard login page
- JWT token storage
- Protected routes
- Auth state management

## When to Start

**Phase 3 - Watch for:**
```bash
cd /Users/I870089/pathfinder
cat SESSION_WORK.md | grep "Phase 2"
# When you see: Phase 2 | ✅ COMPLETE | ...
# Then you can start Phase 3
```

**Phase 5.2 - Watch for:**
```bash
cat SESSION_WORK.md | grep "Phase 5.1"
# When you see: Phase 5.1 | ✅ COMPLETE | ...
# Then you can start Phase 5.2
```

## Required Reading Before Starting

1. `PROJECT.md` - Project overview and architecture
2. `admin-dashboard/` - Next.js 16 dashboard (for Phase 3 & 5.2)
3. `mobile/` - React Native app (for Phase 4)
4. Master plan: `/.claude/plans/lucky-stirring-bentley.md`

## Estimated Time

- Phase 3 (Career Edit): 1 hour
- Phase 4 (Video Upload): 1 hour
- Phase 5.2 (Login UI): 45 minutes
- **Total waiting time:** ~30 minutes (for C1 to complete Phases 1 & 2)

## Production URLs (After C1 Deployment)

- **Admin Dashboard:** https://pathfinder-dashboard.onrender.com (or Vercel URL)
- **Backend API:** https://pathfinder-api.onrender.com
- **Mobile App:** Test locally with Expo Go

## Communication

- Update `SESSION_WORK.md` when you start each phase
- Mark phases as 🔄 IN PROGRESS, then ✅ COMPLETE
- Coordinate with C2 for Phase 5 (auth integration)

---

**DO NOT START UNTIL C1 COMPLETES PHASE 2** ✋
