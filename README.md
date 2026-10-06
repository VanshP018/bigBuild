# BigBuild

Foundation monorepo for the BigBuild AI personal health coach application.

## Scope

This repository currently contains only the Phase 0 foundation:

- Turborepo workspace configuration
- Expo TypeScript mobile application foundation
- FastAPI backend foundation
- Shared types workspace placeholder
- Infrastructure directory

Mobile, API, AI, nutrition, workout, database, authentication, notifications, memory, and adaptation functionality will be added in later tasks.

## Repository layout

```text
apps/mobile          Mobile application workspace
apps/api             Backend API workspace
packages/shared-types Cross-project types workspace
infrastructure       Deployment and infrastructure configuration location
```

## Package manager

This repository uses pnpm 10 because it provides reliable workspace support and efficient dependency storage for Turborepo.

## Requirements

- Node.js 22 LTS or newer supported LTS release
- pnpm 10
- Python 3.11 or newer for the API

Supabase, PostgreSQL, authentication, and product features are intentionally not configured in this foundation task.

## Commands

Install workspace dependencies:

```bash
pnpm install
```

Run the foundation checks:

```bash
pnpm check
```

Run the foundation build:

```bash
pnpm build
```

Run the mobile Expo development server:

```bash
pnpm --filter @bigbuild/mobile dev
```

Run the API development server after creating and activating `apps/api/.venv`:

```bash
pnpm --filter @bigbuild/api dev
```

Run all workspace development tasks:

```bash
pnpm dev
```