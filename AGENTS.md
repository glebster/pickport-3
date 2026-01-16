# AGENTS.md

## Проект
- Local-first PWA на SvelteKit 5 (TypeScript, Tailwind) в `apps/pwa`.
- Mobile-first: основной таргет — телефон/PWA, desktop потом при необходимости.
- Backend FastAPI + Postgres в `apps/backend`; Alembic миграции в `apps/backend/alembic`.
- Локальная БД клиента: IndexedDB (обвязка в `apps/pwa/src/lib/shared`).
- AI слой — прокси в backend (`app/ai`), провайдер выбирается конфигом; контент пользователя не логируем.

## Структура
- `apps/pwa/src/routes` — роуты SvelteKit.
- `apps/pwa/src/lib/domain` — типы/схемы (Entry/List/Recipe/Reminder/Group), `api.types.ts` генерить из OpenAPI.
- `apps/pwa/src/lib/{features,entities,components,shared}` — фичи, сущности, UI, теххелперы/IndexedDB.
- `apps/backend/app/{api,schemas,services,repositories,core,common,ai}` — роуты, схемы Pydantic, сервисы, PG-репозитории, конфиг/DI, хелперы, AI.
- `config/` — рецепты/категории (json/yaml), `.env.example`.
- `db/` — SQL/DDL/дампы (если нужны вне Alembic).
- `docker/` — compose/Dockerfile/скрипты.
- `docs/` — product / ux / architecture / roadmap.

## Команды (по умолчанию)
- PWA: `cd apps/pwa && npm install && npm run dev`.
- Backend: `cd apps/backend && python -m venv .venv && source .venv/bin/activate (или .venv\\Scripts\\activate)`; затем `pip install -r requirements.txt` (или `uv/poetry` когда появится). Запуск: `uvicorn app.main:app --reload` (уточнить точку входа, когда будет создана).
- Генерация типов API для фронта: `cd apps/pwa && npx openapi-typescript http://localhost:8000/openapi.json -o src/lib/domain/api.types.ts`.

## Требования/конвенции
- PWA: offline-first, данные храним локально, синхронизация и AI — опционально.
- Backend: хранит минимум (user/device UUID, телеметрию без контента), контент не логируется.
- Логи AI: только request_id/model/latency/tokens/cost, без текста.
- Без общих utils между стеками; домен фронта локализован в `src/lib/domain`.
- Используем TypeScript strict, Tailwind подключён.
- Всегда сверяться с официальной докой и best practices: Svelte 5 (кодекс Svelte 5), Tailwind, FastAPI (официальный гайд/кодекс), shadcn-svelte. Не вносить паттерны в обход рекомендаций.
- Хранилище: клиентская сторона — IndexedDB (обвязка в `apps/pwa/src/lib/shared`), сервер — Postgres c Alembic-миграциями; не смешивать слои и не плодить дублирование данных.
- UI/адаптив: mobile-first, контейнер `max-w-md`, не растягивать десктоп. Отступы/иерархию сверять с UX-доками (17, 19).
- Tailwind v4: кастомные цвета/токены только через `@theme` и `--color-*`, без инлайновых hex. Утилиты должны быть из известного набора (избегать неизвестных классов).
- Svelte 5: runes-режим, избегать устаревших конструкций (`<svelte:component>`, `{@html}` без необходимости). Сверяться с кодексом Svelte 5 перед добавлением паттернов.
- Логи: не логировать пользовательский контент; для AI — только request_id/model/latency/tokens/cost. Логи разработки держать лаконичными, без излишних деталей.
- Данные: единый источник демо-данных (`static/demo-data.json` или `src/lib/mocks`), не плодить дубликаты фикстур.
- Иконки/цвет: lucide-svelte; бренд — emerald-500, secondary — нейтральный (slate), без бирюзы для secondary.
- Чеки перед коммитом: фронт — `npm run check`/линты (когда появятся); бэк — `pytest`/линты (когда настроены).
- Тени: применять минимум, только при явной необходимости (подсветка action/overlay). Не раскидывать shadow-* без задачи; по умолчанию — без теней.
- SSR: любое решение/рендер не должен ломать SSR; следить за серверными ошибками (vite ssr) и избегать конструкций, не совместимых с SSR.
- Svelte 5 runes: используем `{@render ...}` вместо `<slot>` в runes-компонентах, не смешиваем слоты и `{@render}`.

## Приоритеты и проверки
- Сначала следовать пользовательской доке (docs/*.md), затем этому файлу.
- Перед изменениями кода — сверяться с архитектурой (06, 18), UX (17, 19), best practices (10).
- После правок фронта — `npm run check` / `npm run lint` (когда появятся).
- После правок бэка — `pytest`/линты (когда будут настроены).

## Безопасность/данные
- Не сохранять/не логировать пользовательский контент в backend.
- UUID генерируются локально; синхронизация включается только явным opt-in.

## UI/дизайн-система
- Используем shadcn-svelte как базу компонентов. Не подтягиваем `Card`, карточки делаем свои под контекст (Entry/List). Базовые элементы (Button/Input/Form/Dialog/Tabs/Tooltip/Toast и т.п.) можно брать из shadcn-сета.
- Брендовый цвет — Tailwind `emerald` (логотип в #10b981 / emerald-500). Палитра, где надо emerald.
- Иконки: lucide-svelte, (см. https://lucide.dev/icons/); уже стоят.

## Рабочие файлы
- `PLAN.md` — актуальный чеклист задач; перед стартом новой задачи обновляй/добавляй пункты.
- `LOG.md` — журнал выполненного; после каждого блока работы добавляй краткий пункт.
- Если меняешь правила/паттерны (структура, команды, дизайн-система) — обнови AGENTS.md сразу, чтобы в следующей сессии было актуально.

