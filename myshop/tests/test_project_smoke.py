"""Smoke tests for the project foundation stage."""

from django.urls import reverse


def test_homepage_placeholder(client) -> None:
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert response.content == b"myshop foundation is up"
