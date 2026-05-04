from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_and_login_user():
    reg_payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "secret",
    }
    r = client.post("/auth/register", json=reg_payload)
    assert r.status_code in (200, 201)

    login_payload = {
        "username": "testuser",
        "password": "secret",
    }
    r2 = client.post("/auth/login", json=login_payload)
    assert r2.status_code == 200
    data = r2.json()
    assert "access_token" in data