![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Django 5.1](https://img.shields.io/badge/Django-5.1-092E20?logo=django&logoColor=white)
![DRF API](https://img.shields.io/badge/DRF-API-A30000)
![PostgreSQL 16](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-tested-0A9EDC?logo=pytest&logoColor=white)

# myshop

## Project Description

`myshop` is a Django online store built from the assignment requirements in [docs/PROJECT_SPEC.md](D:/VSCode_Python_Projects_26/DjangoDRFOnlineStore_final_proj_JavaRush/myshop/docs/PROJECT_SPEC.md). It includes:

- a browser storefront built with Django templates, HTMX, Alpine.js, and Tailwind CSS
- session-based cart, checkout, and account flows
- a DRF-based REST API under `/api/`
- JWT authentication for external API clients
- Swagger/OpenAPI documentation at `/api/docs/`
- PostgreSQL and Docker Compose support for local infrastructure

The GraphQL analytics bonus is intentionally not implemented yet.

## Features

- Catalog pages with search, sorting, pagination, category filters, and price filters
- Product detail pages with review display and add-to-cart controls
- Session-backed cart management with stock validation
- Transactional checkout with order item price snapshots and email notifications
- Browser registration, login/logout, password change, profile editing, and address management
- Account order history filtered to the authenticated user
- JWT-protected REST API for products, cart, orders, users, and reviews
- Swagger/OpenAPI docs with request examples and JWT guidance

## Local Development

### Prerequisites

- Python 3.12+ or a compatible local interpreter
- PostgreSQL running locally
- A virtual environment

### Setup

```powershell
cd D:\VSCode_Python_Projects_26\DjangoDRFOnlineStore_final_proj_JavaRush\myshop
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Keep `POSTGRES_HOST=localhost` in `.env` for local non-Docker development.

### Run

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Optional admin user:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

## Docker Compose

The Docker workflow was verified against the checked-in [docker-compose.yml](D:/VSCode_Python_Projects_26/DjangoDRFOnlineStore_final_proj_JavaRush/myshop/docker-compose.yml) and [Dockerfile](D:/VSCode_Python_Projects_26/DjangoDRFOnlineStore_final_proj_JavaRush/myshop/Dockerfile).

### Setup and Run

```powershell
cd D:\VSCode_Python_Projects_26\DjangoDRFOnlineStore_final_proj_JavaRush\myshop
Copy-Item .env.example .env
docker compose up -d --build
docker compose run --rm web python manage.py migrate --noinput
docker compose run --rm web python manage.py createsuperuser
```

Notes:

- `docker compose` overrides `POSTGRES_HOST` to `db` for the `web` container automatically.
- The checked-in container command starts the Django development server on `0.0.0.0:8000`.
- Migrations are not run automatically during container startup, so `docker compose run --rm web python manage.py migrate --noinput` is required after the first boot.

Useful follow-up commands:

```powershell
docker compose logs -f web
docker compose down
```

## URLs

- Home: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Catalog: [http://127.0.0.1:8000/products/](http://127.0.0.1:8000/products/)
- Product detail example pattern: [http://127.0.0.1:8000/product/<slug>/](http://127.0.0.1:8000/product/<slug>/)
- Cart: [http://127.0.0.1:8000/cart/](http://127.0.0.1:8000/cart/)
- Checkout: [http://127.0.0.1:8000/checkout/](http://127.0.0.1:8000/checkout/)
- Account: [http://127.0.0.1:8000/account/](http://127.0.0.1:8000/account/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- API docs: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- API schema: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

## Tests and Quality Checks

```powershell
.\.venv\Scripts\python.exe -m pytest --cov=. --cov-report=term
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py migrate --check
.\.venv\Scripts\python.exe -m flake8 .
.\.venv\Scripts\python.exe -m mypy .
```

Current automated coverage from the last Phase 10 validation run: `97%`.

## API and JWT Examples

OpenAPI docs are available at `/api/docs/` and the raw schema is available at `/api/schema/`.

JWT flow:

1. `POST /api/users/login/` with username and password.
2. Send `Authorization: Bearer <access_token>` on protected endpoints.
3. Refresh expired access tokens with `POST /api/users/token/refresh/`.

Registration:

```bash
curl -X POST http://127.0.0.1:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"api-user\",\"password\":\"VeryStrongPass123\",\"email\":\"api-user@example.com\"}"
```

JWT login:

```bash
curl -X POST http://127.0.0.1:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"api-user\",\"password\":\"VeryStrongPass123\"}"
```

JWT refresh:

```bash
curl -X POST http://127.0.0.1:8000/api/users/token/refresh/ \
  -H "Content-Type: application/json" \
  -d "{\"refresh\":\"<refresh_token>\"}"
```

Product list:

```bash
curl "http://127.0.0.1:8000/api/products/?q=amber&category=extracts&min_price=10.00"
```

Add to cart:

```bash
curl -c cookies.txt -b cookies.txt -X POST http://127.0.0.1:8000/api/cart/ \
  -H "Content-Type: application/json" \
  -d "{\"product_id\":1,\"quantity\":2}"
```

Create order from the current session cart:

```bash
curl -c cookies.txt -b cookies.txt -X POST http://127.0.0.1:8000/api/orders/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d "{\"shipping_address\":\"42 Brewery Lane, Kyiv, 02000, Ukraine\"}"
```

Create review:

```bash
curl -X POST http://127.0.0.1:8000/api/products/1/reviews/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d "{\"rating\":5,\"comment\":\"Excellent ingredients and fast delivery.\"}"
```

Note: `/api/cart/` and `POST /api/orders/` use the current Django session cart, so API clients must preserve cookies between cart updates and order creation.

## Project Structure

- `config/` Django settings, root URLs, ASGI, and WSGI
- `products/` catalog models, admin, and storefront product views
- `orders/` cart helpers, checkout forms, order services, and cart/checkout views
- `users/` browser auth, profile, address models/forms/views
- `api/` DRF serializers, API views, and API routes
- `templates/` shared Django templates and HTMX partials
- `static/` shared static assets
- `media/` uploaded media for development
- `tests/` pytest-django test suite
- `scripts/` helper scripts including validation
- `docs/` planning, specification, and acceptance-tracking documents

## Implementation Checklist

- `[x]` PostgreSQL configuration exists
- `[x]` Docker Compose configuration exists
- `[x]` Catalog, search, sorting, filters, and pagination are implemented
- `[x]` Product detail and review display are implemented
- `[x]` Cart management and stock validation are implemented
- `[x]` Checkout, order creation, transaction handling, and emails are implemented
- `[x]` Browser registration, login, account pages, and address management are implemented
- `[x]` REST API with JWT authentication is implemented
- `[x]` Swagger/OpenAPI documentation is implemented
- `[x]` Tests, flake8, and mypy pass
- `[x]` README contains run, Docker, API/JWT, test, lint, and structure documentation
- `[ ]` Admin analytics and role-based admin hardening are still pending
- `[ ]` GraphQL bonus analytics are still pending
- `[ ]` Final deployment link is not assigned yet

## Deployment or Video Placeholder

If a live deployment is not prepared yet, use this section as the submission placeholder:

- Deployment URL: `TBD`
- Demo video URL: `TBD`
- Suggested demo recording flow:
  1. Show `docker compose up -d --build`
  2. Show `python manage.py migrate` or `docker compose exec web python manage.py migrate`
  3. Walk through catalog, product, cart, checkout, account, and admin
  4. Show `/api/docs/` and one JWT-protected API call
  5. Show `pytest`, `flake8`, and `mypy` passing

## Known Remaining Scope

- GraphQL analytics are intentionally deferred to the bonus phase.
- README does not include GraphQL example queries yet because GraphQL is not implemented.
- Admin analytics and role-aware admin permissions remain future work outside the completed core path.
