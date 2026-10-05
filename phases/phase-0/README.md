# Phase 0: Foundation

Phase 0 prepares the local development environment and repository structure for BigBuild. It does not implement product behavior.

## Goal

Make the project ready for incremental development while keeping the mobile app and API as placeholders. This foundation reduces setup friction and gives future work clear ownership boundaries.

## Completed Sub-parts

### 0.1 Local development environment

We reviewed the required toolchain for the planned stack:

- React Native with Expo for mobile
- Python with FastAPI for the API
- Supabase and PostgreSQL for future data services
- Turborepo for monorepo task orchestration
- pnpm 10 for workspace package management

We checked the local machine for installed runtimes and tooling, identified missing and incompatible prerequisites, and documented recommended versions, checks, installation commands, compatibility notes, and a final readiness checklist. pnpm 10 was installed for the monorepo. Platform tooling such as Xcode, Android Studio, Docker, and the Supabase CLI was not added as application code and may still need to be installed before the corresponding development workflows are used.

**Why:** Establish a known baseline before adding app or service code, and avoid mixing machine setup with product implementation.

### 0.2 Repository and Turborepo foundation

We created the BigBuild Git repository and configured a pnpm/Turborepo monorepo with these workspaces:

```text
bigbuild/
├── apps/
│   ├── mobile/
│   └── api/
├── packages/
│   └── shared-types/
├── architecture/
├── infrastructure/
├── phases/
├── package.json
├── pnpm-workspace.yaml
├── turbo.json
├── .gitignore
└── README.md
```

This sub-part includes:

- Root and workspace package manifests
- pnpm workspace configuration and lockfile
- Turborepo task configuration
- Placeholder `build`, `check`, and `dev` scripts so workspace commands run before app functionality exists
- Root README and `.gitignore`
- Git initialization and the `@bigbuild/*` workspace package scope
- Repository name `bigbuild`

**Why:** Give mobile, API, shared types, architecture documentation, infrastructure, and phase records clear places to grow without coupling their future implementation.

**Verification:** `pnpm install`, `pnpm check`, `pnpm build`, and `pnpm dev` completed successfully for the foundation placeholders.

## Intentionally Deferred

Phase 0 does not add AI, nutrition, workout logic, onboarding, food logging, notifications, user memory, adaptation, authentication, database schemas, Supabase integration, FastAPI endpoints, or Expo screens.

## Continuing Phase 0

Document later Phase 0 sub-parts in this folder. For each entry, record what changed, why it was needed, the affected files or commands, how it was verified, and what remains deferred. Do not mark a foundation item complete until its relevant checks pass.
