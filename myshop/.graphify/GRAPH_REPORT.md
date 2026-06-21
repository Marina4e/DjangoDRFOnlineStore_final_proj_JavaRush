# Graph Report - .  (2026-06-21)

## Corpus Check
- Corpus is ~1 722 words - fits in a single context window. You may not need a graph.

## Summary
- 89 nodes · 81 edges · 13 communities detected
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output
- Edge kinds: contains: 42 · rationale_for: 13 · uses: 13 · method: 5 · imports_from: 4 · inherits: 4


## Input Scope
- Requested: all
- Resolved: all (source: configured-default)
- Included files: 30 · Candidates: recursive
- Excluded: 0 untracked · 0 ignored · 0 sensitive · 0 missing committed

## Graph Freshness
- Built from Git commit: `f9e15e9`
- Compare this hash to `git rev-parse HEAD` before trusting freshness-sensitive graph output.
## God Nodes (most connected - your core abstractions)
1. `Category` - 5 edges
2. `Product` - 5 edges
3. `Review` - 5 edges
4. `Order` - 4 edges
5. `OrderItem` - 4 edges
6. `CategoryAdmin` - 4 edges
7. `ProductAdmin` - 4 edges
8. `ReviewAdmin` - 4 edges
9. `OrderItemInline` - 3 edges
10. `OrderAdmin` - 3 edges

## Surprising Connections (you probably didn't know these)
- `OrderAdmin` --uses--> `Order`  [INFERRED]
  orders/admin.py → orders/models.py
- `OrderAdmin` --uses--> `OrderItem`  [INFERRED]
  orders/admin.py → orders/models.py
- `OrderItemInline` --uses--> `Order`  [INFERRED]
  orders/admin.py → orders/models.py
- `OrderItemInline` --uses--> `OrderItem`  [INFERRED]
  orders/admin.py → orders/models.py
- `CategoryAdmin` --uses--> `Category`  [INFERRED]
  products/admin.py → products/models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.29
Nodes (7): CategoryAdmin, ProductAdmin, ReviewAdmin, Category, Meta, Product, Review

### Community 1 - "Community 1"
Cohesion: 0.27
Nodes (6): OrderAdmin, OrderItemInline, Meta, Order, OrderItem, OrderStatus

### Community 4 - "Community 4"
Cohesion: 0.22
Nodes (5): ApiConfig, AppConfig, OrdersConfig, ProductsConfig, UsersConfig

### Community 5 - "Community 5"
Cohesion: 0.25
Nodes (7): env(), env_bool(), load_env_file(), Django settings for the online store project., Load simple KEY=VALUE pairs from a local .env file if it exists., Return an environment variable value or the provided default., Parse a boolean environment variable.

### Community 6 - "Community 6"
Cohesion: 0.50
Nodes (3): home(), Root URL configuration for the online store project., Return a small placeholder response for the project foundation stage.

### Community 7 - "Community 7"
Cohesion: 0.67
Nodes (2): main(), Run administrative tasks.

### Community 8 - "Community 8"
Cohesion: 0.67
Nodes (1): Smoke tests for the project foundation stage.

### Community 9 - "Community 9"
Cohesion: 1.00
Nodes (1): ASGI config for the online store project.

### Community 10 - "Community 10"
Cohesion: 1.00
Nodes (1): Django project package.

### Community 11 - "Community 11"
Cohesion: 1.00
Nodes (1): WSGI config for the online store project.

### Community 12 - "Community 12"
Cohesion: 1.00
Nodes (1): Migration

### Community 13 - "Community 13"
Cohesion: 1.00
Nodes (1): Products app package.

### Community 14 - "Community 14"
Cohesion: 1.00
Nodes (1): Test package for project-wide tests.

## Knowledge Gaps
- **17 isolated node(s):** `Django project package.`, `ASGI config for the online store project.`, `Django settings for the online store project.`, `Load simple KEY=VALUE pairs from a local .env file if it exists.`, `Return an environment variable value or the provided default.` (+12 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 7`** (2 nodes): `main()`, `Run administrative tasks.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (1 nodes): `Smoke tests for the project foundation stage.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 9`** (1 nodes): `ASGI config for the online store project.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 10`** (1 nodes): `Django project package.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (1 nodes): `WSGI config for the online store project.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `Migration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `Products app package.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (1 nodes): `Test package for project-wide tests.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Are the 3 inferred relationships involving `Category` (e.g. with `CategoryAdmin` and `ProductAdmin`) actually correct?**
  _`Category` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Product` (e.g. with `CategoryAdmin` and `ProductAdmin`) actually correct?**
  _`Product` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Review` (e.g. with `CategoryAdmin` and `ProductAdmin`) actually correct?**
  _`Review` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Order` (e.g. with `OrderAdmin` and `OrderItemInline`) actually correct?**
  _`Order` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Django project package.`, `ASGI config for the online store project.`, `Django settings for the online store project.` to the rest of the system?**
  _17 weakly-connected nodes found - possible documentation gaps or missing edges._