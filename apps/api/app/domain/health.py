from typing import Literal, TypedDict


class HealthStatus(TypedDict):
    status: Literal["ok"]


def build_health_status() -> HealthStatus:
    return {"status": "ok"}