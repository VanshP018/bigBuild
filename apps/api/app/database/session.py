"""Database session boundary; persistence is intentionally not configured yet."""


def database_not_configured() -> None:
    """Keep database setup explicit until the database phase begins."""
    return None