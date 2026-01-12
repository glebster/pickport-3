# Сущности и поля (понятно и по шагам)

Структура: (A) что за сущности и зачем; (B) связи; (C) поля с типами. `ai_raw/ai_meta/payload/diff/result` — JSONB.

---

## A) Что за сущности (коротко и по-людски)
- **users** — учётки людей в системе.
- **spaces** — отдельные «рабочие папки» с данными.
- **memberships** — кто в какой папке и с какой ролью.
- **categories / subcategories** — дерево групп, чтобы раскладывать действия/объекты.
- **objects / actions / pairs** — словари «что» и «что сделал» + допустимые сочетания.
- **entries** — сами записи дневника.
- **files** — просто факты о файле (имя, размер, mime).
- **attachments** — какие файлы прикреплены к записи и какую роль играют (preview/source/ocr).
- **insights** — что ИИ понял про файл (summary, теги, места).
- **fields / formsets** — список полей и наборы полей для форм.
- **extensions** — всё пользовательское (свои поля/категории/пары) одним JSON-хранилищем.
- **recipes / toggles** — шаблоны сценариев и включение/выключение этих шаблонов.
- **tags / people / places / currencies** — словари для подсказок и автодополнений.
- **ai_jobs / ai_usage** — задачи ИИ и расход токенов.
- **reminders / notifications / tokens** — напоминания, inbox событий, push-токены.
- **preferences / settings** — личные и глобальные настройки.
- **lists / listitems** — сохранённые подборки (roadmap).
- **versions / syncs / activity** — версии изменений, синхронизация, аудит.

---

## B) Как связаны (очень кратко)
- У каждого `space` свои `entries`, `files`, `lists`, `ai_jobs`, `reminders`, `notifications`.
- Пользователь попадает в `space` через `memberships` и получает роль.
- В каждой `entry` всегда есть `action` + `object`, часто есть `category`/`subcategory`.
- Что можно сочетать, фиксирует `pairs`; всё, что добавил пользователь, лежит в `extensions`.
- `entries` привязываются к `files` через `attachments`; расшифровка файла ИИ хранится в `insights`.
- `recipes` строятся на `action/object` (+ category/subcategory) и берут поля из `formsets`; `toggles` решают, включён ли рецепт; кастомные поля/категории подмешиваются из `extensions`.
- `reminders` и `notifications` могут ссылаться на `entry`; `ai_jobs`/`insights` могут ссылаться на файл или запись.
- История/синк: `versions` следят за изменениями записей, `syncs` — за обменом данных в space, `activity` — за действиями пользователя.

---

## C) Поля и типы (key | описание | тип)

### Users / Spaces
- users: `id` (uuid), `email` (string), `status` (enum), `created_at` (ts); доп. `name` (string), `avatar_url` (url), `timezone` (string), `locale` (string), `password_hash` (string), `deleted_at` (ts).
- spaces: `id` (uuid), `owner_id` (uuid), `name` (string), `created_at` (ts); доп. `icon` (string), `color` (string), `description` (text), `settings` (jsonb), `deleted_at` (ts).
- memberships: `id` (uuid), `space_id` (uuid), `user_id` (uuid), `role` (enum owner/editor/viewer), `created_at` (ts); доп. `invited_by` (uuid), `accepted_at` (ts), `removed_at` (ts).

### Семантика
- categories: `id` (uuid), `code` (string), `label` (string); доп. `description` (text), `icon` (string), `color` (string), `sort` (int), `enabled` (bool), `ai_hint` (text).
- subcategories: `id` (uuid), `category_id` (uuid), `code` (string), `label` (string); доп. `description`, `icon`, `sort`, `enabled`, `ai_hint`.
- objects: `id` (uuid), `code` (string), `label` (string); доп. `category_id`, `subcategory_id`, `description`, `icon`, `is_default` (bool), `ai_hint`.
- actions: `id` (uuid), `code` (string), `label` (string); доп. `category_id`, `subcategory_id`, `description`, `icon`, `is_default`, `ai_hint`.
- pairs: `id` (uuid), `object_id` (uuid), `action_id` (uuid); доп. `category_id`, `subcategory_id`, `enabled` (bool), `sort` (int).

### Entries и файлы
- entries (обяз.): `id` (uuid), `user_id` (uuid), `space_id` (uuid), `status` (enum), `date` (date), `action_id` (uuid), `object_id` (uuid), `title` (string), `created_at` (ts), `updated_at` (ts).
- entries (доп.): `note` (text), `amount` (money/number), `currency` (string), `tags` (string[]), `people` (string[]/uuid[]), `category_id` (uuid), `subcategory_id` (uuid), `place_text` (string), `geo` (point/json), `attachments` (string[]), `extras` (jsonb), `ai_confidence` (number), `ai_source` (enum text/photo/url/voice), `ai_model` (string), `ai_version` (string), `ai_raw` (jsonb), `ai_meta` (jsonb), `ai_flags` (string[]), `ai_notes` (text), `deleted_at` (ts).
- files: `id` (uuid), `user_id` (uuid), `space_id` (uuid), `filename` (string), `mime` (string), `size` (int), `created_at` (ts); доп. `checksum` (string), `width` (int), `height` (int), `duration` (int), `storage_key` (string), `deleted_at` (ts).
- attachments: `id` (uuid), `entry_id` (uuid), `file_id` (uuid); доп. `role` (enum preview/source/ocr/other), `sort` (int).
- insights: `id` (uuid), `file_id` (uuid), `summary` (text), `ai_model` (string); доп. `objects` (string[]), `places` (string[]), `tags` (string[]), `confidence` (number), `ai_meta` (jsonb), `raw` (jsonb).

