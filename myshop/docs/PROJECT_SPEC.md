# Technical Assignment: Online Store on Django/DRF

## 1. Introduction and Goal

You are a beginner developer at your first job. Your task is to transform a ready-made static HTML/CSS design into a full-fledged online store application using Django.

**The project must include:**

* **Web interface:** Django, templates, sessions.
* **REST API** for external clients: DRF, JWT.
* **GraphQL** for analytics as an additional improvement.
* **Infrastructure:** PostgreSQL, Docker.
* **Code quality:** typing, linters, tests, documentation.

**Goal:** to demonstrate understanding of Django, DRF, working with databases, architectural practices, code quality standards, and deployment skills.

**HTML Template:** https://github.com/MagicCodeGit/Hop-and-Barley.git

---

## 2. General Principles

* The **web interface** for users in the browser uses **session-based authentication**, which is the standard for Django.
* **External APIs** use **JWT** for authorization.
* **GraphQL** is available through a single endpoint `/graphql/`.
* The project structure is approximate — variations are allowed, but it must be logical and modular.
* **Infrastructure:** the use of **PostgreSQL** is mandatory. All services, the application and the database, must be deployed through **Docker Compose**.
* The use of alternative dependency managers (`poetry`, `pip-tools/uv`).

---

## 3. Functional Blocks

### 3.1. Product Catalog and Search (`/` and `/products/`)

**Functionality:**

* Product list with pagination.
* Filtering by category and price range.
* Search by name and description.
* Sorting by price, popularity, and novelty.

**Key topics:** CBV, templates, ORM, optimization of database queries.

### 3.2. Product Page (`/product/<slug>/`)

* Detailed information: name, description, price, image, rating.
* Reviews with ratings from 1 to 5. Ability to leave a review only after purchasing the product — verification is required.
* "Add to Cart" button and quantity selection.

**Key topics:** CBV, forms, ORM, validation.

### 3.3. Cart (`/cart/`)

* Viewing cart contents.
* Adding, removing, and changing product quantities.
* Calculating the final price, taking stock balances into account.
* Storing cart data in the session.
* Checking product availability in stock.

**Key topics:** Django Sessions, Message Framework, business logic.

### 3.4. Checkout (`/checkout/`)

* Form for contact details and delivery address.
* Payment method selection: imitation/mock.
* Creating an order record in the database.
* Email notification for the user and the administrator.
* Error handling and form validation.

**Key topics:** Forms, sending email, database transactions.

### 3.5. Personal Account (`/account/`)

* Registration, login/logout with session auth.
* Order history with filtering.
* Profile editing.
* Password change.
* Management of delivery addresses.

**Key topics:** Authentication, ORM, forms, access control.

### 3.6. Admin Panel (`/admin/`)

* Managing products, categories, orders, reviews, and users.
* Analytics: aggregations and annotations — revenue, top products, number of orders.
* Search, filters, custom actions.
* Configuring access rights for different roles.

**Key topics:** Django Admin, aggregations, customization.

### 3.7. REST API (`/api/`)

Examples of resources and actions:

| Resource     | Action | URL Pattern | HTTP Method(s) | Description |
| ------------ | ------ | ----------- | -------------- | ----------- |
| **Products** |        |             |                |             |

```
            | List                   | /api/products/                 | GET                      | Pagination, filtering, search
            | Details                | /api/products/<id>/            | GET                      | Product information
```

**Orders**
| Create                 | /api/orders/                   | POST                     | Create an order based on the cart
| Own list               | /api/orders/                   | GET                      | List of current user's orders
| Details                | /api/orders/<id>/              | GET                      | Detailed information, only about own order
| Update/cancel          | /api/orders/<id>/              | PATCH/PUT/DELETE         | Change status/cancel
**Users**
| Registration           | /api/users/register/           | POST                     | Create an account
| Login (JWT)            | /api/users/login/              | POST                     | Get access/refresh tokens
**Cart**
| Management             | /api/cart/                     | GET, POST, PATCH, DELETE | Manage cart contents
**Reviews**
| Add/view               | /api/products/<id>/reviews/    | GET, POST                | List and submit a review

* **JWT:** implement an access + refresh token mechanism.
* **Access rights:** a user can view/change only their own data.

**Key topics:** DRF, serialization, ViewSets/routers, pagination, permissions.

### 3.8. API Documentation

* Swagger/OpenAPI for the REST API, for example at `/api/docs/`.
* Request examples, data schemas, description of the authorization process.

**Key topics:** Automatic documentation generation: drf-spectacular, drf-yasg.

### 3.9. GraphQL

* Single endpoint `/graphql/`.
* Analytical queries:

  * **Orders:** revenue, quantity, average order value, trends.
  * **Products:** popular products, stock balances.
  * **Users:** activity, number of repeat purchases.

**Key topics:** Graphene-Django, resolvers, authorization in GraphQL.

> **Note:** extended test coverage, CI/CD setup, and so on.

---

## 4. Data Structure: Database

### Category

