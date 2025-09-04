from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_invalid_file_upload():
    response = client.post("/analyze", files={"image": ("test.txt", b"not an image", "text/plain")})
    assert response.status_code == 422 or response.status_code == 400
