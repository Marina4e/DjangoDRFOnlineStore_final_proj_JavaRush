---
name: drf-api-builder
description: Plan or implement Django REST Framework APIs with serializers, views/viewsets, permissions, JWT authentication, filtering, pagination, status codes, and Swagger/OpenAPI documentation. Use for API endpoint design and implementation in this Django online store project.
---

# DRF API Builder

## Core Rule

Implement only API behavior required by `docs/PROJECT_SPEC.md`. Do not derive API requirements from the Hop & Barley visual reference.

If endpoint behavior, payloads, roles, or permissions are missing, document the gap before coding.

## API Design Workflow

1. Read the technical assignment.
2. List resources, actions, roles, and ownership rules.
3. Define endpoint paths and HTTP methods.
4. Define request and response payloads.
5. Choose serializers and validation rules.
6. Choose permissions per endpoint/action.
7. Plan pagination, filtering, search, and ordering only where required.
8. Add OpenAPI coverage.
9. Add pytest API tests.

## DRF Guidelines

- Keep serializers explicit about fields and validation.
- Use DRF permissions for access rules.
- Use consistent HTTP status codes.
- Keep mutation endpoints transactional when multiple writes are involved.
- Avoid exposing internal model fields accidentally.
- Keep API errors predictable for clients.

## JWT Guidelines

- Protect required endpoints with JWT authentication.
- Test anonymous, invalid-token, wrong-user, and allowed-user scenarios.
- Keep browser session auth decisions separate from API JWT decisions.

## Output Expected From This Skill

When asked to plan an API, produce:

- Endpoint table.
- Serializer list.
- Permission matrix.
- Validation rules.
- OpenAPI documentation notes.
- Test matrix.
