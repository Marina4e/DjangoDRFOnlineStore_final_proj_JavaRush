# AGENTS.md

## Project Boundary

This repository is for a Django online store built with:

- Django
- Django REST Framework
- JWT authentication
- PostgreSQL
- Docker Compose
- pytest-django
- Swagger/OpenAPI
- Django Templates
- HTMX
- Alpine.js
- Tailwind CSS

The technical assignment in `docs/PROJECT_SPEC.md` is the main source of product and backend requirements.
The Hop & Barley document in `docs/HOP_AND_BARLEY_REFERENCE.md` is only a visual/frontend reference.

Current planning note: both source documents are present but empty. Do not implement business behavior until `docs/PROJECT_SPEC.md` contains the actual assignment.

## Non-Negotiable Rules

- Do not treat the visual reference as a functional specification.
- Do not create Django models, migrations, serializers, views, templates, or package installs during planning-only tasks.
- Do not invent product rules that are absent from the technical assignment.
- Keep frontend behavior progressively enhanced: server-rendered templates first, HTMX for partial updates, Alpine.js for local UI state only.
- Keep API behavior explicit and testable with DRF serializers, permissions, JWT flows, and OpenAPI documentation.
- Prefer small, focused commits by phase once implementation begins.

## Project Roles

- `django-htmx-architect`: designs the Django app structure, server-rendered pages, HTMX boundaries, URLs, forms, and template organization.
- `tailwind-ui-builder`: builds Tailwind/Django template UI using the Hop & Barley reference only for visual tone.
- `drf-api-builder`: builds DRF serializers, viewsets/views, permissions, JWT auth flows, and Swagger/OpenAPI coverage.
- `test-writer`: creates pytest-django tests for models, views, API behavior, permissions, and HTMX responses.
- `code-reviewer`: reviews implementation for assignment compliance, security, regressions, and missing tests.

## Expected Workflow

1. Confirm `docs/PROJECT_SPEC.md` is filled with the technical assignment.
2. Update `docs/TECH_DECISIONS.md` only when a decision has a clear reason.
3. Follow `docs/IMPLEMENTATION_PLAN.md` phase by phase.
4. Work from `docs/TASKS.md`; keep task status current.
5. Validate against `docs/ACCEPTANCE_CHECKLIST.md` before calling the project complete.

## Quality Bar

- All protected actions require authentication and permission checks.
- All user input is validated by forms or serializers.
- API responses use consistent status codes and error shapes.
- Templates remain accessible, responsive, and usable without JavaScript for core flows where practical.
- Tests cover happy paths, validation failures, permission failures, and important edge cases.
- Docker Compose must run the app with PostgreSQL without depending on local services.

# Agent instructions

Always use Context7 MCP when working with Django, HTMX, Alpine.js, Tailwind CSS, Python packages, or any library-specific code.

Always use OpenAI Developer Docs MCP when working with OpenAI API, Codex configuration, Agents SDK, or OpenAI-related documentation.

Use Playwright MCP to test frontend behavior: pages, forms, buttons, navigation, HTMX updates, and UI bugs.

Do not rewrite the whole project without a plan.
First read PROJECT_SPEC.md, then create or update TASKS.md.
Work in small steps.
After each change, explain what files were changed and how to test them.