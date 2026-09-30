from datetime import datetime, timezone

from fastapi import APIRouter

from internal.config.settings import settings
from internal.service.health_service import get_health_info

router = APIRouter(prefix="/api/v1", tags=["Health"])

START_TIME = datetime.now(timezone.utc)


@router.get("/health", status_code=200)
def health_check():
    uptime = get_health_info(START_TIME)

    return {
        "status": "ok",
        "name": settings.app_name,
        "version": settings.app_version,
        "uptime": uptime,
    }
