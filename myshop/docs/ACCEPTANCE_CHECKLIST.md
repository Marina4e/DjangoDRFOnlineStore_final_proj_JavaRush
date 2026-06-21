# Acceptance Checklist

## Phase 0 - Planning Gate

- `[x]` `docs/PROJECT_SPEC.md` contains the technical assignment.
- `[x]` `docs/HOP_AND_BARLEY_REFERENCE.md` contains visual reference material.
- `[x]` Requirements were extracted into concrete tasks.
- `[x]` Acceptance checks were updated from the assignment.
- `[x]` Technical decisions were refined from the assignment.
- `[x]` No Django implementation code was created during Phase 0.
- `[x]` No models or migrations were created during Phase 0.
- `[x]` No packages were installed during Phase 0.

## Source Boundaries

- `[ ]` The technical assignment remains the source of functional/backend requirements.
- `[ ]` Hop & Barley is used only as a visual/frontend reference.
- `[ ]` The old static frontend is not copied directly.
- `[ ]` The new frontend is built with Django Templates, HTMX, Alpine.js, and Tailwind CSS.

## Infrastructure Acceptance

- `[ ]` The project starts with `docker-compose up` on a clean system.
- `[ ]` Docker Compose runs both the Django application and PostgreSQL database.
- `[ ]` PostgreSQL is the configured database.
- `[ ]` Required environment variables are documented in `.env.example` or README.
- `[ ]` Dependencies are documented in `requirements.txt` or `pyproject.toml`.
- `[ ]` Static and media files are configured for local development.

## Data Model Acceptance

- `[ ]` `Category` has `id`, `name`, unique `slug`, nullable parent category, `created_at`, and `updated_at`.
- `[ ]` `Product` has `id`, `name`, unique `slug`, `description`, `price`, `category`, `image`, `is_active`, `stock`, `created_at`, and `updated_at`.
- `[ ]` `Order` has `user`, `status`, `total_price`, shipping address data, `created_at`, and `updated_at`.
- `[ ]` `OrderItem` has `order`, `product`, `quantity`, and purchase-time price snapshot.
- `[ ]` `Review` has `product`, `user`, rating 1-5, `comment`, and `created_at`.
- `[ ]` Optional `Address` model exists if reusable delivery address management needs it.
- `[ ]` Optional `Payment` model exists if mock payment state needs persistence.
- `[ ]` Constraints prevent invalid prices, quantities, stock values, ratings, and statuses.

## Catalog Acceptance

- `[ ]` Homepage `/` is available.
- `[ ]` Product list `/products/` is available.
- `[ ]` Product list has pagination.
- `[ ]` Product list filters by category.
- `[ ]` Product list filters by price range.
- `[ ]` Product list searches by name and description.
- `[ ]` Product list sorts by price.
- `[ ]` Product list sorts by popularity.
- `[ ]` Product list sorts by novelty.
- `[ ]` Catalog queries are optimized enough to avoid obvious N+1 queries.

## Product Page and Reviews Acceptance

- `[ ]` Product detail page `/product/<slug>/` is available.
- `[ ]` Product page displays name, description, price, image, rating, and reviews.
- `[ ]` Product page includes add-to-cart and quantity controls.
- `[ ]` Review rating is limited to 1-5.
- `[ ]` Reviews can be submitted only by authenticated users who purchased the product.
- `[ ]` Users who did not purchase the product cannot submit a review.

## Cart Acceptance

- `[ ]` Cart page `/cart/` is available.
- `[ ]` Cart data is stored in the Django session.
- `[ ]` Users can add products to the cart.
- `[ ]` Users can remove products from the cart.
- `[ ]` Users can change product quantities.
- `[ ]` Cart totals are calculated correctly.
- `[ ]` Cart operations validate product stock.
- `[ ]` A user cannot order more products than are available in stock.
- `[ ]` Cart actions use helpful messages or inline validation feedback.

## Checkout Acceptance

- `[ ]` Checkout page `/checkout/` is available.
- `[ ]` Checkout collects contact details and delivery address.
- `[ ]` Checkout includes mock payment method selection.
- `[ ]` Checkout validates form input.
- `[ ]` Checkout creates an order record in the database.
- `[ ]` Checkout creates order items with price snapshots.
- `[ ]` Checkout handles stock availability inside the order creation flow.
- `[ ]` Checkout uses a database transaction for order creation.
- `[ ]` Email notification is sent to the user.
- `[ ]` Email notification is sent to the administrator.
- `[ ]` Checkout errors are handled clearly.

## Account Acceptance

