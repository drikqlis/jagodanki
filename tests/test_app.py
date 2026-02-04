import pytest

from app import app, BIO, PROJECTS


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_returns_200(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_index_contains_bio_name(client):
    resp = client.get("/")
    html = resp.data.decode()
    assert BIO["name"] in html


def test_index_contains_all_projects(client):
    resp = client.get("/")
    html = resp.data.decode()
    for project in PROJECTS:
        assert project["title"] in html


def test_index_contains_navigation(client):
    resp = client.get("/")
    html = resp.data.decode()
    assert "Projekty" in html
    assert "Kontakt" in html


def test_index_contains_current_year(client):
    from datetime import datetime

    resp = client.get("/")
    html = resp.data.decode()
    assert str(datetime.now().year) in html


def test_index_html_lang_pl(client):
    resp = client.get("/")
    html = resp.data.decode()
    assert 'lang="pl"' in html


def test_static_css_exists(client):
    resp = client.get("/static/css/style.css")
    assert resp.status_code == 200


def test_static_favicons_exist(client):
    paths = [
        "/static/favicon/apple-touch-icon.png",
        "/static/favicon/favicon-32x32.png",
        "/static/favicon/favicon-16x16.png",
        "/static/favicon/site.webmanifest",
    ]
    for path in paths:
        resp = client.get(path)
        assert resp.status_code == 200, f"{path} missing"


def test_static_placeholder_images_exist(client):
    for i in range(1, 5):
        resp = client.get(f"/static/images/placeholder-{i}.svg")
        assert resp.status_code == 200, f"placeholder-{i}.svg missing"
