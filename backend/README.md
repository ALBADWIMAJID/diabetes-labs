# Backend (Lab 2)

Минимальный backend для учебной системы предварительной оценки риска диабета 2 типа.

## Что реализовано
- `GET /health` — проверка доступности API
- `POST /risk-assessment` — расчет `score`, `risk_level`, `recommendation`
- Rule-based логика без базы данных

## Локальный запуск
1. Перейти в папку `backend`
2. Установить зависимости:
   - `pip install -r requirements.txt`
3. Запустить сервер:
   - `uvicorn app.main:app --reload --port 8000`

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
