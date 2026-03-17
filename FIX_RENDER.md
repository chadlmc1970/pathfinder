# Fix Render Deployment - Action Required

**Issue:** Render service `srv-d6sr8e4hg0os73fdsllg` is deploying the **wrong application** (TSP Route Solver instead of PathFinder).

**Root Cause:** The Render service is connected to the wrong GitHub repository.

---

## ⚡ FASTEST FIX (5 minutes)

### Option 1: Reconnect Repository in Dashboard

1. **Open Render dashboard:**
   ```
   https://dashboard.render.com/web/srv-d6sr8e4hg0os73fdsllg
   ```

2. **Check Settings tab:**
   - Look for "Repository" section
   - Current repo is probably: `chadlmc1970/tsp` or similar (WRONG)
   - Should be: `chadlmc1970/pathfinder` (CORRECT)

3. **Fix the connection:**
   - Click "Disconnect Repository"
   - Click "Connect Repository"
   - Select: `chadlmc1970/pathfinder`
   - Branch: `main`
   - Root Directory: leave blank (render.yaml is in root)

4. **Trigger manual deploy:**
   - Click "Manual Deploy" → "Deploy latest commit"
   - Wait 2-3 minutes
   - Verify with: `curl https://pathfinder-api.onrender.com/health`

---

## 🔄 ALTERNATIVE FIX (10 minutes)

### Option 2: Delete and Recreate Service

If Option 1 doesn't work, create a fresh service:

```bash
# 1. Delete old service in Render dashboard
# Go to: https://dashboard.render.com/web/srv-d6sr8e4hg0os73fdsllg
# Settings → Delete Service

# 2. Create new service via dashboard
# Blueprint: Use render.yaml from repo
# Repository: chadlmc1970/pathfinder
# Branch: main

# 3. Set environment variables in new service:
# - DATABASE_URL: (same as before)
# - ANTHROPIC_API_KEY: (same as before)
# - PYTHON_VERSION: 3.11.15
# - CORS_ORIGINS: https://pathfinder-dashboard.onrender.com,https://pathfinder-mobile.onrender.com

# 4. Wait for deploy, then verify
curl https://pathfinder-api.onrender.com/health
curl https://pathfinder-api.onrender.com/api/v1/careers/
```

---

## ✅ Verification Commands

After fixing, run these to confirm PathFinder is deployed:

```bash
# Should return: {"status":"healthy","service":"pathfinder-api"}
curl https://pathfinder-api.onrender.com/health

# Should return: JSON array with 20 Louisiana careers
curl https://pathfinder-api.onrender.com/api/v1/careers/ | jq '.[0:3]'

# Should NOT return: "Route Solver Test" HTML
curl -I https://pathfinder-api.onrender.com/
```

---

## 📋 After Successful Fix

Once backend is verified:

1. **Update SESSION_WORK.md:**
   ```bash
   cd /Users/I870089/pathfinder
   # Mark Phase 1 as ✅ COMPLETE
   # Remove BLOCKER entries
   git add SESSION_WORK.md
   git commit -m "Phase 1 complete: PathFinder backend live"
   git push origin main
   ```

2. **Continue to Phase 2:**
   - Deploy admin dashboard to Vercel
   - Test mobile app locally

3. **Notify C2 and C3:**
   - They'll see the ✅ in SESSION_WORK.md
   - C2 can start Phase 5.1 (JWT backend)
   - C3 waits for Phase 2 completion

---

## 🆘 If Still Stuck

Check Render logs for errors:
```
https://dashboard.render.com/web/srv-d6sr8e4hg0os73fdsllg/logs
```

Look for:
- "PathFinder Build Script" in logs = CORRECT ✅
- "TSP" or "Route Solver" in logs = WRONG ❌

---

**Current Status:** Waiting for you to fix Render repository connection
**Estimated Time:** 5-10 minutes
**Next Step:** Run Option 1 or Option 2 above
