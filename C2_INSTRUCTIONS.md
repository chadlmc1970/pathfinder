# C2 (Backend Developer) - HOLD Instructions

**Status:** ⏸️ **BLOCKED - DO NOT START YET**

## Current Situation

C1 (DevOps Lead) is fixing a **critical blocker**:
- Render service is deploying **wrong application** (TSP Route Solver instead of PathFinder)
- Repository connection needs to be fixed in Render dashboard
- Backend API is NOT live yet

## Your Assignment (Phase 5.1)

Once C1 marks Phase 1 as ✅ in `SESSION_WORK.md`, you will implement:

### JWT Authentication Backend
- Add JWT token generation endpoint (`/api/v1/auth/token`)
- Add token verification middleware
- Protect existing career endpoints with auth
- Add user registration/login endpoints
- Use PostgreSQL for user storage (Neon database already configured)

## When to Start

**Watch for this signal:**
```bash
cd /Users/I870089/pathfinder
cat SESSION_WORK.md | grep "Phase 1"
# When you see: Phase 1 | ✅ COMPLETE | ...
# Then you can start Phase 5.1
```

## Required Reading Before Starting

1. `PROJECT.md` - Project overview and architecture
2. `backend/app/main.py` - Current API structure
3. `backend/app/models/` - Database models
4. Master plan: `/.claude/plans/lucky-stirring-bentley.md`

## Estimated Time

- Phase 5.1 (JWT Backend): 45 minutes
- Waiting on C1: ~15 minutes

## Communication

- Update `SESSION_WORK.md` when you start Phase 5.1
- Mark Phase 5.1 as 🔄 IN PROGRESS
- Mark Phase 5.1 as ✅ COMPLETE when done
- This allows C3 to coordinate Phase 5.2 (Login UI)

---

**DO NOT START UNTIL C1 COMPLETES PHASE 1** ✋
