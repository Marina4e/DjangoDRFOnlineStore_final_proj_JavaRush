# Technical Decisions

## Status

Phase 0 requirements extraction is complete. This document records implementation decisions only; it does not authorize code changes by itself.

No Django code, models, migrations, package installs, or Docker changes were made during Phase 0.

## Source Priority

1. `docs/PROJECT_SPEC.md` - primary technical assignment and functional/backend requirements.
2. User instructions in the current task - stack and phase constraints.
3. `docs/HOP_AND_BARLEY_REFERENCE.md` - visual/frontend reference only.
4. Existing project structure - naming and organization guidance.

If sources conflict, follow the technical assignment unless the user gives a newer explicit instruction.

## Backend Framework

Use Django as the main web framework.

Use Django session authentication for browser-facing web flows:

- Registration.
- Login/logout.
- Account pages.
- Checkout/account access control.

Use Django REST Framework for external JSON APIs under `/api/`.

Use JWT only for external API authorization, with access and refresh tokens.

## Database

Use PostgreSQL as the required database.

Model design must include at minimum:

- `Category`
- `Product`
- `Order`
- `OrderItem`
- `Review`

Optional models are allowed when they simplify required behavior:

- `Address` for saved delivery addresses.
- `Payment` for persisted mock payment state.

Use constraints for money, quantity, stock, rating, and status rules where practical.

## Cart and Checkout

Use Django sessions for the browser cart.

Create orders from the cart using database transactions to keep order records, order items, stock validation, and price snapshots consistent.

Payment is a mock/imitation flow. Do not integrate a real payment provider unless a later instruction explicitly asks for it.

Email notifications are required for the user and administrator during checkout.

## REST API

Use DRF serializers, permissions, and views/viewsets for API behavior.

Required endpoint groups:

- Products: list and detail.
- Orders: create, own list, own detail, update/cancel.
- Users: registration and JWT login.
- Cart: get/add/update/delete contents.
- Reviews: list and create for a product.

Users can view or change only their own API data unless staff/admin permissions explicitly allow more.

## API Documentation

Expose Swagger/OpenAPI documentation at `/api/docs/`.

Preferred package for implementation: `drf-spectacular`, because it is actively used with DRF and produces OpenAPI 3 schemas. `drf-yasg` remains acceptable if project constraints require it.

Document:

- Request examples.
- Data schemas.
- JWT authorization process.
- Access token, refresh token, and refresh flow.

## GraphQL

GraphQL analytics should be treated as a bonus phase, not part of the core required implementation path.

Expose a single endpoint at `/graphql/`.

Preferred package for implementation: `graphene-django`, matching the assignment's key topic.

GraphQL should focus on analytics, not duplicate the full REST API:

- Orders: revenue, quantity, average order value, trends.
- Products: popular products, stock balances.
- Users: activity, repeat purchases.

Protect analytics with appropriate authorization, likely staff/admin only unless the assignment is later narrowed.

## Frontend

Build a new frontend with:

- Django Templates.
- HTMX.
- Alpine.js.
- Tailwind CSS.

Do not copy the old Hop & Barley static frontend directly.

Use Hop & Barley only for visual direction: layout ideas, retail tone, spacing, typography, product cards, forms, and admin/account visual patterns.

Replace visual-reference localStorage login/logout simulation with real Django session authentication.

Use HTMX for server-rendered partial updates such as filtering, cart quantity changes, cart removal, form fragments, and pagination where useful.

Use Alpine.js only for local UI state such as menus, tabs, accordions, disclosure panels, and small controls.

## Project Structure

Use a modular Django structure close to the assignment:

- `config` for settings, root URLs, ASGI/WSGI.
- `products` for catalog, categories, product pages, product serializers/forms/admin.
- `orders` for cart, checkout, orders, order items, order serializers/forms/admin.
- `users` for registration, profile, account, authentication, addresses.
- `reviews` as a separate app only if keeping review ownership separate is clearer; otherwise reviews may live in `products`.
- `payments` only if mock payment state needs its own module.
- `api` only for cross-app API routing/documentation composition.
- `graphql` or `analytics` for schema and resolvers.
- `templates`, `static`, and `tests` for shared presentation assets and tests.

Favor separation of concerns and readability over matching the suggested tree exactly.

## Dependencies

No packages are installed during Phase 0.

Phase 1 should document dependencies before installation. Expected dependency categories:

- Django.
- Django REST Framework.
- PostgreSQL driver.
- JWT auth package, preferably `djangorestframework-simplejwt`.
- Swagger/OpenAPI package, preferably `drf-spectacular`.
- GraphQL package, preferably `graphene-django`.
- pytest and pytest-django.
- flake8 or equivalent linter.
- mypy.
- Image handling support for product images.
- Email/backend configuration support as needed.
- Tailwind/HTMX/Alpine integration approach.

Use `requirements.txt` unless the user chooses `pyproject.toml`, Poetry, uv, or another dependency manager before Phase 1 implementation.

## Testing

Use pytest-django.

Required coverage areas:

- Catalog, search, filters, sorting, and pagination.
- Product detail and review purchase verification.
- Session cart behavior and stock validation.
- Checkout order creation, transactions, price snapshots, stock handling, and emails.
- Registration, login/logout, password change, profile editing, addresses, and order history.
- DRF API JWT auth, permissions, validation, and own-data restrictions.
- Swagger/OpenAPI availability.
- GraphQL analytics and authorization.
- Admin analytics where practical.

Extended target: at least 80% coverage if time allows.

## Quality and Documentation

Use type annotations for functions and methods where practical.

Add docstrings for public APIs and important modules.

Configure flake8 or an equivalent linter.

Configure mypy.

README must include:

- Project description.
- Docker installation and startup instructions.
- API usage examples including JWT.
- Commands for tests and linters.
- Project structure description.
- GraphQL examples or links to GraphQL documentation.

## Open Decisions For Phase 1

- Choose exact dependency file format: keep `requirements.txt` or switch to `pyproject.toml`.
- Choose exact Tailwind integration method.
- Decide whether `Review` is part of `products` or a separate `reviews` app.
- Decide whether saved delivery addresses require a dedicated `Address` model.
- Decide whether mock payments require a dedicated `Payment` model.
- Decide staff/admin-only policy for GraphQL analytics.
