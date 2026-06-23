# myshop

## Project

Online store built with Django templates for the browser UI, Django REST Framework for `/api/`, PostgreSQL for persistence, and Docker Compose for local infrastructure.

## Run

### Local Python

1. Create and activate a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Create `.env` from `.env.example` and keep `POSTGRES_HOST=localhost` for local venv usage.
4. Run `python manage.py migrate`.
5. Run `python manage.py runserver`.

### Docker

1. Create `.env` from `.env.example`.
2. Keep the database credentials in `.env` and leave `POSTGRES_HOST=localhost` there for local use.
3. Run `docker compose up --build`.
4. Docker Compose overrides `POSTGRES_HOST` to `db` inside the `web` container automatically.

## Test

- `pytest`
- `python manage.py check`
- `python manage.py migrate --check`

## Lint

- `flake8 .`
- `mypy .`

## API

OpenAPI docs are available at `/api/docs/` and the raw schema is available at `/api/schema/`.

JWT flow:

1. `POST /api/users/login/` with username and password.
2. Send `Authorization: Bearer <access_token>` on protected endpoints.
3. Refresh expired access tokens with `POST /api/users/token/refresh/`.

Example requests:

```bash
curl -X POST http://127.0.0.1:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"api-user\",\"password\":\"VeryStrongPass123\",\"email\":\"api-user@example.com\"}"
```

```bash
curl -X POST http://127.0.0.1:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"api-user\",\"password\":\"VeryStrongPass123\"}"
```

```bash
curl -X POST http://127.0.0.1:8000/api/users/token/refresh/ \
  -H "Content-Type: application/json" \
  -d "{\"refresh\":\"<refresh_token>\"}"
```

```bash
curl "http://127.0.0.1:8000/api/products/?q=amber&category=extracts&min_price=10.00"
```

```bash
curl -c cookies.txt -b cookies.txt -X POST http://127.0.0.1:8000/api/cart/ \
  -H "Content-Type: application/json" \
  -d "{\"product_id\":1,\"quantity\":2}"
```

```bash
curl -c cookies.txt -b cookies.txt -X POST http://127.0.0.1:8000/api/orders/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d "{\"shipping_address\":\"42 Brewery Lane, Kyiv, 02000, Ukraine\"}"
```

```bash
curl -X POST http://127.0.0.1:8000/api/products/1/reviews/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d "{\"rating\":5,\"comment\":\"Excellent ingredients and fast delivery.\"}"
```

Note: the cart and order-create endpoints use the current Django session cart, so API clients must preserve cookies between cart updates and order creation.

## Structure

- `config/` Django project settings and URL configuration
- `products/` product-domain app shell
- `orders/` order-domain app shell
- `users/` user-domain app shell
- `api/` API app shell
- `templates/` shared Django templates
- `static/` shared static assets
- `media/` uploaded media during development
- `tests/` project-wide tests
- `scripts/` helper scripts including validation
