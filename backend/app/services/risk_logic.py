from app.schemas import RiskAssessmentRequest, RiskAssessmentResponse


def _calculate_bmi(height_cm: float, weight_kg: float) -> float:
    height_m = height_cm / 100
    return weight_kg / (height_m * height_m)


def calculate_risk(payload: RiskAssessmentRequest) -> RiskAssessmentResponse:
    """Простая rule-based логика для учебного MVP."""
    score = 0
    factors: list[str] = []

    bmi = _calculate_bmi(payload.height_cm, payload.weight_kg)

    if payload.age >= 60:
        score += 3
        factors.append("возраст 60+")
    elif payload.age >= 45:
        score += 2
        factors.append("возраст 45-59")

    if bmi >= 30:
        score += 3
        factors.append("ИМТ 30+")
    elif bmi >= 25:
        score += 2
        factors.append("ИМТ 25-29.9")

    if payload.physical_activity == "low":
        score += 2
        factors.append("низкая физическая активность")
    elif payload.physical_activity == "medium":
        score += 1
        factors.append("средняя физическая активность")

    if payload.family_history_diabetes:
        score += 2
        factors.append("семейная история диабета")

    if payload.high_sugar_intake:
        score += 1
        factors.append("частое потребление сахара")

    if payload.high_blood_pressure_history:
        score += 2
        factors.append("повышенное давление в анамнезе")

    if score >= 8:
        risk_level = "высокий риск"
        recommendation = (
            "Рекомендуется обратиться к врачу для дополнительной оценки состояния."
        )
    elif score >= 4:
        risk_level = "средний риск"
        recommendation = (
            "Желательно скорректировать образ жизни и запланировать профилактическую консультацию."
        )
    else:
        risk_level = "низкий риск"
        recommendation = (
            "Рекомендуется поддерживать текущие полезные привычки и регулярно проходить профилактический контроль."
        )

    if factors:
        explanation = "На результат повлияли факторы: " + ", ".join(factors) + "."
    else:
        explanation = "Выраженные факторы риска по выбранной анкете не выявлены."

    return RiskAssessmentResponse(
        score=score,
        risk_level=risk_level,
        recommendation=recommendation,
        explanation=explanation,
    )