- `[ ]` Registration works through the web interface with Django session auth.
- `[ ]` Login works through the web interface with Django session auth.
- `[ ]` Logout works through the web interface with Django session auth.
- `[ ]` Password change works.
- `[ ]` Profile editing works.
- `[ ]` Delivery address management works.
- `[ ]` Order history is available in `/account/`.
- `[ ]` Order history supports filtering.
- `[ ]` Account pages enforce access control.

## Admin Acceptance

- `[ ]` Django admin is available at `/admin/`.
- `[ ]` Admin can manage products.
- `[ ]` Admin can manage categories.
- `[ ]` Admin can manage orders.
- `[ ]` Admin can manage reviews.
- `[ ]` Admin can manage users.
- `[ ]` Admin includes search and filters.
- `[ ]` Admin includes useful custom actions.
- `[ ]` Admin analytics show revenue.
- `[ ]` Admin analytics show top products.
- `[ ]` Admin analytics show number of orders.
- `[ ]` Admin access rights are configured for different roles.

## REST API Acceptance

- `[ ]` REST API is available under `/api/`.
- `[ ]` JWT access and refresh token mechanism works.
- `[ ]` `POST /api/users/register/` creates an account.
- `[ ]` `POST /api/users/login/` returns access and refresh tokens.
- `[ ]` `GET /api/products/` lists products with pagination, filtering, and search.
- `[ ]` `GET /api/products/<id>/` returns product information.
- `[ ]` `GET /api/orders/` returns the current user's orders.
- `[ ]` `POST /api/orders/` creates an order based on the cart.
- `[ ]` `GET /api/orders/<id>/` returns only the current user's own order detail.
- `[ ]` `PATCH/PUT/DELETE /api/orders/<id>/` updates or cancels orders according to permission/status rules.
- `[ ]` `GET/POST/PATCH/DELETE /api/cart/` manages cart contents.
- `[ ]` `GET/POST /api/products/<id>/reviews/` lists and creates reviews.
- `[ ]` Users can view or change only their own API data.
- `[ ]` API validation errors are explicit and consistent.

## API Documentation Acceptance

- `[ ]` Swagger/OpenAPI documentation is available at `/api/docs/`.
- `[ ]` API docs include request examples.
- `[ ]` API docs describe JWT authorization.
- `[ ]` API docs describe access token, refresh token, and refresh flow.
- `[ ]` API docs schemas match implemented serializers.

## GraphQL Acceptance

- `[ ]` GraphQL is available through a single endpoint `/graphql/`.
- `[ ]` GraphQL analytics are protected by appropriate authorization.
- `[ ]` Order analytics include revenue, quantity, average order value, and trends.
- `[ ]` Product analytics include popular products and stock balances.
- `[ ]` User analytics include activity and repeat purchases.
- `[ ]` README or API docs include GraphQL types and example queries.

## Frontend Acceptance

- `[ ]` Frontend uses Django Templates as the primary rendering layer.
- `[ ]` HTMX is used for server-rendered partial updates where appropriate.
- `[ ]` Alpine.js is limited to local UI state.
- `[ ]` Tailwind CSS styles the templates.
- `[ ]` Visual styling is inspired by Hop & Barley but not copied directly.
- `[ ]` Pages are responsive across mobile and desktop.
- `[ ]` Forms show useful validation errors.
- `[ ]` Core flows do not rely on localStorage auth simulation.

## Testing Acceptance

- `[ ]` pytest-django is configured.
- `[ ]` Tests cover catalog, filters, search, sorting, and pagination.
- `[ ]` Tests cover product detail and review restrictions.
- `[ ]` Tests cover cart behavior and stock validation.
- `[ ]` Tests cover checkout, order creation, transactions, and emails.
- `[ ]` Tests cover registration, login/logout, account editing, password change, addresses, and order history.
- `[ ]` Tests cover REST API JWT auth, permissions, and own-data restrictions.
- `[ ]` Tests cover GraphQL analytics.
- `[ ]` Tests cover the restriction that users cannot order more products than are in stock.
- `[ ]` Extended test coverage target is at least 80% if time allows.

## Code Quality Acceptance

- `[ ]` Important functions and methods include type annotations.
- `[ ]` Public APIs and important modules include docstrings.
- `[ ]` flake8 or equivalent linter is configured.
- `[ ]` mypy is configured.
- `[ ]` Linters pass without critical errors.
- `[ ]` Tests pass successfully.

## Documentation and Submission Acceptance

- `[ ]` README contains project description.
- `[ ]` README contains Docker installation and startup instructions.
- `[ ]` README contains API usage examples including JWT.
- `[ ]` README contains test and lint commands.
- `[ ]` README describes project structure.
- `[ ]` README or docs describe GraphQL example queries.
- `[ ]` Implementation checklist with completion marks is included.
- `[ ]` Repository has meaningful commits and branch usage.
- `[ ]` Deployment link or video demonstration is prepared for submission.