* `id` (PK)
* `name` (CharField)
* `slug` (SlugField, unique)
* `parent` (ForeignKey to self, nullable) — for implementing nested categories
* `created_at`, `updated_at`

### Product

* `id` (PK)
* `name` (CharField)
* `slug` (SlugField, unique)
* `description` (TextField)
* `price` (DecimalField)
* `category` (ForeignKey to Category)
* `image` (ImageField)
* `is_active` (BooleanField)
* `stock` (IntegerField) — quantity in stock
* `created_at`, `updated_at`

### Order

* `id` (PK)
* `user` (ForeignKey to User)
* `status` (CharField: `pending`, `paid`, `shipped`, `delivered`, `cancelled`)
* `total_price` (DecimalField)
* `shipping_address` (TextField or a separate Address model)
* `created_at`, `updated_at`

### OrderItem

* `id` (PK)
* `order` (ForeignKey to Order)
* `product` (ForeignKey to Product)
* `quantity` (IntegerField)
* `price` (DecimalField) — price snapshot at the time of purchase

### Review

* `id` (PK)
* `product` (ForeignKey to Product)
* `user` (ForeignKey to User)
* `rating` (IntegerField, 1–5)
* `comment` (TextField)
* `created_at`

*Additional models can be implemented:* Address, Payment, and so on.

---

## 5. Approximate Project Architecture

```text
/myshop/
├── config/         # Settings, urls, asgi/wsgi
├── products/       # Models, views, serializers, forms, admin for products
├── orders/         # Order and cart logic
├── users/          # Registration, profiles, authentication
├── reviews/        # Reviews, or as part of `products`
├── payments/       # Payment methods, webhooks
├── graphql/        # Schema and resolvers, if used
├── templates/      # Django templates
├── static/         # Static files: CSS, JS, images
├── tests/          # Tests
├── docker-compose.yml # File for infrastructure startup
├── Dockerfile      # Application Docker image
├── manage.py
└── README.md
```

> **Note:** The structure is approximate. The priority is separation of concerns, readability, and code extensibility.

---

## 6. Code Quality and Infrastructure

1. **Typing and Docstrings**

   * Use type annotations in functions/methods.
   * Write docstrings for public APIs and important modules.

2. **Linters and Static Checking**

   * Configure `flake8` or an equivalent tool.
   * Use `mypy` for type checking.

3. **Testing**

   * Use `pytest-django`.
   * Cover the main scenarios with tests: catalog, cart, orders, registration/login, REST API, business logic.
   * Check restrictions, for example, a user cannot order more products than are available in stock.

4. **Infrastructure**

   * Database — **PostgreSQL**.
   * **Docker Compose** for local startup: application + database.
   * All dependencies must be documented in `requirements.txt` or `pyproject.toml`.
   * Bonus: use of `poetry` or `uv`.

5. **Git Workflow**

   * Make meaningful, small commits.
   * Use branches for development: `feature/...`, `develop/...`, stable branch `main`.

6. **Documentation**

   * **README.md** must contain: project description, installation and startup instructions, API usage examples including JWT, how to run tests and linters, and a description of the project structure.

---

## 7. API Documentation and Interaction

* Configure Swagger/OpenAPI for the REST API.
* Add request examples with JWT, and explain the authorization scheme.
* Describe the format of access/refresh tokens and the process of refreshing them.
* Describe types and example queries in GraphQL.

---

## Recommended Improvements

* GraphQL analytics.
* Extended test coverage: >=80%.
* CI/CD setup: automatic running of tests, linters, image build.
* Use of `poetry` or another modern dependency manager.

---

## 9. Project Submission Requirements

1. GitHub repository with all code.
2. Detailed **README.md** containing:

   * Project description.
   * Installation and startup instructions through Docker.
   * API usage examples including JWT.
   * Commands for running tests and linters.
   * Description of the project structure.
3. Link to the deployed project or a video demonstration.
4. Your full name and group, as well as a link to the repository, sent to the teacher.
5. Implementation checklist with marks showing what has been completed.
6. Meaningful commit history and use of branches.

---

## 10. Pre-submission Checklist

* [ ] The project starts with the `docker-compose up` command on a clean system.
* [ ] PostgreSQL is used.
* [ ] Catalog: filters, search, and pagination are implemented.
* [ ] Product page: details, reviews, and an add-to-cart button are present.
* [ ] Cart: contents can be managed, the total is calculated, and stock validation exists.
* [ ] Checkout: an order is created, email is sent, and validation exists.
* [ ] Personal account: registration, login, order history, and profile editing work.
* [ ] REST API: authorization through JWT works, documentation exists, and access rights are configured.
* [ ] Admin panel: analytics, filters, and convenient data management exist.
* [ ] Swagger/OpenAPI documentation is available and works correctly.
* [ ] Code contains typing and docstrings.
* [ ] Linters: flake8/mypy pass without critical errors.
* [ ] Basic tests are implemented and pass successfully.
* [ ] README is complete and understandable.
* [ ] Commits are meaningful, and branches are used correctly.
* [ ] This checklist is added to the project.
