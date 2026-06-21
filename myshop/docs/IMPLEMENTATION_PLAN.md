# Implementation Plan

## Planning Constraint

Do not implement Django code yet. Do not create models yet. Do not install packages yet.

This plan becomes executable only after `docs/PROJECT_SPEC.md` is filled with the technical assignment.

## Phase 0 - Specification Intake

Goal: turn the technical assignment into a concrete build checklist.

Steps:

1. Read `docs/PROJECT_SPEC.md`.
2. Extract required features, entities, roles, API endpoints, pages, validation rules, and non-functional requirements.
3. Read `docs/HOP_AND_BARLEY_REFERENCE.md` only for frontend mood, layout, typography, and interaction inspiration.
4. Update `docs/TASKS.md` with assignment-specific tasks.
5. Update `docs/ACCEPTANCE_CHECKLIST.md` with assignment-specific checks.
6. Confirm technical decisions that depend on package choices.

Exit criteria:

- No empty or ambiguous core requirements remain.
- Entity list and user flows are documented.
- Implementation tasks are specific enough to code without guessing.

## Phase 1 - Project Foundation

Goal: prepare the Django project and local runtime.

Planned work after implementation is allowed:

- Configure Django settings for environment variables.
- Configure PostgreSQL connection.
- Configure static files and template directories.
- Configure Docker Compose for web and database services.
- Add required packages to dependencies.
- Configure pytest-django.
- Add Swagger/OpenAPI tooling.
- Add JWT auth package.

Exit criteria:

- App starts locally.
- Database connection works.
- Test runner works.
- OpenAPI route is reachable.

## Phase 2 - Data Model and Admin

Goal: implement assignment-approved entities.

Planned work:

- Define models only from the technical assignment.
- Add constraints, indexes, choices, and relations.
- Create migrations.
- Register useful admin screens.
- Add model tests for constraints and string representations.

Exit criteria:

- Migrations apply cleanly.
- Admin can inspect core data.
- Model tests pass.

## Phase 3 - Authentication and Users

Goal: implement user access flows required by the assignment.

Planned work:

- Configure JWT endpoints for API clients.
- Add session-based pages only if browser login is required.
- Add permissions for user-owned resources and admin-only actions.
- Add tests for authenticated, anonymous, and unauthorized access.

Exit criteria:

- Protected API endpoints reject anonymous users.
- Role rules match the assignment.
- Auth tests pass.

## Phase 4 - DRF API

Goal: expose required JSON behavior.

Planned work:

- Create serializers with explicit validation.
- Create viewsets or API views.
- Add filtering, search, ordering, and pagination only where required.
- Document endpoints in OpenAPI.
- Add API tests for status codes, payloads, validation, and permissions.

Exit criteria:

- Required endpoints are implemented.
- Swagger/OpenAPI reflects implemented behavior.
- API tests pass.

## Phase 5 - Template Frontend

Goal: build the server-rendered ecommerce UI.

Planned work:

- Create base layout, navigation, and reusable template partials.
- Build assignment-required pages.
- Use HTMX for partial updates such as filtering, cart changes, form submissions, or pagination where appropriate.
- Use Alpine.js for small local state.
- Apply Tailwind styling aligned with the Hop & Barley visual reference.

Exit criteria:

- Required pages are responsive and accessible.
- Core flows work with server-rendered responses.
- HTMX partials return correct fragments.

## Phase 6 - End-to-End Hardening

Goal: close gaps before final review.

Planned work:

- Run full pytest suite.
- Run Django checks.
- Verify Docker Compose startup.
- Verify key browser flows manually.
- Review OpenAPI docs.
- Review security-sensitive behavior.
- Update documentation if implementation decisions changed.

Exit criteria:

- Acceptance checklist is complete.
- No known critical or high-severity issues remain.
- Project can be run from documented commands.

## Working Rules

- Complete one phase before starting the next unless a dependency requires a small forward adjustment.
- Keep tests close to the behavior being implemented.
- Keep UI partials small and named by the fragment they return.
- Avoid broad abstractions until repeated behavior proves they are useful.
- Do not invent missing assignment requirements; stop and ask or document the gap.
