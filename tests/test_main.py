import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders/", json={
        "customer_name": "Test User",
        "item_name": "Pen",
        "quantity": 5,
        "status": "pending"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Test User"
    assert data["quantity"] == 5

def test_get_order_by_id():
    # Create a sample order
    create_resp = client.post("/orders/", json={
        "customer_name": "Tester",
        "item_name": "Notebook",
        "quantity": 2,
        "status": "shipped"
    })
    order_id = create_resp.json()["id"]

    # Fetch it
    get_resp = client.get(f"/orders/{order_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["item_name"] == "Notebook"

def test_update_order_status():
    # Create order
    create_resp = client.post("/orders/", json={
        "customer_name": "Updater",
        "item_name": "Charger",
        "quantity": 1,
        "status": "pending"
    })
    order_id = create_resp.json()["id"]

    # Update status
    update_resp = client.put(f"/orders/{order_id}", json={"status": "delivered"})
    assert update_resp.status_code == 200
    assert update_resp.json()["status"] == "delivered"

def test_filter_orders_by_status():
    # Add at least one shipped order
    client.post("/orders/", json={
        "customer_name": "FilterUser",
        "item_name": "Router",
        "quantity": 1,
        "status": "shipped"
    })

    response = client.get("/orders/?status=shipped")
    assert response.status_code == 200
    data = response.json()
    assert all(order["status"].lower() == "shipped" for order in data)
