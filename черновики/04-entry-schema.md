# JSONSchema для EntryDraft и Entry

## 1. Размещение схем
- **Каталог**: `frontend/src/lib/server/schemas/`.
- **Файлы**:
  - `entry-draft.schema.json` — схема данных, которые приходят на фронт от AI/визарда до сохранения (Draft).
  - `entry.schema.json` — схема итоговой записи (как хранится в FastAPI/PostgreSQL).
- **API**: роут `GET /api/config/entry-schema` возвращает обе схемы (`draft`, `entry`, `version`), фронт использует их для генерации типов и валидации.
- **Генерация типов**: `pnpm run generate:schemas` → дергает `json-schema-to-typescript` и складывает типы в `src/lib/types/generated/`.

## 2. EntryDraft
- Идентификатор: `id` (опционально) — клиентский UID.
- Структура:
  - `action`, `object`, `title`, `note`, `category`, `subcategory`, `tags[]`.
  - `amount`, `currency`, `date`, `people[]`, `placeText`, `geo`, `attachments[]`, `syncState`.
  - `aiMeta`: `model`, `confidence`, `source`, `clarifyingQuestions[]`, `promptVersion`, `recipeCandidateId`.
  - `status`: `draft | rejected | confirmed`.
  - `version`: целое число, зафиксированное перед синхронизацией.
  - `context`: `EntryContext` (JSON для будущих полей — финансы, адреса, метрики, планирование).

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pickpock.app/schema/entry-draft",
  "title": "EntryDraft",
  "type": "object",
  "required": ["action", "object", "status"],
  "properties": {
    "id": { "type": "string" },
    "action": { "type": "string", "enum": ["noted", "visited", "planned", "spent", "received", "lent", "borrowed", "returned", "bought", "gave", "took"] },
    "object": { "type": "string", "enum": ["money", "place", "food", "item", "service", "wish", "task", "note"] },
    "title": { "type": "string", "maxLength": 280 },
    "note": { "type": "string" },
    "category": { "type": "string", "maxLength": 64 },
    "subcategory": { "type": "string", "maxLength": 64 },
    "tags": { "type": "array", "items": { "type": "string" }, "maxItems": 12 },
    "amount": { "type": "number" },
    "currency": { "type": "string", "minLength": 3, "maxLength": 3 },
    "date": { "type": "string", "format": "date-time" },
    "people": { "type": "array", "items": { "type": "string" }, "maxItems": 10 },
    "placeText": { "type": "string" },
    "geo": { "$ref": "#/$defs/GeoPoint" },
    "attachments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "name": { "type": "string" },
          "type": { "type": "string" },
          "size": { "type": "number" },
          "url": { "type": "string", "format": "uri" }
        },
        "required": ["id", "name", "type", "size"]
      },
      "maxItems": 10
    },
    "aiMeta": {
      "$ref": "#/$defs/AIMeta"
    },
    "status": { "type": "string", "enum": ["draft", "rejected", "confirmed"] },
    "version": { "type": "integer", "minimum": 1 },
    "syncState": { "type": "string", "enum": ["local-only", "pending", "synced"] },
    "context": { "$ref": "#/$defs/EntryContext" }
  },
  "additionalProperties": false,
  "$defs": {
    "GeoPoint": {
      "type": "object",
      "properties": {
        "lat": { "type": "number", "minimum": -90, "maximum": 90 },
        "lng": { "type": "number", "minimum": -180, "maximum": 180 },
        "accuracy": { "type": "number" }
      },
      "required": ["lat", "lng"]
    },
    "AIMeta": {
      "type": "object",
      "properties": {
        "model": { "type": "string" },
        "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
        "source": { "type": "string", "enum": ["text", "photo", "url", "recipe"] },
        "clarifyingQuestions": {
          "type": "array",
          "items": { "type": "string" },
          "maxItems": 5
        },
        "promptVersion": { "type": "string" },
        "recipeCandidateId": { "type": "string" }
      }
    },
    "EntryContext": {
      "type": "object",
      "properties": {
        "finance": {
          "type": "object",
          "properties": {
            "merchant": { "type": "string" },
            "store": { "type": "string" },
            "cardLast4": { "type": "string", "pattern": "^[0-9]{4}$" },
            "iban": { "type": "string" },
            "account": { "type": "string" },
            "invoice": { "type": "string" },
            "billId": { "type": "string" },
            "receiptNumber": { "type": "string" }
          }
        },
        "location": {
          "type": "object",
          "properties": {
            "address": { "type": "string" },
            "city": { "type": "string" },
            "country": { "type": "string" },
            "zip": { "type": "string" },
            "region": { "type": "string" },
            "street": { "type": "string" },
            "building": { "type": "string" },
            "apartment": { "type": "string" }
          }
        },
        "metrics": {
          "type": "object",
          "properties": {
            "rating": { "type": "number", "minimum": 0, "maximum": 5 },
            "quantity": { "type": "number" },
            "unit": { "type": "string" },
            "distance": { "type": "number" },
            "calories": { "type": "number" },
            "duration": { "type": "number" },
            "mood": { "type": "string" },
            "weather": { "type": "string" },
            "temperature": { "type": "number" }
          }
        },
        "planning": {
          "type": "object",
          "properties": {
            "startTime": { "type": "string", "format": "date-time" },
            "endTime": { "type": "string", "format": "date-time" },
            "time": { "type": "string" },
            "recurrence": { "type": "string" },
            "project": { "type": "string" }
          }
        },
        "contacts": {
          "type": "object",
          "properties": {
            "phone": { "type": "string" },
            "email": { "type": "string", "format": "email" },
            "website": { "type": "string", "format": "uri" },
            "social": { "type": "string" }
          }
        },
        "extras": {
          "type": "object",
          "additionalProperties": true
        }
      },
      "additionalProperties": true
    }
  }
}
```

> Примечание: значения `category`/`subcategory` берём из `GET /api/config/categories` и конфигурации рецептов; схема намеренно не содержит enum, чтобы каталог можно было расширять без её обновления.

## 3. Entry
- Все поля из Draft плюс:
  - `entryId` (UUID записи в PostgreSQL), `userId`, `created`, `updated`, `spaceId`.
  - `recipeSelectedId` (какой рецепт выбрал пользователь), `recipeVersion`.
  - `extras`: JSONB (метрики, ссылки, кастомные поля из рецептов).
  - `aiRaw`: оригинальный ответ AI (string), `aiConfidence`.
  - `syncedAt`, `deletedAt`, `syncState`, `conflictState`.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pickpock.app/schema/entry",
  "title": "Entry",
  "allOf": [
    { "$ref": "https://pickpock.app/schema/entry-draft" },
    {
      "type": "object",
      "required": ["pbId", "userId", "created", "updated", "status"],
      "properties": {
        "pbId": { "type": "string" },
        "userId": { "type": "string" },
        "spaceId": { "type": "string" },
        "recipeId": { "type": "string" },
        "recipeSelectedId": { "type": "string" },
        "recipeVersion": { "type": "integer" },
        "extras": { "type": "object", "additionalProperties": true },
        "aiRaw": { "type": "string" },
        "aiConfidence": { "type": "number", "minimum": 0, "maximum": 1 },
        "syncedAt": { "type": "string", "format": "date-time" },
        "deletedAt": { "type": "string", "format": "date-time" },
        "conflictState": { "type": "string", "enum": ["none", "local-newer", "server-newer"] },
        "created": { "type": "string", "format": "date-time" },
        "updated": { "type": "string", "format": "date-time" }
      }
    }
  ]
}
```

