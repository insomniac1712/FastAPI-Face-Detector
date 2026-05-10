from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200


def test_roi_endpoint():
    response = client.get("/api/roi")
    assert response.status_code == 200