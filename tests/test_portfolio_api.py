import os

import pytest
import requests


BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
TIMEOUT = 5


def url(path: str) -> str:
    return f"{BASE_URL.rstrip('/')}/{path.lstrip('/')}"


@pytest.mark.api
def test_health_endpoint_returns_ok_status():
    response = requests.get(url("/health"), timeout=TIMEOUT)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert response.json() == {"status": "OK"}


@pytest.mark.api
def test_about_endpoint_returns_profile_text():
    response = requests.get(url("/about"), timeout=TIMEOUT)

    assert response.status_code == 200
    assert response.text == "ВСЕ работет"


@pytest.mark.api
def test_home_page_returns_portfolio_html():
    response = requests.get(url("/"), timeout=TIMEOUT)

    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]
    assert "<title>QA Portfolio</title>" in response.text
    assert "QA ENGINEER" in response.text


@pytest.mark.api
def test_stylesheet_is_available():
    response = requests.get(url("/css/style.css"), timeout=TIMEOUT)

    assert response.status_code == 200
    assert "text/css" in response.headers["Content-Type"]
    assert ".site-header" in response.text


@pytest.mark.api
def test_unknown_route_returns_404():
    response = requests.get(url("/unknown-route"), timeout=TIMEOUT)

    assert response.status_code == 404
