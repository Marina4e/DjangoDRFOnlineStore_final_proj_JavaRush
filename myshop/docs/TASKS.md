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
- `[x]` Run validation commands successfully in an environment with dependencies installed.

## Phase 2 - Data Model and Admin Foundation

- `[x]` Create `Category` model with `id`, `name`, unique `slug`, nullable self-parent, `created_at`, `updated_at`.
- `[x]` Create `Product` model with `id`, `name`, unique `slug`, `description`, `price`, `category`, `image`, `is_active`, `stock`, `created_at`, `updated_at`.
- `[x]` Add product query helpers for active products, novelty sorting, price sorting, popularity sorting, search, category filtering, and price filtering.
- `[x]` Create `Order` model with `user`, `status`, `total_price`, `shipping_address` or address relation, `created_at`, `updated_at`.
- `[x]` Create `OrderItem` model with `order`, `product`, `quantity`, and purchase-time `price` snapshot.
- `[x]` Create `Review` model with `product`, `user`, `rating`, `comment`, and `created_at`.
- `[x]` Create initial migrations for `products` and `orders`.
- `[ ]` Decide whether to implement `Address` as a separate model; required if account address management needs reusable saved addresses.
- `[ ]` Decide whether to implement `Payment` as a separate model; required if mock payment state needs persistence.
- `[x]` Add database constraints for positive prices, positive stock, positive quantities, review rating 1-5, and valid order statuses.
- `[x]` Add admin screens for products, categories, orders, and reviews.
- `[x]` Add admin search, list filters, useful list displays, and basic ordering.
- `[ ]` Add admin custom actions where they provide clear value.
- `[ ]` Add admin analytics for revenue, top products, and number of orders using aggregations/annotations.
- `[ ]` Configure role-aware admin access rights.

## Phase 3 - Product Catalog Web UI

- `[x]` Build homepage `/` with product catalog entry experience.
- `[x]` Build product list `/products/` with pagination.
- `[x]` Add category filtering.
- `[x]` Add price range filtering.
- `[x]` Add search by product name and description.
- `[x]` Add sorting by price.
- `[x]` Add sorting by popularity.
- `[x]` Add sorting by novelty.
- `[x]` Optimize catalog queries with appropriate `select_related` and annotations for catalog pages.
- `[x]` Use Django Templates, HTMX, Alpine.js, and Tailwind CSS for the new frontend.
- `[x]` Use Hop & Barley only for visual direction; do not copy the old frontend directly.
- `[x]` Add tests for catalog rendering, filtering, search, sorting, and pagination.
- `[x]` Run `graphify .` before implementation only for code structure and use `graphify scope inspect . --scope auto` when the full command stops on semantic corpus detection.
- `[x]` Run validation after implementation.
- `[!]` Run `graphify .` again after implementation if possible; the command still stops on semantic corpus detection after AST scanning.
- `[x]` Update `docs/TASKS.md`.
- `[x]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[x]` Provide the exact local run command.
- `[x]` Provide the exact browser URL.
- `[x]` Provide a short manual QA checklist for the user.
- `[ ]` Provide the next exact prompt for Phase 4.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.

## Phase 4 - Product Detail and Review Display

- `[x]` Build product detail page `/product/<slug>/` with name, description, price, image, rating, reviews, and quantity selection UI.
- `[x]` Show review list and rating display on the product page.
- `[x]` Prepare review-related query behavior without implementing purchase-gated submission yet.
- `[x]` Add tests for product detail rendering and review display behavior.
- `[x]` Run `graphify .` before implementation only for code structure.
- `[x]` Run validation after implementation.
- `[!]` Run `graphify .` again after implementation if possible; the command still stops on semantic corpus detection after AST scanning.
- `[x]` Update `docs/TASKS.md`.
- `[x]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[x]` Provide the exact local run command.
- `[x]` Provide the exact browser URL.
- `[x]` Provide a short manual QA checklist for the user.
- `[ ]` Provide the next exact prompt for Phase 5.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.

## Phase 5 - Cart Web UI

- `[ ]` Implement session-backed cart at `/cart/`.
- `[ ]` Add products to cart with quantity selection.
- `[ ]` Update cart item quantities.
- `[ ]` Remove cart items.
- `[ ]` Calculate cart totals from current product prices.
- `[ ]` Validate product stock before adding/updating cart quantities.
- `[ ]` Show useful Django messages for cart actions and validation failures.
- `[ ]` Add cart tests for add, remove, quantity update, total calculation, session persistence, and stock validation.
- `[ ]` Run `graphify .` before implementation only for code structure.
- `[ ]` Run validation after implementation.
- `[ ]` Run `graphify .` again after implementation if possible.
- `[ ]` Update `docs/TASKS.md`.
- `[ ]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[ ]` Provide the exact local run command.
- `[ ]` Provide the exact browser URL.
- `[ ]` Provide a short manual QA checklist for the user.
- `[ ]` Provide the next exact prompt for Phase 6.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.

## Phase 6 - Checkout Web UI

