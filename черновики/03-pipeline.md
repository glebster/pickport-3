# Организация пайплайна и рабочих процессов

## 1. Сквозной пользовательский пайплайн
1. **Захват сигнала**: текст, голос, фото, URL, повтор записи, выбор рецепта.  
   _Улучшения_: привести источники к единому интерфейсу `SourceAdapter`, чтобы проще расширять (например, email-forward).
2. **AI-анализ** (`ai/analyze`) → canonical `Action + Object + Context`.  
   _Улучшения_: жёстко фиксировать версию схемы в ответе и валидировать на клиенте до показа пользователю.
3. **Clarify & Drafts**: AI-уточнения, выбор рецепта, мульти-драфты.  
   _Улучшения_: хранить выбор пользователя (принятый/отклонённый драфт) в `entries.aiMeta` для дальнейшего обучения.
4. **Recipe Form**: автозаполнение полей, ручные правки, проверка обязательных.  
   _Улучшения_: унифицировать секции формы через JSONSchema → можно генерировать UI и серверную валидацию из одного описания.
5. **Сохранение + синхронизация**: optimistic UI → IndexedDB → FastAPI `/api/entries` → PostgreSQL → мердж в стор.  
   _Улучшения_: внедрить версионирование записей (`version`, `updatedAtClient`) и эвристику автоконфликта, хранить `syncedAt`/`conflictState`.
6. **Пост-обработка**: логирование, телеметрия, фоновые задачи (resize фото, индексация поиска).  
   _Улучшения_: вынести в очередь (например, Flower/Celery или lightweight worker) с DLQ для проблемных записей.

## 2. Логическая структура репозитория
- `frontend/`: SvelteKit 5 PWA + Capacitor обвязка, IndexedDB слой.
- `backend/`: FastAPI + PostgreSQL + Redis/Celery (CRUD, AI, синк, observability).
- `common/`: типы данных, JSONSchema, конфиги рецептов/полей (shared между фронтом и бэком).
- `infrastructure/`: docker-compose, Terraform/Ansible, CI/CD workflows.

_Рекомендации_:
- Перевести конфиги рецептов и полей в `common/config/` и генерировать typed выходы через build-скрипт → исключить несинхронность.
- Добавить слой `pkg/ai/` с адаптерами под разные провайдеры, чтобы легко переключать OpenRouter ↔ локальные модели.

## 3. Технический пайплайн данных
```
Source -> AI Analyze -> Clarify -> RecipeForm -> FastAPI /api/entries -> PostgreSQL/S3
      -> Celery Post-processing -> Sync Service (IndexedDB <-> FastAPI /api/sync) -> Search/Vector Index -> Observability
```
- **Normalization**: каждый шаг пишет данные в нормализованный `EntryDraft`, избегая потери контекста.
- **Metadata**: поле `aiMeta` содержит `model`, `promptVersion`, `confidence`, `clarifications`.
- **Search**: после сохранения запускаем обновление векторного индекса (локально или в бэкенде), чтобы чат/поиск получал свежие результаты.
- **Auditing**: все критичные переходы (draft accepted, entry saved, sync resolved) логируются в единую шину событий → пригодно для аналитики воронки.

## 4. Организация команды и релизов
- **Итерации по сценариям**: собирать end-to-end vertical slice (источник → запись → поиск), а не отдельные технические задачи.
- **Design Review → Dev Plan → Build → Dogfooding → Release**: фиксировать чек-лист, чтобы не пропускать обновление документации и smoke-тесты.
- **QA Definition**: автоматизировать smoke через FastAPI fixtures + Playwright (ключевые flow `/new`, чат, sync, offline).
- **Release Train**: раз в 2 недели – стабилизация, freeze рецептов, обновление `/docs` и логов изменений.

## 5. Observability & качество
- **Client logger** отправляет события в ingestion API, откуда попадает в ClickHouse/BigQuery.
- **Server metrics**: latencies по `ai/analyze`, `entries`, размер payload → алерты на SLO.
- **Data QA**: периодически гонять скрипт `scripts/validate-entries.ts`, который проверяет заполненность ключевых полей, расхождения сумм и т.д.
- **Feedback loop**: UI позволяет помечать запись “AI ошибся” → эта метка попадает в `aiMeta.feedback` и используется для обучения.

## 6. Следующие шаги для структурирования
1. Создать `docs/architecture-api.md` mindmap-пункт «Пайплайны» и включить диаграмму данных.
2. Сгенерировать JSONSchema для `EntryDraft` и `Entry` и подключить её к фронту/бэку.
3. Настроить CI, который проверяет синхронизацию конфигов (recipes/fields), генерацию схем и наличие Alembic миграций.

## 7. Лучшие практики
- **Single Source of Truth**: конфиги рецептов, полей, типов данных живут в `common/` и проходят генерацию типизированных клиентов → исключаем расхождения между фронтом и бэком.
- **Schema-first**: все API описываются OpenAPI/JSONSchema, из них генерируются клиенты, тестовые фикстуры и валидация форм.
- **Telemetry by default**: каждый новый маршрут и UI-экран сразу добавляют метрики/события, без этого фича считается неполной.
- **Feature toggles**: крупные изменения оборачиваются в фичи-флаги, чтобы безопасно включать их для тест-группы.
- **Offline-first тесты**: критические сценарии проверяются в e2e как в онлайн, так и при отключённой сети.
- **Security baseline**: все данные AI/файлов проходят фильтры (size/type), ключи и токены хранятся только в `.env.local`, логи не содержат PII.

### Pragmatic-first подход
- Используем `MVP slices`: на ранних этапах документацию/схемы можно поддерживать в упрощённом виде (например, `zod` схемы на фронте), а полную генерацию OpenAPI включать по мере стабилизации API.
- Telemetry собираем через лёгкий клиент (например, `console batch upload`) с последующим переходом на полноценный ingestion, чтобы не тормозить разработку UX.
- Для offline/Capacitor сначала покрываем smoke-кейсы ручным чек-листом, а автоматизацию Playwright подключаем после того, как сценарии устаканятся.
- Feature toggles можно начать с простого `config.json + localStorage`, а уже потом переносить во внешний сервис.

## 8. Связка с планом развития API
- **Config-first**: выносим `fields/recipes/categories` в `/api/config/*`, чтобы визард и AI всегда читали актуальные формы без пересборки.
- **Entries+Search**: расширяем `/api/entries` параметрами (фильтры, пагинация, stats) и добавляем `/api/entries/search` для лёгкого поиска; семантический `/api/ai/search` остаётся комплементарным.
- **Dictionaries & Import**: `GET /api/dictionaries/{tags,people,places}` и `POST /api/import/{qr,voice}` нужны пайплайну на шагах clarify/form, чтобы AI и пользователь имели единые подсказки.
- **Reminders/Notifications**: отдельный блок API для напоминаний и inbox, события которого подключаются к пайплайну post-processing.
- **Sync layer**: `/api/sync/state|push|pull` поддерживает оффлайн и versioning; логика конфликтов завязана на `EntryDraft.version` из шага 5 пайплайна.
- **Backend split**: по мере роста тяжёлые задачи (OCR, batch AI) переводятся на FastAPI + Celery с WebSocket уведомлениями (`task:{id}`), фронт остаётся тонким клиентом.

