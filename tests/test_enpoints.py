from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_home():
    response = client.get("/") # requests.get("") # python requests
    assert response.status_code == 200
    assert "application/json" in response.headers['content-type']
    assert response.json() == {"message": "Hello World"}