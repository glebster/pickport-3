# Глобальный план

Документы распределены так:
- `01-ponyal.md` — понимание продукта и архитектуры.
- `02-plan.md` — общий план (что строим и как остаётся под контролем).
- `08-roadmap.md` — этапы/очерёдность.
- `05-log.md` — факт выполнения.

## 1. Что создаём

| Направление | Цель | Основные элементы |
|-------------|------|--------------------|
| Продукт | Личный «карманный дневник» с формулой `Entry = Action + Object + Context`. | Визард `/new`, лента/дашборд, семантический поиск/чат, каталог рецептов, настройки, возможность добавлять пользовательские рецепты и поля. |
| Архитектура | Монорепо SvelteKit 5 + FastAPI + PostgreSQL + Redis + Celery + IndexedDB + object storage. | `frontend/`, `backend/`, `common/`, `docker/`. |
| Данные/AI | Единые JSON Schema, AI-анализ (OpenRouter) для заполнения полей и подсказок. | `common/schemas`, генерация TS/Pydantic, `aiRaw`/`aiMeta`. |
| Sync & Offline | IndexedDB + сервис-воркер + `/api/sync/*`. | Черновики локально, сервер — источник истинных UUID. |
| Observability/Security | Telemetry по умолчанию, health-check, логирование, auth baseline. | loguru, метрики, rate limiting, data quality. |

## 2. Карта работ (высокоуровнево)

1. **Ядро данных** — Entries CRUD, конфиги/словари, схемы, базовые API.
2. **Sync + Background** — `/api/sync/*`, reminders, Celery задачи, обработка файлов.
3. **AI/UX расширения** — мульти-драфты, рекомендации, расширенный поиск/статистика.
4. **Observability & Security** — метрики, телеметрия, alerting, auth.
5. **Платформы** — PWA/Capacitor упаковки, оффлайн режимы, экспорт/импорт.

Детализированная последовательность живёт в `docs/08-roadmap.md` (этапы G0→G5).

## 3. Ближайшие шаги (G1-G2)

1. **Миграции**: `poetry run alembic upgrade head`, автопроверка миграций.
2. **API `/api/v1/entries`**: Pydantic схемы, CRUD, pytest.
3. **Frontend sync**: SvelteKit тянет схемы с backend, IndexedDB адаптер.
4. **Подготовка к sync**: черновики `/api/v1/sync/state`, Celery worker, health-check Postgres/Redis.

## 4. Контроль

- Roadmap — `docs/08-roadmap.md`.
- Журнал — `docs/05-log.md`.
- Открытые вопросы/блокеры — `docs/03-pipeline.md`.
- Чек-лист тестов — TODO (добавить на этапе интеграционных тестов).
