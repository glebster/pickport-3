# Лог сессий

## 2026-01-14
- Согласовали структуру монорепо: `apps/pwa`, `apps/backend`, `config`, `db`, `docker`, `docs`.
- Сгенерирован SvelteKit + Tailwind проект в `apps/pwa`.
- Добавлен AI-скелет (`apps/backend/app/ai/provider.py`).
- Добавлен `AGENTS.md` с правилами (mobile-first, shadcn без Card, emerald как бренд, PLAN/LOG).
- Созданы и переименованы рабочие файлы `PLAN.md` и `LOG.md`.
- Настроен базовый теминг shadcn (переменные в `src/routes/layout.css`, вернули дефолт палитру).
- Проверен `manifest.json` и наличие иконок/лого в `static`.
- Добавлен `components.json`, утилита `cn` (`src/lib/utils.ts`), установлены `clsx` и `tailwind-merge`.
- Подключён shadcn-svelte CLI и добавлены компоненты (без Card, без combobox/date-picker/formsnap/typography). Установлен `lucide-svelte`. Папка `ui` пересоздана и наполнена полным набором: accordion, alert-dialog, alert, aspect-ratio, avatar, badge, breadcrumb, button-group, button, calendar, carousel, chart, checkbox, collapsible, command, context-menu, data-table, dialog, drawer, dropdown-menu, empty, field, hover-card, input-group, input-otp, input, item, kbd, label, menubar, native-select, navigation-menu, pagination, popover, progress, radio-group, range-calendar, resizable, scroll-area, select, separator, sheet, sidebar, skeleton, slider, sonner, spinner, switch, table, tabs, textarea, toggle-group, toggle, tooltip; добавлен hook `is-mobile`.
- Мокапы роутов `/`, `/lists`, `/new` с демо-данными (лента, списки, визард 2 шага); брендовый emerald опционально через `.brand-emerald` в `layout.css`.
- Добавлены детальные мок-роуты `/entries/[id]`, `/lists/[id]` с подстановкой демо-данных; линковка из ленты и списков.
- Создан универсальный каркас страницы `PageShell` (`src/lib/components/layout/page-shell.svelte`) для внутренних экранов: шапка/сабхедер, скролл-контент, нижние блоки, авто‑скролл для чата.
- Все маршруты из `docs/05-ui-routes.md` созданы как мок-страницы на базе `PageShell` (enter/entries/search/bot/reminders/settings/preferences/planner/groups/dashboard/lifeline и т.д.).
- Добавлены карточки `EntryCard/ListCard/ReminderCard` в `lib/components/cards`, обновлены демо-данные (в списке grocery >=2 entries).
- Исправлены SSR-ошибки (`PageShell` без mix slot/{@render}, добавлен import), проброс tailwind var через `@theme`.
- Демо-данные синхронизированы с `docs/02-categories-recipes.md`: категории в нижнем регистре (en), подкатегории — глагольные slug, лейблы по-русски.

