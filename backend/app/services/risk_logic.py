from app.schemas import RiskAssessmentRequest, RiskAssessmentResponse


def _calculate_bmi(height_cm: float, weight_kg: float) -> float:
    height_m = height_cm / 100
    return weight_kg / (height_m * height_m)


def calculate_risk(payload: RiskAssessmentRequest) -> RiskAssessmentResponse:
    """Простая rule-based логика для учебного MVP."""
    score = 0

    bmi = _calculate_bmi(payload.height_cm, payload.weight_kg)

    if payload.age >= 60:
        score += 3
    elif payload.age >= 45:
        score += 2

    if bmi >= 30:
        score += 3
    elif bmi >= 25:
        score += 2

    if payload.physical_activity == "low":
        score += 2
    elif payload.physical_activity == "medium":
        score += 1

    if payload.family_history_diabetes:
        score += 2

    if payload.high_sugar_intake:
        score += 1

    if payload.high_blood_pressure_history:
        score += 2

    if score >= 8:
        risk_level = "высокий риск"
        recommendation = (
            "Рекомендуется в ближайшее время обратиться к врачу для подробной оценки состояния."
        )
    elif score >= 4:
        risk_level = "средний риск"
        recommendation = (
            "Желательно скорректировать образ жизни и запланировать профилактическую консультацию."
        )
    else:
        risk_level = "низкий риск"
        recommendation = (
            "Сохраняйте текущие привычки и периодически проходите профилактический контроль."
        )

    return RiskAssessmentResponse(
        score=score,
        risk_level=risk_level,
        recommendation=recommendation,
    )
