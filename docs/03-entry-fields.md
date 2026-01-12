# 03 — Поля записей

## Уровни важности

### 1) Обязательные
Минимум, без которого событие теряет смысл.

- `title`
- `date`
- в финансах: `amount`
- в долгах: `person`
- в некоторых сценариях: `placeText` (если событие связано с конкретным местом)

Запись не сохраняется, если обязательные поля пусты.
`title` может быть сформирован автоматически (из `action + object` и ключевых слов), но пользователь должен иметь возможность быстро поправить его перед сохранением.
`date` по умолчанию ставится текущая, но в сценариях «в прошлом/в будущем» пользователь может выбрать точную или приблизительную дату.

### 2) Основные (рекомендуемые)
Обычно ожидаются для конкретной категории.

Примеры: `amount`, `currency`, `placeText`, `category`, `rating`, `mood`, `quantity`.

ИИ стремится заполнить их автоматически.

### 3) Дополнительные
Дают глубину и контекст.

Примеры: `note`, `tags`, `attachments`, `geo`, `duration`, `calories`, `emotions`.

## Универсальные поля

- `title`
- `date`
- `tags`
- `note`
- `attachments`

Эти поля доступны почти в каждой категории и сохраняют общий язык карточек.
Рецепты могут добавлять свои специализированные поля без изменения кода.

## Контекстные поля

**Люди и место:**
- `people[]`
- `placeText`
- `geo`

**Финансы:**
- `amount`
- `currency`
- `merchant`

**Качество и настроение:**
- `rating`
- `mood`

**Повторы и напоминания:**
- `reminder`
- `recurrence` (future)

**Списки и вложения:**
- `listId` (если запись связана со списком, например с чеком)
- `attachments` (сканы, фото, документы, треки)

Контекстные поля доступны во всех категориях, но реально отображаются и заполняются только если подходят сценарию.

## Типы полей (FieldId → Type)

Таблица фиксирует ожидаемый `type` для каждого `FieldId` и служит опорой для UI‑рендера и валидаторов.

| FieldId       | Label          | Type                               |
| ------------- | -------------- | ---------------------------------- |
| title         | Название       | text                               |
| date          | Дата           | date                               |
| tags          | Теги           | tags                               |
| note          | Описание       | textarea                           |
| attachments   | Вложения       | json                               |
| amount        | Сумма          | money                              |
| currency      | Валюта         | select                             |
| category      | Категория      | text                               |
| subcategory   | Подкатегория   | text                               |
| people        | Люди           | people                             |
| placeText     | Место          | text                               |
| address       | Адрес          | text                               |
| city          | Город          | text                               |
| geo           | Координаты     | geo                                |
| items         | —              | **❗ нет определения в FIELD_DEFS** |
| rating        | Оценка         | number                             |
| quantity      | Количество     | number                             |
| unit          | Единицы        | text                               |
| url           | Ссылка         | url                                |
| recurrence    | Повторяемость  | text                               |
| distance      | Дистанция      | number                             |
| calories      | Калории        | number                             |
| duration      | Длительность   | number                             |
| startTime     | Начало         | time                               |
| endTime       | Окончание      | time                               |
| country       | Страна         | text                               |
| region        | Регион         | text                               |
| zip           | Индекс         | text                               |
| street        | Улица          | text                               |
| building      | Дом            | text                               |
| apartment     | Квартира       | text                               |
| merchant      | Мерчант        | text                               |
| store         | Магазин        | text                               |
| cardLast4     | Карта (посл.4) | text                               |
| iban          | IBAN           | text                               |
| account       | Счёт           | text                               |
| invoice       | Счёт/инвойс    | text                               |
| billId        | Счёт/чек ID    | text                               |
| phone         | Телефон        | text                               |
| email         | Email          | text                               |
| website       | Сайт           | url                                |
| receiptNumber | Номер чека     | text                               |
| orderId       | ID заказа      | text                               |
| table         | Стол           | text                               |
| seat          | Место          | text                               |
| mood          | Настроение     | text                               |
| weather       | Погода         | text                               |
| temperature   | Температура    | number                             |
| participants  | Участники      | text                               |
| device        | Устройство     | text                               |
| project       | Проект         | text                               |
| context       | Контекст       | text                               |
| jsonField     | —              | **❗ нет определения в FIELD_DEFS** |
| time          | Время          | time                               |
| numberField   | Числовое поле  | number                             |
| selectField   | —              | **❗ нет определения в FIELD_DEFS** |

## Правила работы с полями

1. Пользователь может **удалить любое предложенное поле**.
2. Поля добавляются **динамически**, на основе рецепта.
3. Пустые поля не хранятся (чтобы не плодить шум).
4. Поля можно **сворачивать/разворачивать**, чтобы не перегружать карточку (mobile‑first).
