# Implementation Plan

## Planning Constraint

This plan follows the technical assignment in `docs/PROJECT_SPEC.md` and the visual-only reference in `docs/HOP_AND_BARLEY_REFERENCE.md`.

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

## Phase 3 - Product Catalog Web UI

Goal: build the core storefront browsing experience before detail, cart, checkout, and account flows.

Planned work:

- Build homepage `/` with product catalog entry experience.
- Build product list `/products/` with pagination.
- Add category filtering.
- Add price range filtering.
- Add search by product name and description.
- Add sorting by price, popularity, and novelty.
- Optimize catalog queries with appropriate ORM loading and query patterns.
- Add tests for catalog rendering, filtering, search, sorting, and pagination.
- Use Django Templates, HTMX, Alpine.js, and Tailwind CSS for the new frontend.

Exit criteria:

- Catalog pages are reachable and responsive.
- Filtering, search, sorting, and pagination work.
- Browser QA is completed by the user.

## Phase 4 - Product Detail and Review Display

Goal: implement product detail presentation and review display before cart and account behavior.

Planned work:

- Build product detail page `/product/<slug>/` with name, description, price, image, rating, reviews, and quantity selection UI.
- Show review list and rating display on the product page.
- Prepare review display and review-related query behavior without implementing purchase-gated submission yet.
- Add tests for product detail rendering and review display behavior.

Exit criteria:

- Product detail pages render the expected assignment fields.
- Review display works correctly.
- Browser QA is completed by the user.

## Phase 5 - Cart Web UI

Goal: implement cart browsing and cart state management before checkout.

Planned work:

- Implement session-backed cart at `/cart/`.
- Add products to cart with quantity selection.
- Update and remove cart items.
- Calculate totals from current product prices.
- Validate stock before cart updates.
- Add tests for cart add/remove/update behavior, totals, and stock validation.

Exit criteria:

- Cart flows work correctly.
- Stock validation is enforced for cart operations.
- Browser QA is completed by the user.

## Phase 6 - Checkout Web UI

Goal: implement checkout and order creation on top of the cart and existing models.

Planned work:

- Implement checkout page `/checkout/` with contact details, delivery address, and mock payment selection.
- Create orders and order items in a database transaction.
- Validate stock before order creation.
- Send user and administrator email notifications.
- Add validation and clear error handling for checkout failures.
- Add tests for checkout validation, order creation, transactions, stock handling, and email behavior.

Exit criteria:

- Checkout flow works correctly.
- Stock validation is enforced at order creation.
- Browser QA is completed by the user.

## Phase 7 - Authentication and Users

Goal: implement user access flows required by the assignment after the storefront flow exists.

Planned work:

- Implement browser registration, login, and logout with Django session authentication.
- Implement password change.
- Implement profile editing.
- Implement account page access control.
- Implement order history with filtering for the authenticated user.
- Implement delivery address management if needed for the account phase.
- Add permissions for user-owned resources and admin-only actions.
- Add tests for authenticated, anonymous, and unauthorized access.

Exit criteria:

- Browser auth and account flows work.
- Role and access rules match the assignment.
- Browser QA is completed by the user.

## Phase 8 - REST API and JWT

Goal: expose required JSON behavior.

Planned work:

- Create serializers with explicit validation.
- Create viewsets or API views.
- Configure JWT access and refresh token behavior.
- Add filtering, search, ordering, and pagination only where required.
- Add API tests for status codes, payloads, validation, and permissions.

Exit criteria:

- Required endpoints are implemented.
- API tests pass.

## Phase 9 - Swagger/OpenAPI and Final Coverage Expansion

Goal: finalize API documentation quality and broaden remaining automated coverage.

Planned work:

- Configure Swagger/OpenAPI at `/api/docs/`.
- Document authorization, schemas, and request examples.
- Ensure generated docs match implemented endpoints and serializers.
- Expand tests and coverage across implemented catalog, product, cart, checkout, account, API, and permission behavior.
- Add regression tests such as stock and access restrictions.

Exit criteria:

- API docs are reachable and accurate.
- Coverage is strong across the implemented core path.
- Browser QA is completed by the user.

## Phase 10 - Final Hardening, README, Submission Prep

Goal: close remaining gaps and prepare the project for delivery.

Planned work:

- Run full pytest suite.
- Run Django checks.
- Verify Docker Compose startup.
- Verify key browser flows manually.
- Review security-sensitive behavior.
- Finalize README with setup, JWT/API usage, tests, linters, and project structure.
- Finalize implementation checklist and submission-readiness details.
- Update documentation if implementation decisions changed.

Exit criteria:

- Acceptance checklist is complete.
- No known critical or high-severity issues remain.
- Project can be run from documented commands.
- User browser QA has been completed for the final integrated flow.

## Bonus Phase - GraphQL Analytics

Goal: implement the assignment's bonus analytics-focused GraphQL endpoint after the core required path is done.

Planned work:

- Configure `/graphql/`.
- Add analytical queries for orders, products, and users.
- Protect GraphQL analytics with appropriate authorization.
- Add GraphQL tests and documentation examples.

Exit criteria:

- GraphQL analytics queries work.
- Browser or API QA is completed by the user.

## Working Rules

- Complete one phase before starting the next unless a dependency requires a small forward adjustment.
- Run `graphify .` before each future implementation phase only to understand code structure.
- Never use Graphify output as a requirements source.
- Keep tests close to the behavior being implemented in every relevant phase rather than postponing all test work to the end.
- Keep UI partials small and named by the fragment they return.
- Avoid broad abstractions until repeated behavior proves they are useful.
- Do not invent missing assignment requirements; stop and ask or document the gap.
- After each future implementation phase, run validation commands, provide the exact local run command, provide the exact browser URL, and provide a short manual QA checklist for the user.
- After each future implementation phase, run `graphify .` again after implementation if possible.
- After each future implementation phase, update `docs/TASKS.md` and update `docs/ACCEPTANCE_CHECKLIST.md` when relevant.
- After each future implementation phase, provide the next exact prompt for the next phase.
- Do not mark a future implementation phase complete until the user confirms the manual browser check.
 - Do not start the next phase automatically.
