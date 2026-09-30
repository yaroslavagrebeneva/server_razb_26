from fastapi import FastAPI

from internal.config.settings import settings
from internal.controller.health_controller import router as health_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend service веб-системы CheckIn для учета посещаемости студентов.",
)

app.include_router(health_router)


@app.get("/", tags=["System"])
def root():
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "message": "CheckIn Backend Service is running",
    }
