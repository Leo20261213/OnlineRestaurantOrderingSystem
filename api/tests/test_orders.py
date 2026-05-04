from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order():
    payload = {
        "customer_id": 1,
        "total_amount": 25.50,
        "status": "pending"
    }
    r = client.post("/orders/", json=payload)
    assert r.status_code in (200, 201)
    data = r.json()
    assert data["total_amount"] == 25.50