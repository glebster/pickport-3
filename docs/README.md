# PickPock — продуктовая документация

Эта папка — рабочая документация по продукту PickPock. Здесь собраны ключевые идеи, модель данных, UX‑потоки, архитектурные решения и зоны риска.

## Навигация

1. **[00-overview.md](00-overview.md)** — назначение продукта, ценность и позиционирование.
2. **[01-semantic-core.md](01-semantic-core.md)** — семантическое ядро (Action + Object + Context).
3. **[02-categories-recipes.md](02-categories-recipes.md)** — категории, рецепты и намерения.
4. **[03-entry-fields.md](03-entry-fields.md)** — поля записей и правила заполнения.
5. **[04-ux-flows.md](04-ux-flows.md)** — ключевые UX‑потоки добавления и подтверждения.
6. **[05-ui-routes.md](05-ui-routes.md)** — экраны, маршруты и навигация.
7. **[06-architecture.md](06-architecture.md)** — общая архитектура FastAPI + Svelte 5 + PWA.
8. **[07-ai-search-reminders.md](07-ai-search-reminders.md)** — роль ИИ, поиск и напоминания.
9. **[08-mvp-roadmap.md](08-mvp-roadmap.md)** — MVP и развитие.
10. **[09-risks-open-questions.md](09-risks-open-questions.md)** — узкие места и открытые вопросы.
11. **[10-best-practices.md](10-best-practices.md)** — best practices для mobile‑first PWA.
12. **[11-screens.md](11-screens.md)** — обзор экранов по скриншотам.
13. **[12-security.md](12-security.md)** — безопасность и приватность.
14. **[13-monetization.md](13-monetization.md)** — монетизация.
15. **[14-entities.md](14-entities.md)** — основные сущности простыми словами.
16. **[15-use-cases.md](15-use-cases.md)** — подробные сценарии использования.
17. **[17-new-wizard-tz.md](17-new-wizard-tz.md)** — ТЗ на экран `/new` (2‑этапный визард).
18. **[18-storage-model.md](18-storage-model.md)** — модель хранения: локальная база и облачный контур.

## Принципы оформления

- Все документы описывают продукт «языком пользователя» и остаются актуальными при изменениях дизайна.
- Семантическое ядро считается стабильным и меняется редко.
- Вся архитектура строится вокруг событий, а не таблиц, заметок или задач.
