from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Location(BaseModel):
    lat: float = Field(..., example=10.7769, description="Vĩ độ")
    lng: float = Field(..., example=106.7009, description="Kinh độ")

class RoutePredictionRequest(BaseModel):
    origin: Location
    destination: Location
    departure_time: Optional[datetime] = Field(default_factory=datetime.utcnow, example="2026-10-20T08:30:00Z")

class CandidateRoute(BaseModel):
    route_id: str = Field(..., example="ROUTE_A")
    distance_km: float = Field(..., example=7.5)
    predicted_duration_min: float = Field(..., example=22.3)
    baseline_duration_min: float = Field(..., example=25.0)
    geometry: str = Field(..., example="sample_polyline_a")

class RoutePredictionResponse(BaseModel):
    recommended_route_id: str = Field(..., example="ROUTE_A")
    candidate_routes: List[CandidateRoute]
    selection_reason: str = Field(..., example="Tuyến có ETA ngắn nhất (22.3 phút)")

class RealtimeETAUpdateRequest(BaseModel):
    trip_id: str = Field(..., example="TRIP_101")
    current_location: Location
    timestamp: datetime = Field(default_factory=datetime.utcnow, example="2026-10-20T08:42:00Z")

class RealtimeETAUpdateResponse(BaseModel):
    trip_id: str = Field(..., example="TRIP_101")
    updated_eta_min: float = Field(..., example=11.2)
    estimated_arrival_time: datetime = Field(..., example="2026-10-20T08:53:12Z")