"""Smoke tests for the product catalog entry stage."""

import pytest
from django.urls import reverse


pytestmark = pytest.mark.django_db


def test_homepage_renders_catalog_entry_experience(client) -> None:
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert b"Browse catalog" in response.content
    assert b"Fresh additions to the catalog" in response.content
