from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import RiskAssessmentRequest, RiskAssessmentResponse
from app.services.risk_logic import calculate_risk

app = FastAPI(
    title="Diabetes Risk Assessment API",
    description="Учебный API для предварительной оценки риска диабета 2 типа",
    version="0.2.0",
)

# Для локальной интеграции frontend и backend в рамках лабораторной.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/risk-assessment", response_model=RiskAssessmentResponse)
def risk_assessment(payload: RiskAssessmentRequest) -> RiskAssessmentResponse:
    return calculate_risk(payload)
