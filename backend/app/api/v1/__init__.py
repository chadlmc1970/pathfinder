from fastapi import APIRouter
from app.api.v1 import careers, videos, engagement, users, recommendations

router = APIRouter()

# Include API routers
router.include_router(careers.router, prefix="/careers", tags=["careers"])
router.include_router(videos.router, prefix="/videos", tags=["videos"])
router.include_router(engagement.router, prefix="/engagement", tags=["engagement"])
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
