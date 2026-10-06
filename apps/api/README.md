# BigBuild API

FastAPI foundation for the BigBuild backend. This workspace currently contains only configuration, routing, a health check, and boundaries for future services and persistence.

## Setup

Use Python 3.11 or newer and create a virtual environment from this directory:

```bash
cd apps/api
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

Copy `.env.example` to `.env` only when local configuration overrides are needed.

## Run

From `apps/api/`:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

From the monorepo root, after installing the API environment:

```bash
pnpm --filter @bigbuild/api dev
```

## Health check

```bash
curl http://localhost:8000/api/v1/health
```

Expected response:

```json
{"status":"ok"}
```

The API intentionally does not connect to a database or implement authentication, AI, or product domain logic yet.