# myshop

## Project

Online store foundation built with Django for the web interface, PostgreSQL for persistence, and Docker Compose for local infrastructure.

Phase 1 includes only the project foundation. Domain models, business logic, catalog flows, cart flows, checkout flows, REST API endpoints, JWT auth, Swagger, and GraphQL are intentionally deferred to later phases.

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

REST API, JWT, Swagger/OpenAPI, and GraphQL are planned but not implemented in Phase 1.

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
