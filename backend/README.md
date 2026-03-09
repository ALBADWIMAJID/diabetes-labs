# Backend (Lab 3)

Минимальный backend для MVP учебной системы предварительной оценки риска диабета 2 типа.

## Реализованные endpoints
- `GET /health` — проверка доступности сервиса.
- `POST /risk-assessment` — расчет риска по анкете.

## Формат ответа `POST /risk-assessment`
- `score` — итоговый балл.
- `risk_level` — категория риска (`низкий риск`, `средний риск`, `высокий риск`).
- `recommendation` — краткая рекомендация.
- `explanation` — пояснение, какие факторы повлияли на результат.

## Локальный запуск
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Пример запроса
```json
{
  "age": 52,
  "height_cm": 170,
  "weight_kg": 82,
  "physical_activity": "low",
  "family_history_diabetes": true,
  "high_sugar_intake": true,
  "high_blood_pressure_history": false
}
```

## Ограничение
Данный backend реализует учебный rule-based baseline и не является клинической диагностической системой.
