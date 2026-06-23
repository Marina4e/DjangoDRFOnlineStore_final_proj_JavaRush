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

- `[x]` The technical assignment remains the source of functional/backend requirements.
- `[x]` Hop & Barley is used only as a visual/frontend reference.
- `[x]` The old static frontend is not copied directly.
- `[x]` The new frontend is built with Django Templates, HTMX, Alpine.js, and Tailwind CSS.

## Infrastructure Acceptance

- `[x]` The project starts with `docker-compose up` on a clean system.
- `[x]` Docker Compose configuration exists for both the Django application and PostgreSQL database.
- `[x]` PostgreSQL is the configured database.
- `[x]` Required environment variables are documented in `.env.example` or README.
- `[x]` Dependencies are documented in `requirements.txt`.
- `[x]` Static and media files are configured for local development.
- `[x]` `manage.py`, `config/settings.py`, `config/urls.py`, `config/asgi.py`, and `config/wsgi.py` exist.
- `[x]` Basic app shells exist for `products`, `orders`, `users`, and `api`.
- `[x]` pytest-django configuration exists.
- `[x]` Basic lint and type-check configuration exists.
- `[x]` Validation script exists at `scripts/validate.ps1`.

## Data Model Acceptance

- `[ ]` `Category` has `id`, `name`, unique `slug`, nullable parent category, `created_at`, and `updated_at`.
- `[ ]` `Product` has `id`, `name`, unique `slug`, `description`, `price`, `category`, `image`, `is_active`, `stock`, `created_at`, and `updated_at`.
- `[ ]` `Order` has `user`, `status`, `total_price`, shipping address data, `created_at`, and `updated_at`.
- `[ ]` `OrderItem` has `order`, `product`, `quantity`, and purchase-time price snapshot.
- `[ ]` `Review` has `product`, `user`, rating 1-5, `comment`, and `created_at`.
- `[x]` Optional `Address` model exists if reusable delivery address management needs it.
- `[ ]` Optional `Payment` model exists if mock payment state needs persistence.
- `[ ]` Constraints prevent invalid prices, quantities, stock values, ratings, and statuses.

## Catalog Acceptance

- `[x]` Homepage `/` is available.
- `[x]` Product list `/products/` is available.
- `[x]` Product list has pagination.
- `[x]` Product list filters by category.
- `[x]` Product list filters by price range.
- `[x]` Product list searches by name and description.
- `[x]` Product list sorts by price.
- `[x]` Product list sorts by popularity.
- `[x]` Product list sorts by novelty.
- `[x]` Catalog queries are optimized enough to avoid obvious N+1 queries.

## Product Page and Reviews Acceptance

- `[x]` Product detail page `/product/<slug>/` is available.
- `[x]` Product page displays name, description, price, image, rating, and reviews.
- `[x]` Product page includes add-to-cart and quantity controls.
- `[x]` Review rating is limited to 1-5.
- `[ ]` Reviews can be submitted only by authenticated users who purchased the product.
- `[ ]` Users who did not purchase the product cannot submit a review.

## Cart Acceptance

- `[x]` Cart page `/cart/` is available.
- `[x]` Cart data is stored in the Django session.
- `[x]` Users can add products to the cart.
- `[x]` Users can remove products from the cart.
- `[x]` Users can change product quantities.
- `[x]` Cart totals are calculated correctly.
- `[x]` Cart operations validate product stock.
- `[x]` A user cannot order more products than are available in stock.
- `[x]` Cart actions use helpful messages or inline validation feedback.

## Checkout Acceptance

- `[x]` Checkout page `/checkout/` is available.
- `[x]` Checkout collects contact details and delivery address.
- `[x]` Checkout includes mock payment method selection.
- `[x]` Checkout validates form input.
- `[x]` Checkout creates an order record in the database.
- `[x]` Checkout creates order items with price snapshots.
- `[x]` Checkout handles stock availability inside the order creation flow.
- `[x]` Checkout uses a database transaction for order creation.
- `[x]` Email notification is sent to the user.
- `[x]` Email notification is sent to the administrator.
- `[x]` Checkout errors are handled clearly.

## Account Acceptance