## 4. API контракт
- `GET /api/config/entry-schema` → `{ "version": "2026-01-10", "draft": {...}, "entry": {...} }`.
- `POST /api/entries` валидирует входные данные против `entry.schema.json` (server-side), FastAPI принимает только проверенные поля.
- `POST /api/ai/analyze` возвращает объект, прошедший проверку `EntryDraft` (AI не может прислать лишние поля).
- Клиент: при загрузке приложения запрашивает схемы → генерирует типы (`EntryDraft`, `Entry`) и использует их в формах, сторе и IndexedDB.
- Схемы версионируются: поле `version` в API отвечает за backward-compatibility; изменения документируем в `/docs/04-entry-schema.md`.

## 5. Следующие шаги
1. Создать каталог `frontend/src/lib/server/schemas/` и добавить JSON-файлы, включая `$defs`.
2. Реализовать helper `getEntrySchemas()` в `src/lib/server/schema.ts`, который кеширует схемы и отдаёт их роуту `/api/config/entry-schema`.
3. Настроить генерацию типов (`json-schema-to-typescript`) + подключить ESLint rule, запрещающий импорт устаревших типов.
4. Для PostgreSQL/IndexedDB хранить `syncState` и `conflictState`, чтобы UI понимал статус записи.
5. Описать единый словарь `action/object` (например, `src/lib/config/semantic.ts`) и предусмотреть механизм расширения/alias, чтобы схема могла ссылаться на него или автоматически пересобираться.

