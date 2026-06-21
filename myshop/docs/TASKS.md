# Tasks

## Status Legend

- `[ ]` not started
- `[~]` in progress
- `[x]` complete
- `[!]` blocked

## Current Blocker

- `[!]` Fill `docs/PROJECT_SPEC.md` with the technical assignment. The current file is empty, so implementation tasks cannot be made assignment-specific yet.
- `[!]` Fill `docs/HOP_AND_BARLEY_REFERENCE.md` if visual guidance should be used. The current file is empty, so frontend reference details cannot be applied yet.

## Planning Tasks

- `[x]` Create project agent instructions in `AGENTS.md`.
- `[x]` Create technical decision log in `docs/TECH_DECISIONS.md`.
- `[x]` Create phased implementation plan in `docs/IMPLEMENTATION_PLAN.md`.
- `[x]` Create task tracker in `docs/TASKS.md`.
- `[x]` Create acceptance checklist in `docs/ACCEPTANCE_CHECKLIST.md`.
- `[x]` Create local skills for architecture, UI, API, tests, and review.

## Specification Intake Tasks

- `[ ]` Extract required domain entities from the technical assignment.
- `[ ]` Extract required user roles and permission rules.
- `[ ]` Extract required frontend pages and user flows.
- `[ ]` Extract required API endpoints and payloads.
- `[ ]` Extract required validation rules.
- `[ ]` Extract required admin behavior.
- `[ ]` Extract required test/acceptance criteria.
- `[ ]` Convert extracted requirements into model, API, frontend, and test tasks.

## Backend Foundation Tasks

- `[ ]` Confirm exact dependency list after package installation is allowed.
- `[ ]` Configure Django settings for environment-based configuration.
- `[ ]` Configure PostgreSQL.
- `[ ]` Configure Docker Compose services.
- `[ ]` Configure pytest-django.
- `[ ]` Configure Swagger/OpenAPI.
- `[ ]` Configure JWT authentication.

## Data Model Tasks

- `[ ]` Design models from the technical assignment.
- `[ ]` Review model design before creating migrations.
- `[ ]` Implement models.
- `[ ]` Create migrations.
- `[ ]` Register admin screens.
- `[ ]` Add model tests.

## API Tasks

- `[ ]` Define serializer contracts.
- `[ ]` Define URL structure.
- `[ ]` Implement DRF views/viewsets.
- `[ ]` Add permissions.
- `[ ]` Add filtering/search/pagination where required.
- `[ ]` Add OpenAPI annotations where needed.
- `[ ]` Add API tests.

## Frontend Tasks

- `[ ]` Define base template structure.
- `[ ]` Define Tailwind design tokens from visual reference.
- `[ ]` Build shared layout and navigation.
- `[ ]` Build required pages.
- `[ ]` Build HTMX partials for assignment-approved interactions.
- `[ ]` Add Alpine.js for local UI state where useful.
- `[ ]` Add template and HTMX response tests.

## Quality Tasks

- `[ ]` Run Django system checks.
- `[ ]` Run pytest.
- `[ ]` Verify Docker Compose startup.
- `[ ]` Verify Swagger/OpenAPI route.
- `[ ]` Review security and permission behavior.
- `[ ]` Complete `docs/ACCEPTANCE_CHECKLIST.md`.

# Project verification checklist

1. Run:
   python manage.py check

2. Run:
   python manage.py makemigrations --check --dry-run

3. Run:
   python manage.py test

4. Start server:
   python manage.py runserver

5. Open in browser:
   http://127.0.0.1:8000/

6. Check main pages, admin, API endpoints, forms, and errors.