- `[x]` Registration works through the web interface with Django session auth.
- `[x]` Login works through the web interface with Django session auth.
- `[x]` Logout works through the web interface with Django session auth.
- `[x]` Password change works.
- `[x]` Profile editing works.
- `[x]` Delivery address management works.
- `[x]` Order history is available in `/account/`.
- `[x]` Order history supports filtering.
- `[x]` Account pages enforce access control.

## Admin Acceptance

- `[x]` Django admin is wired at `/admin/`.
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

- `[x]` REST API namespace is reserved under `/api/`.
- `[x]` JWT access and refresh token mechanism works.
- `[x]` `POST /api/users/register/` creates an account.
- `[x]` `POST /api/users/login/` returns access and refresh tokens.
- `[x]` `GET /api/products/` lists products with pagination, filtering, and search.
- `[x]` `GET /api/products/<id>/` returns product information.
- `[x]` `GET /api/orders/` returns the current user's orders.
- `[x]` `POST /api/orders/` creates an order based on the cart.
- `[x]` `GET /api/orders/<id>/` returns only the current user's own order detail.
- `[x]` `PATCH/PUT/DELETE /api/orders/<id>/` updates or cancels orders according to permission/status rules.
- `[x]` `GET/POST/PATCH/DELETE /api/cart/` manages cart contents.
- `[x]` `GET/POST /api/products/<id>/reviews/` lists and creates reviews.
- `[x]` Users can view or change only their own API data.
- `[x]` API validation errors are explicit and consistent.

## API Documentation Acceptance

- `[x]` Swagger/OpenAPI documentation is available at `/api/docs/`.
- `[x]` API docs include request examples.
- `[x]` API docs describe JWT authorization.
- `[x]` API docs describe access token, refresh token, and refresh flow.
- `[x]` API docs schemas match implemented serializers.

## GraphQL Acceptance

- `[ ]` GraphQL is available through a single endpoint `/graphql/`.
- `[ ]` GraphQL analytics are protected by appropriate authorization.
- `[ ]` Order analytics include revenue, quantity, average order value, and trends.
- `[ ]` Product analytics include popular products and stock balances.
- `[ ]` User analytics include activity and repeat purchases.
- `[ ]` README or API docs include GraphQL types and example queries.

## Frontend Acceptance

- `[x]` Frontend uses Django Templates as the primary rendering layer.
- `[x]` HTMX is used for server-rendered partial updates where appropriate.
- `[x]` Alpine.js is limited to local UI state.
- `[x]` Tailwind CSS styles the templates.
- `[x]` Visual styling is inspired by Hop & Barley but not copied directly.
- `[ ]` Pages are responsive across mobile and desktop.
- `[x]` Forms show useful validation errors.
- `[x]` Core flows do not rely on localStorage auth simulation.

## Testing Acceptance

- `[x]` pytest-django is configured.
- `[x]` Tests cover catalog, filters, search, sorting, and pagination.
- `[x]` Tests cover product detail and review restrictions.
- `[x]` Tests cover cart behavior and stock validation.
- `[x]` Tests cover checkout, order creation, transactions, and emails.
- `[x]` Tests cover registration, login/logout, account editing, password change, addresses, and order history.
- `[x]` Tests cover REST API JWT auth, permissions, and own-data restrictions.
- `[ ]` Tests cover GraphQL analytics.
- `[x]` Tests cover the restriction that users cannot order more products than are in stock.
- `[x]` Extended test coverage target is at least 80% if time allows.

## Code Quality Acceptance

- `[x]` Important functions and methods include type annotations.
- `[x]` Public APIs and important modules include docstrings.
- `[x]` flake8 or equivalent linter is configured.
- `[x]` mypy is configured.
- `[x]` Linters pass without critical errors.
- `[x]` Tests pass successfully.

## Documentation and Submission Acceptance

- `[x]` README contains project description.
- `[x]` README contains Docker installation and startup instructions.
- `[x]` README contains API usage examples including JWT.
- `[x]` README contains test and lint commands.
- `[x]` README describes project structure.
- `[ ]` README or docs describe GraphQL example queries.
- `[x]` Implementation checklist with completion marks is included.
- `[ ]` Repository has meaningful commits and branch usage.
- `[x]` Deployment link or video demonstration is prepared for submission.
