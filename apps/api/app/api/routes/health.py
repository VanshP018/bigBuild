from fastapi import APIRouter

from app.api.schemas.health import HealthResponse
from app.services.health import HealthService

router = APIRouter(tags=["health"])
health_service = HealthService()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse.model_validate(health_service.check())