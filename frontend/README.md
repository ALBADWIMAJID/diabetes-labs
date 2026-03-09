# Frontend (Lab 3)

Минимальный UI для MVP системы предварительной оценки риска диабета 2 типа.

## Что реализовано
- Одна страница с описанием и дисклеймером.
- Форма анкеты с базовой клиентской валидацией.
- Отправка данных в backend endpoint `POST /risk-assessment`.
- Отображение `score`, `risk_level`, `recommendation`, `explanation`.

## Локальный запуск
```bash
cd frontend
python -m http.server 5500
```

Открыть: `http://localhost:5500`

По умолчанию API: `http://localhost:8000`
(при необходимости можно изменить константу `API_BASE_URL` в `script.js`).
