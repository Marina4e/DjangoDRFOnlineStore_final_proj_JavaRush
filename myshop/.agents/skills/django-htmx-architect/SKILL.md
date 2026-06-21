---
name: django-htmx-architect
description: Design Django server-rendered architecture with Django Templates, HTMX, Alpine.js boundaries, URL structure, forms, views, template partials, and project organization. Use when planning or implementing Django template pages, HTMX interactions, server-rendered workflows, or app structure for this online store project.
---

# Django HTMX Architect

## Core Rule

Use `docs/PROJECT_SPEC.md` as the source of functional requirements. Use `docs/HOP_AND_BARLEY_REFERENCE.md` only for visual/frontend inspiration.

If the technical assignment is empty or ambiguous, stop before implementation and document the missing requirement.

## Architecture Priorities

- Prefer Django Templates for primary page rendering.
- Use HTMX for partial server updates, not for hidden client-side business logic.
- Use Alpine.js only for small local UI state.
- Keep URLs, views, forms, and templates grouped by feature.
- Keep reusable template fragments in clearly named partial files.
- Make the non-JavaScript server flow understandable where practical.

## Design Workflow

1. Read the technical assignment.
2. Extract pages, forms, user flows, roles, and permissions.
3. Identify full-page views and HTMX partial views.
4. Define URL names before writing views.
5. Choose Django forms for browser-submitted input.
6. Plan templates and partials.
7. List tests for full-page and HTMX responses.

## HTMX Guidelines

- Return fragments for HTMX requests and full pages for normal requests.
- Use clear partial names such as `_product_grid.html`, `_cart_summary.html`, or `_form_errors.html`.
- Validate all input server-side.
- Keep redirects and messages explicit after mutations.
- Avoid duplicating business rules in JavaScript.

## Output Expected From This Skill

When asked to plan architecture, produce:

- App/module responsibilities.
- URL map.
- View list.
- Template and partial list.
- Form list.
- HTMX interaction list.
- Tests to write.
