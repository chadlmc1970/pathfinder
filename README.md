# PathFinder

**TikTok-style career discovery for Louisiana 8th graders**

PathFinder is a mobile-first career exploration platform that helps Louisiana 8th graders discover careers through short-form video content. Students swipe through 15-30 second clips of real Louisiana workers, building their "Interest DNA" profile while AI recommendations align their interests with Louisiana workforce priorities.

## 🎯 Core Innovation

Bottom-up discovery (student interests) meets top-down workforce alignment (Louisiana economic priorities) through Claude 4.6-powered recommendations.

## 🏗️ Architecture

- **Mobile:** React Native with Expo (iOS first, Android later)
- **Backend:** FastAPI (Python 3.11+) on Render
- **Database:** Neon PostgreSQL (serverless)
- **Admin Dashboard:** Next.js 16 (App Router) on Vercel
- **Video Storage:** Vercel Blob (CDN-backed)
- **AI:** Claude 4.6 via Anthropic API (OIDC auth)
- **Auth:** Clerk (Vercel Marketplace integration)

## 📂 Repository Structure

```
pathfinder/
├── mobile/                 # React Native (Expo) - iOS app
├── backend/                # FastAPI - API server
├── admin-dashboard/        # Next.js 16 - Content management
├── docs/                   # Documentation
├── scripts/                # Deployment scripts
└── README.md
```

## 🚀 Quick Start

See individual README files in each workspace directory for setup instructions.

## 📊 Success Metrics (Pilot KPIs)

- 60%+ weekly active usage
- 5+ min avg session duration
- 10+ careers viewed per session
- 30% save rate on viewed careers
- 70% retention within 7 days

## 🎓 Target Audience

Louisiana 8th graders (100-500 students pilot → statewide scale)

## 📝 License

All rights reserved.
