from __future__ import annotations

import pytest
from django.urls import reverse


pytestmark = pytest.mark.django_db


def test_api_schema_endpoint_exposes_openapi_document(client) -> None:
    response = client.get(reverse("api-schema"))

    assert response.status_code == 200
    payload = response.content.decode("utf-8")
    assert "openapi: 3.0.3" in payload
    assert "title: MyShop REST API" in payload
    assert "/api/products/:" in payload
    assert "/api/orders/:" in payload
    assert "/api/users/login/:" in payload
    assert "jwtAuth:" in payload


def test_api_docs_swagger_ui_is_reachable(client) -> None:
    response = client.get(reverse("api-docs"))

    assert response.status_code == 200
    assert b"swagger-ui" in response.content.lower()
    assert b"/api/schema/" in response.content