- `[ ]` Implement checkout page `/checkout/` with contact details and delivery address form.
- `[ ]` Add mock payment method selection.
- `[ ]` Create order records inside a database transaction.
- `[ ]` Create order items with price snapshots.
- `[ ]` Decrease stock or otherwise enforce stock availability at order creation.
- `[ ]` Send email notification to the user.
- `[ ]` Send email notification to the administrator.
- `[ ]` Handle checkout errors and form validation cleanly.
- `[ ]` Add checkout tests for validation, transaction behavior, order creation, order items, stock handling, and email notifications.
- `[ ]` Run `graphify .` before implementation only for code structure.
- `[ ]` Run validation after implementation.
- `[ ]` Run `graphify .` again after implementation if possible.
- `[ ]` Update `docs/TASKS.md`.
- `[ ]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[ ]` Provide the exact local run command.
- `[ ]` Provide the exact browser URL.
- `[ ]` Provide a short manual QA checklist for the user.
- `[ ]` Provide the next exact prompt for Phase 7.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.

## Phase 7 - Authentication and Users

- `[ ]` Implement browser registration with Django session authentication.
- `[ ]` Implement browser login and logout with Django session authentication.
- `[ ]` Implement password change.
- `[ ]` Implement profile editing.
- `[ ]` Implement delivery address management.
- `[ ]` Implement account order history with filtering.
- `[ ]` Ensure account pages require authenticated users.
- `[ ]` Replace any visual-reference localStorage auth simulation with real Django auth state.
- `[ ]` Add tests for registration, login/logout, profile editing, password change, addresses, and order history filtering.
- `[ ]` Run `graphify .` before implementation only for code structure.
- `[ ]` Run validation after implementation.
- `[ ]` Run `graphify .` again after implementation if possible.
- `[ ]` Update `docs/TASKS.md`.
- `[ ]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[ ]` Provide the exact local run command.
- `[ ]` Provide the exact browser URL.
- `[ ]` Provide a short manual QA checklist for the user.
- `[ ]` Provide the next exact prompt for Phase 8.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.

## Phase 8 - REST API and JWT

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
- `[ ]` Add REST API tests for JWT, products, cart, orders, reviews, permissions, and own-data restrictions.
- `[ ]` Run `graphify .` before implementation only for code structure.
- `[ ]` Run validation after implementation.
- `[ ]` Run `graphify .` again after implementation if possible.
- `[ ]` Update `docs/TASKS.md`.
- `[ ]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[ ]` Provide the exact local run command.
- `[ ]` Provide the exact browser URL.
- `[ ]` Provide a short manual QA checklist for the user.
- `[ ]` Provide the next exact prompt for Phase 9.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.

## Phase 9 - Swagger/OpenAPI and Final Coverage Expansion

- `[ ]` Configure Swagger/OpenAPI at `/api/docs/`.
- `[ ]` Document JWT authorization scheme.
- `[ ]` Document access and refresh token formats and refresh process.
- `[ ]` Add request examples for registration, JWT login, products, cart, orders, and reviews.
- `[ ]` Ensure generated schemas match implemented serializers and views.
- `[ ]` Add OpenAPI availability/schema smoke tests.
- `[ ]` Expand final coverage across implemented catalog, detail, cart, checkout, auth, and API behavior.
- `[ ]` Add regression tests that are still missing, including stock and access restrictions.
- `[ ]` Push toward the extended coverage target of at least 80% if time allows.
- `[ ]` Run `graphify .` before implementation only for code structure.
- `[ ]` Run validation after implementation.
- `[ ]` Run `graphify .` again after implementation if possible.
- `[ ]` Update `docs/TASKS.md`.
- `[ ]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[ ]` Provide the exact local run command.
- `[ ]` Provide the exact browser URL.
- `[ ]` Provide a short manual QA checklist for the user.
- `[ ]` Provide the next exact prompt for Phase 10.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.

## Phase 10 - Final Hardening, README, Submission Prep

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
- `[ ]` Run `graphify .` before implementation only for code structure.
- `[ ]` Run validation after implementation.
- `[ ]` Run `graphify .` again after implementation if possible.
- `[ ]` Update `docs/TASKS.md`.
- `[ ]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[ ]` Provide the exact local run command.
- `[ ]` Provide the exact browser URL.
- `[ ]` Provide a short manual QA checklist for the user.
- `[ ]` Provide the next exact prompt for the Bonus Phase if needed.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.

## Bonus Phase - GraphQL Analytics

- `[ ]` Configure a single GraphQL endpoint at `/graphql/`.
- `[ ]` Add authorization rules for analytics access.
- `[ ]` Implement order analytics: revenue, quantity, average order value, and trends.
- `[ ]` Implement product analytics: popular products and stock balances.
- `[ ]` Implement user analytics: activity and repeat purchases.
- `[ ]` Document GraphQL types and example queries.
- `[ ]` Add GraphQL analytics tests.
- `[ ]` Run `graphify .` before implementation only for code structure.
- `[ ]` Run validation after implementation.
- `[ ]` Run `graphify .` again after implementation if possible.
- `[ ]` Update `docs/TASKS.md`.
- `[ ]` Update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- `[ ]` Provide the exact local run command.
- `[ ]` Provide the exact browser URL.
- `[ ]` Provide a short manual QA checklist for the user.
- `[ ]` Wait for the user's manual browser check before marking the phase complete.
