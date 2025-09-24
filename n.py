from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_navigation_item():
    response = client.post("/api/v1/navigation/", json={"name": "Home", "link": "/home", "icon": "home-icon"})
    assert response.status_code == 200
    assert response.json()["name"] == "Home"

def test_read_navigation_item():
    response = client.get("/api/v1/navigation/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Home"