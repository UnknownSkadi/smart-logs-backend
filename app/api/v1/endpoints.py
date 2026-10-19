from fastapi import APIRouter, status
from app.schemas.route import (
    RoutePredictionRequest,
    RoutePredictionResponse,
    CandidateRoute,
    RealtimeETAUpdateRequest,
    RealtimeETAUpdateResponse
)
from datetime import timedelta

router = APIRouter()

@router.post(
    "/routes/predict",
    response_model=RoutePredictionResponse,
    status_code=status.HTTP_200_OK,
    summary="Dự báo thời gian di chuyển và đề xuất tuyến đường"
)
def predict_route(payload: RoutePredictionRequest):
    route_a = CandidateRoute(
        route_id="ROUTE_A",
        distance_km=7.5,
        predicted_duration_min=22.3,
        baseline_duration_min=25.0,
        geometry="sample_polyline_a"
    )
    route_b = CandidateRoute(
        route_id="ROUTE_B",
        distance_km=8.2,
        predicted_duration_min=28.1,
        baseline_duration_min=30.0,
        geometry="sample_polyline_b"
    )
    
    return RoutePredictionResponse(
        recommended_route_id="ROUTE_A",
        candidate_routes=[route_a, route_b],
        selection_reason="Tuyến có ETA ngắn nhất (22.3 phút)"
    )

@router.post(
    "/routes/update-eta",
    response_model=RealtimeETAUpdateResponse,
    status_code=status.HTTP_200_OK,
    summary="Cập nhật ETA Realtime theo GPS"
)
def update_realtime_eta(payload: RealtimeETAUpdateRequest):
    updated_eta = 11.2
    arrival_time = payload.timestamp + timedelta(minutes=updated_eta)
    
    return RealtimeETAUpdateResponse(
        trip_id=payload.trip_id,
        updated_eta_min=updated_eta,
        estimated_arrival_time=arrival_time
    )