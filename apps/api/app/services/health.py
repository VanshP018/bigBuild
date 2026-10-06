from app.domain.health import HealthStatus, build_health_status


class HealthService:
    def check(self) -> HealthStatus:
        return build_health_status()