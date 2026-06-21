# Tasks

## Status Legend

- `[ ]` not started
- `[~]` in progress
- `[x]` complete
- `[!]` blocked

## Phase 0 - Specification Intake

- `[x]` Read `docs/PROJECT_SPEC.md` as the primary technical assignment.
- `[x]` Read `docs/HOP_AND_BARLEY_REFERENCE.md` as a visual/frontend reference only.
- `[x]` Extract required functional blocks.
- `[x]` Extract required data entities and fields.
- `[x]` Extract required authentication and authorization rules.
- `[x]` Extract required REST API endpoints.
- `[x]` Extract required GraphQL analytics endpoint.
- `[x]` Extract required frontend pages and interactions.
- `[x]` Extract required admin features.
- `[x]` Extract required quality, infrastructure, and documentation requirements.
- `[x]` Update `docs/TASKS.md` with concrete implementation tasks.
- `[x]` Update `docs/ACCEPTANCE_CHECKLIST.md` with concrete acceptance checks.
- `[x]` Refine `docs/TECH_DECISIONS.md` from assignment details.

## Phase 1 - Project Foundation

- `[x]` Fix stale planning notes in `AGENTS.md` and `docs/ACCEPTANCE_CHECKLIST.md`.
- `[x]` Confirm the Django project root and existing app folders are the implementation target.
- `[x]` Create `manage.py` and Django `config` project files.
- `[x]` Configure environment-based Django settings.
- `[x]` Document dependencies in `requirements.txt` without installing them.
- `[x]` Configure PostgreSQL settings through environment variables.
- `[x]` Fill `.env.example` with required non-secret variables.
- `[x]` Configure Dockerfile for the Django app.
- `[x]` Configure Docker Compose with web and PostgreSQL services.
- `[x]` Configure static files, media files, and template directories.
- `[x]` Create basic app shells for `products`, `orders`, `users`, and `api`.
- `[x]` Configure pytest-django.
- `[x]` Configure basic lint and type-check command targets.
- `[x]` Add a project README skeleton with run, test, lint, and API sections.
- `[x]` Add `scripts/validate.ps1`.
- `[ ]` Run validation commands successfully in an environment with dependencies installed.

## Phase 2 - Data Model and Admin Foundation

- `[ ]` Create `Category` model with `id`, `name`, unique `slug`, nullable self-parent, `created_at`, `updated_at`.
- `[ ]` Create `Product` model with `id`, `name`, unique `slug`, `description`, `price`, `category`, `image`, `is_active`, `stock`, `created_at`, `updated_at`.
- `[ ]` Add product query helpers for active products, novelty sorting, price sorting, popularity sorting, search, category filtering, and price filtering.
- `[ ]` Create `Order` model with `user`, `status`, `total_price`, `shipping_address` or address relation, `created_at`, `updated_at`.
- `[ ]` Create `OrderItem` model with `order`, `product`, `quantity`, and purchase-time `price` snapshot.
- `[ ]` Create `Review` model with `product`, `user`, `rating`, `comment`, and `created_at`.
- `[ ]` Decide whether to implement `Address` as a separate model; required if account address management needs reusable saved addresses.
- `[ ]` Decide whether to implement `Payment` as a separate model; required if mock payment state needs persistence.
- `[ ]` Add database constraints for positive prices, positive stock, positive quantities, review rating 1-5, and valid order statuses.
- `[ ]` Add admin screens for products, categories, orders, reviews, and users.
- `[ ]` Add admin search, list filters, useful list displays, and custom actions.
- `[ ]` Add admin analytics for revenue, top products, and number of orders using aggregations/annotations.
- `[ ]` Configure role-aware admin access rights.

## Phase 3 - Web Authentication and Account

- `[ ]` Implement browser registration with Django session authentication.
- `[ ]` Implement browser login and logout with Django session authentication.
- `[ ]` Implement password change.
- `[ ]` Implement profile editing.
- `[ ]` Implement delivery address management.
- `[ ]` Implement account order history with filtering.
- `[ ]` Ensure account pages require authenticated users.
- `[ ]` Replace any visual-reference localStorage auth simulation with real Django auth state.

## Phase 4 - Catalog and Product Web UI

- `[ ]` Build homepage `/` with product catalog entry experience.
- `[ ]` Build product list `/products/` with pagination.
- `[ ]` Add category filtering.
- `[ ]` Add price range filtering.
- `[ ]` Add search by product name and description.
- `[ ]` Add sorting by price.
- `[ ]` Add sorting by popularity.
- `[ ]` Add sorting by novelty.
- `[ ]` Optimize catalog queries with appropriate `select_related`, `prefetch_related`, annotations, and indexes.
- `[ ]` Build product detail page `/product/<slug>/` with name, description, price, image, rating, reviews, add-to-cart button, and quantity selection.
- `[ ]` Implement review submission only for authenticated users who purchased the product.
- `[ ]` Validate review rating from 1 to 5.
- `[ ]` Use Django Templates, HTMX, Alpine.js, and Tailwind CSS for the new frontend.
- `[ ]` Use Hop & Barley only for visual direction; do not copy the old frontend directly.