### Поля/формы/рецепты
- fields: `id` (uuid), `code` (string), `label` (string), `type` (enum), `serialize` (enum string/number/json); доп. `section` (enum base/extended), `is_array` (bool), `min/max/step` (number), `options` (jsonb), `placeholder` (string), `ai_key` (string), `default` (any), `validators` (jsonb), `unit` (string), `precision` (int), `sort` (int).
- formsets: `id` (uuid), `form_id` (uuid), `field_id` (uuid), `required` (bool); доп. `sort` (int), `visible_if` (jsonb).
- recipes: `id` (uuid), `action_id` (uuid), `object_id` (uuid), `label` (string), `enabled` (bool); доп. `category_id`, `subcategory_id`, `icon` (string), `color` (string), `description` (text), `form_id` (uuid), `ai_mode` (string), `ai_extract` (jsonb), `sort` (int), `user_id` (uuid).
- toggles: `id` (uuid), `user_id` (uuid), `recipe_id` (uuid), `enabled` (bool); доп. `pinned` (bool), `sort` (int).

### Кастомное (пользователь)
- extensions: `id` (uuid), `user_id` (uuid), `space_id` (uuid), `kind` (enum field/category/subcategory/pair), `data` (jsonb), `created_at` (ts); доп. `base_id` (uuid, ссылка на базовую сущность если это расширение), `enabled` (bool), `sort` (int).
  - Пример `data` для `kind=field`: `{ code, label, type, serialize, section, is_array, options, ai_key, default, validators, unit, precision }`
  - Пример `data` для `kind=category`: `{ code, label, description, icon, color, ai_hint }`
  - Пример `data` для `kind=subcategory`: `{ code, label, cat_id?, description, icon, ai_hint, action_id?, object_id? }`
  - Пример `data` для `kind=pair`: `{ object_id, action_id, category_id?, subcategory_id?, enabled }`

### Справочники для UX/AI
- tags: `id` (uuid), `user_id` (uuid), `label` (string); доп. `color` (string), `usage_count` (int), `last_used_at` (ts).
- people: `id` (uuid), `user_id` (uuid), `label` (string); доп. `avatar` (string), `contacts` (jsonb), `usage_count` (int), `last_used_at` (ts).
- places: `id` (uuid), `user_id` (uuid), `label` (string), `geo` (point/json); доп. `address` (string), `city` (string), `country` (string), `usage_count` (int), `last_used_at` (ts).
- currencies: `code` (string), `label` (string); доп. `symbol` (string), `precision` (int), `default_for_user_id` (uuid).

### AI задачи и метрики
- ai_jobs: `id` (uuid), `user_id` (uuid), `space_id` (uuid), `type` (string), `status` (enum), `payload` (jsonb), `created_at` (ts); доп. `result` (jsonb), `error` (text), `finished_at` (ts), `source_entry_id` (uuid), `source_file_id` (uuid), `model` (string).
- ai_usage: `id` (uuid), `user_id` (uuid), `space_id` (uuid), `model` (string), `tokens_prompt` (int), `tokens_completion` (int), `created_at` (ts); доп. `cost` (number), `request_id` (string), `latency_ms` (int), `error` (text).

### Напоминания и уведомления
- reminders: `id` (uuid), `user_id` (uuid), `space_id` (uuid), `due_at` (ts), `channel` (enum push/email/local), `status` (enum), `payload` (jsonb); доп. `entry_id` (uuid), `type` (enum once/recurring), `timezone` (string), `snooze_until` (ts), `created_at` (ts), `updated_at` (ts).
- notifications: `id` (uuid), `user_id` (uuid), `space_id` (uuid), `type` (string), `payload` (jsonb), `created_at` (ts); доп. `delivered_at` (ts), `read_at` (ts), `channel` (enum), `entry_id` (uuid), `reminder_id` (uuid).
- tokens: `id` (uuid), `user_id` (uuid), `token` (string), `platform` (enum web/ios/android), `created_at` (ts); доп. `device` (string), `expires_at` (ts), `revoked_at` (ts).

### Настройки
- preferences: `id` (uuid), `user_id` (uuid); доп. `default_currency` (string), `locale` (string), `timezone` (string), `ai_enabled` (bool), `ai_model` (string), `theme` (string), `quiet_hours` (jsonb), `onboarding_done_at` (ts).
- settings: ключ-значение глобальных флагов и лимитов (jsonb).

### Списки (roadmap)
- lists: `id` (uuid), `space_id` (uuid), `title` (string), `created_at` (ts); доп. `description`, `icon`, `color`, `filters` (jsonb), `sort`.
- listitems: `id` (uuid), `list_id` (uuid), `entry_id` (uuid); доп. `note` (text), `sort` (int).

### Журналы и синк
- versions: `id` (uuid), `entry_id` (uuid), `user_id` (uuid), `space_id` (uuid), `version` (int), `diff` (jsonb), `created_at` (ts); доп. `source` (string).
- syncs: `id` (uuid), `space_id` (uuid), `user_id` (uuid), `direction` (enum push/pull), `hash` (string), `created_at` (ts); доп. `items_count` (int), `status` (enum), `error` (text).
- activity: `id` (uuid), `user_id` (uuid), `space_id` (uuid), `action` (string), `resource` (string), `created_at` (ts); доп. `ip` (string), `user_agent` (string), `meta` (jsonb).

