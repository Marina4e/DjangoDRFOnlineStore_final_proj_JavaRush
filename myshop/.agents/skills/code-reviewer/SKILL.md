---
name: code-reviewer
description: Review Django, DRF, HTMX, Alpine.js, Tailwind, Docker, and pytest changes for assignment compliance, security, regressions, missing tests, permission bugs, API contract issues, and frontend quality in this online store project.
---

# Code Reviewer

## Review Priority

Lead with findings. Order by severity. Include file and line references when possible.

## Source Priority

1. `docs/PROJECT_SPEC.md`
2. User instructions
3. `docs/TECH_DECISIONS.md`
4. `docs/IMPLEMENTATION_PLAN.md`
5. `docs/HOP_AND_BARLEY_REFERENCE.md` for visual direction only

## What To Check

- Functional behavior matches the technical assignment.
- No behavior is sourced only from the visual reference.
- Models enforce required constraints.
- API serializers do not expose unintended fields.
- Permissions protect user-owned and restricted resources.
- JWT-authenticated endpoints reject anonymous or invalid access.
- Forms and serializers validate user input.
- HTMX endpoints return appropriate full or partial responses.
- Alpine.js does not hold business-critical state.
- Tailwind UI is responsive and accessible.
- Tests cover important success and failure paths.
- Docker and environment setup are reproducible.
- Swagger/OpenAPI docs match implemented endpoints.

## Finding Format

Use this structure:

- Severity.
- File and line.
- Problem.
- Impact.
- Suggested fix.

If no issues are found, say so clearly and mention any residual risk or untested area.

## Severity Guide

- Critical: data loss, auth bypass, secret leak, app cannot run.
- High: major required behavior broken, permission bug, API contract break.
- Medium: edge case failure, missing validation, incomplete tests for important behavior.
- Low: maintainability, polish, minor accessibility or consistency issue.
