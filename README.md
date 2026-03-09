# Проект: Разработка системы оценки риска диабета 2 типа

## Общая цель
Репозиторий содержит последовательные лабораторные работы по учебному проекту веб-системы **предварительной** оценки риска диабета 2 типа.

Проект не является медицинской диагностической системой и не заменяет консультацию врача.

## Логика развития по лабораторным
- **Lab 1 (анализ):** формализация проблемы, требований, сценариев и ролей.
- **Lab 2 (проектирование):** архитектура, дизайн-решения, baseline-логика и план реализации.
- **Lab 3 (MVP-прототип):** интегрированный frontend + backend с рабочим сквозным сценарием.

## Реализовано в MVP (Lab 3)
- Backend (FastAPI):
  - `GET /health`
  - `POST /risk-assessment`
- Frontend (HTML/CSS/JS):
  - анкета пользователя;
  - отправка данных в API;
  - отображение `score`, `risk_level`, `recommendation`, `explanation`.
- Rule-based логика оценки риска без БД и авторизации.

## Основной пользовательский сценарий
1. Пользователь открывает страницу frontend.
2. Заполняет анкету (возраст, рост, вес, активность и дополнительные факторы).
3. Нажимает кнопку расчета.
4. Frontend отправляет данные в `POST /risk-assessment`.
5. Backend рассчитывает балл и категорию риска.
6. Пользователь видит результат и краткие рекомендации.

## Структура репозитория
- `docs/` — документация Lab 1, Lab 2, Lab 3
- `backend/` — API и логика расчета риска
- `frontend/` — интерфейс анкеты и отображение результата
- `.env.example` — пример минимальных переменных окружения

## Карта документов
### Lab 1
- `docs/prd.md`
- `docs/usecases.md`
- `docs/stakeholders.md`
- `docs/raci.md`

### Lab 2
- `docs/architecture.md`
- `docs/design-notes.md`
- `docs/sprint-plan.md`
- `docs/ai-deliverables.md`

### Lab 3
- `docs/requirements-v2.md`
- `docs/integration-report.md`

## Быстрый локальный запуск
### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Проверка:
- `http://localhost:8000/health`
- `http://localhost:8000/docs`

### Frontend
```bash
cd frontend
python -m http.server 5500
```

Открыть в браузере: `http://localhost:5500`

По умолчанию frontend обращается к API: `http://localhost:8000`.
