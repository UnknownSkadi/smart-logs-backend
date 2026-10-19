from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import router as api_v1_router

app = FastAPI(
    title="Smart Logs ETA API Service",
    description="Hệ thống Backend hỗ trợ dự báo thời gian di chuyển và chọn tuyến giao hàng",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "Smart Logs Backend đang hoạt động bình thường"}

app.include_router(api_v1_router, prefix="/api/v1", tags=["Routes & ETA"])