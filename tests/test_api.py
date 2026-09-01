from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_extract():
    response = client.post("/extract", json={"text": "45-year-old male"})
    assert response.status_code == 200
    assert response.json()["age"] == 45


def test_extract_bad_input():
    response = client.post("/extract", json={"wrong": "field"})
    assert response.status_code == 422