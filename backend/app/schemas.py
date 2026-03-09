from typing import Literal

from pydantic import BaseModel, Field


class RiskAssessmentRequest(BaseModel):
    age: int = Field(..., ge=18, le=100, description="Возраст пользователя")
    height_cm: float = Field(..., gt=100, le=230, description="Рост в сантиметрах")
    weight_kg: float = Field(..., gt=30, le=250, description="Вес в килограммах")
    physical_activity: Literal["low", "medium", "high"]
    family_history_diabetes: bool
    high_sugar_intake: bool
    high_blood_pressure_history: bool


class RiskAssessmentResponse(BaseModel):
    score: int
    risk_level: Literal["низкий риск", "средний риск", "высокий риск"]
    recommendation: str
    explanation: str
