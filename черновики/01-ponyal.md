# Что я понял из текущих материалов

## Продукт и сценарии
- PickPock — персональный «карманный дневник» жизненных событий; базовая сущность `Entry = Action + Object + Context`.
- Главные UX-потоки: мультимодальный визард `/new`, лента/дашборд, семантический поиск и чат, каталог рецептов/категорий, настройки.
- Источники данных сейчас: текст, фото, URL, выбор рецепта; остальные (голос, QR, импорт) отложены.
- Action/Object имеют фиксированный словарь (можно расширять через recipes). Категории/подкатегории приходят из `/api/config/categories`.

## Данные и AI
- Поля формы описаны конфигами (`fields.ts` → `common/schemas`), есть секции finance/location/metrics/planning/contacts.
- AI (через OpenRouter) парсит ввод, заполняет обозначенные `aiKey` поля, создаёт мульти-драфты, ведёт диалог для уточнений; при низкой уверенности ставим `noted + note`.
- AI-ответы (`aiRaw`, `aiMeta`) сохраняются для отладки/обучения.

## Архитектура
- Фронтенд: SvelteKit 5 + shadcn-svelte, IndexedDB для оффлайна, PWA-only, позже Capacitor.
- Backend: FastAPI + PostgreSQL + Redis/Celery + object storage (S3/MinIO). Общие JSON Schema лежат в `common/schemas`, FastAPI отдаёт их через `/api/v1/config/entry-schema`.
- Стек развёрнут в монорепо: `frontend/`, `backend/`, `common/`, `docker/`.
- Sync-протокол `/api/sync/state|push|pull` запланирован, но пока не реализован; та же история с reminders, dictionaries, расширенным search/stats.

## Принципы и целевые практики
- Offline-first + optimistic UI, единый источник правды для схем/конфигов, телеметрия «по умолчанию», безопасное хранение и UUID для всех сущностей.
- Не перегружаем MVP: сначала ядро Entry + конфиги, затем расширения (sync, reminders, AI automation).

## Текущее состояние (G0)
- Документация обновлена под стек SvelteKit 5 + FastAPI/PostgreSQL.
- JSON Schema вынесены в `common/schemas`, действует генерация TS/Pydantic типов (`npm run generate:schemas`).
- Backend и Docker окружение инициализированы, есть Alembic + модель `entries`, эндпоинт `/api/v1/config/entry-schema`.
- Roadmap (G0→G5) зафиксирован в `docs/08-roadmap.md`, лог работ — в `docs/05-log.md`.

