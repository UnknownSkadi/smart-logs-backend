from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Smart Logs Backend đang hoạt động bình thường"}

def test_predict_route_endpoint():
    payload = {
        "origin": {"lat": 10.7769, "lng": 106.7009},
        "destination": {"lat": 10.8021, "lng": 106.6438},
        "departure_time": "2026-10-20T08:30:00Z"
    }
    response = client.post("/api/v1/routes/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "recommended_route_id" in data
    assert len(data["candidate_routes"]) > 0

def test_update_eta_endpoint():
    payload = {
        "trip_id": "TRIP_101",
        "current_location": {"lat": 10.7850, "lng": 106.6910},
        "timestamp": "2026-10-20T08:42:00Z"
    }
    response = client.post("/api/v1/routes/update-eta", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["trip_id"] == "TRIP_101"