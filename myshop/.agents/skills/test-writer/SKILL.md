---
name: test-writer
description: Write or plan pytest-django tests for Django models, forms, template views, HTMX partial responses, DRF APIs, JWT authentication, permissions, validation, and regression coverage in this online store project.
---

# Test Writer

## Core Rule

Tests must reflect the technical assignment. Do not create tests for behavior invented from the visual reference.

## Test Strategy

- Prefer pytest-django.
- Keep tests close to the app behavior under test.
- Cover happy paths and failure paths.
- Test permissions and authentication explicitly.
- Test HTMX partial responses separately from full-page responses.
- Use factories or fixtures once repeated setup appears.

## Coverage Targets

For models:

- Required fields.
- Constraints.
- Relationships.
- Domain methods.
- String representations if meaningful.

For forms and serializers:

- Valid payloads.
- Missing required fields.
- Invalid values.
- Cross-field validation.
- Permission-sensitive fields.

For views and templates:

- Correct status codes.
- Correct template names.
- Context data.
- Redirects and messages after mutations.
- Anonymous and unauthorized behavior.

For HTMX:

- Fragment template returned.
- Correct status code.
- Expected swapped content.
- Validation errors in partial responses.

For DRF APIs:

- Status codes.
- Response payload shape.
- Authentication requirements.
- Permission failures.
- Pagination/filtering/search when required.
- OpenAPI availability where practical.

## Output Expected From This Skill

When asked to plan tests, produce:

- Test file list.
- Fixture/factory needs.
- Test cases grouped by behavior.
- Edge cases.
- Commands to run.