## Phase 5 - Cart and Checkout Web UI

- `[ ]` Implement session-backed cart at `/cart/`.
- `[ ]` Add products to cart with quantity selection.
- `[ ]` Update cart item quantities.
- `[ ]` Remove cart items.
- `[ ]` Calculate cart totals from current product prices.
- `[ ]` Validate product stock before adding/updating cart quantities.
- `[ ]` Show useful Django messages for cart actions and validation failures.
- `[ ]` Implement checkout page `/checkout/` with contact details and delivery address form.
- `[ ]` Add mock payment method selection.
- `[ ]` Create order records inside a database transaction.
- `[ ]` Create order items with price snapshots.
- `[ ]` Decrease stock or otherwise enforce stock availability at order creation.
- `[ ]` Send email notification to the user.
- `[ ]` Send email notification to the administrator.
- `[ ]` Handle checkout errors and form validation cleanly.

## Phase 6 - REST API

- `[ ]` Configure DRF under `/api/`.
- `[ ]` Configure JWT access and refresh tokens.
- `[ ]` Add API user registration at `POST /api/users/register/`.
- `[ ]` Add API JWT login at `POST /api/users/login/`.
- `[ ]` Add product list endpoint `GET /api/products/` with pagination, filtering, and search.
- `[ ]` Add product detail endpoint `GET /api/products/<id>/`.
- `[ ]` Add order collection endpoint `GET /api/orders/` for the current user's orders.
- `[ ]` Add order create endpoint `POST /api/orders/` based on the current cart.
- `[ ]` Add order detail endpoint `GET /api/orders/<id>/` scoped to the current user's own order.
- `[ ]` Add order update/cancel endpoint `PATCH/PUT/DELETE /api/orders/<id>/` with ownership and status rules.
- `[ ]` Add cart management endpoint `GET/POST/PATCH/DELETE /api/cart/`.
- `[ ]` Add review list/create endpoint `GET/POST /api/products/<id>/reviews/`.
- `[ ]` Enforce that users can view/change only their own API data.
- `[ ]` Add serializers with explicit validation for products, orders, cart items, users, and reviews.
- `[ ]` Add API pagination and permissions.

## Phase 7 - API Documentation

- `[ ]` Configure Swagger/OpenAPI at `/api/docs/`.
- `[ ]` Document JWT authorization scheme.
- `[ ]` Document access and refresh token formats and refresh process.
- `[ ]` Add request examples for registration, JWT login, products, cart, orders, and reviews.
- `[ ]` Ensure generated schemas match implemented serializers and views.

## Phase 8 - GraphQL Analytics

- `[ ]` Configure a single GraphQL endpoint at `/graphql/`.
- `[ ]` Add authorization rules for analytics access.
- `[ ]` Implement order analytics: revenue, quantity, average order value, and trends.
- `[ ]` Implement product analytics: popular products and stock balances.
- `[ ]` Implement user analytics: activity and repeat purchases.
- `[ ]` Document GraphQL types and example queries.

## Phase 9 - Tests

- `[ ]` Add model tests for category, product, order, order item, review, and optional address/payment models.
- `[ ]` Add catalog tests for pagination, category filtering, price filtering, search, and sorting.
- `[ ]` Add product page tests for detail display, reviews, add-to-cart, and purchase-gated review submission.
- `[ ]` Add cart tests for add, remove, quantity update, total calculation, session persistence, and stock validation.
- `[ ]` Add checkout tests for validation, transaction behavior, order creation, order items, stock handling, and email notifications.
- `[ ]` Add account tests for registration, login/logout, profile editing, password change, addresses, and order history filtering.
- `[ ]` Add admin tests for configured management and analytics behavior where practical.
- `[ ]` Add REST API tests for JWT, products, cart, orders, reviews, permissions, and own-data restrictions.
- `[ ]` Add OpenAPI availability/schema smoke tests.
- `[ ]` Add GraphQL analytics tests.
- `[ ]` Add regression test that a user cannot order more products than are in stock.
- `[ ]` Aim for extended coverage target of at least 80% if time allows.

## Phase 10 - Quality, Documentation, and Submission

- `[ ]` Add type annotations to functions and methods.
- `[ ]` Add docstrings for public APIs and important modules.
- `[ ]` Configure flake8 or equivalent linter.
- `[ ]` Configure mypy.
- `[ ]` Ensure tests pass.
- `[ ]` Ensure linters pass without critical errors.
- `[ ]` Ensure mypy passes or document accepted limitations.
- `[ ]` Complete README with project description, Docker startup instructions, API/JWT examples, test/lint commands, and project structure.
- `[ ]` Add implementation checklist with completion marks.
- `[ ]` Prepare deployment link or video demonstration instructions.
- `[ ]` Maintain meaningful commits and branch names such as `feature/...`, `develop/...`, and stable `main`.
