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

- `action`
- `object`
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

| FieldId       | Label          | Type     |
| ------------- | -------------- | -------- |
| title         | Название       | text     |
| date          | Дата           | date     |
| tags          | Теги           | tags     |
| note          | Описание       | textarea |
| attachments   | Вложения       | json     |
| amount        | Сумма          | money    |
| currency      | Валюта         | select   |
| category      | Категория      | text     |
| subcategory   | Подкатегория   | text     |
| action        | Действие       | text     |
| people        | Люди           | people   |
| person        | Персона        | text     |
| place         | Локация        | text     |
| placeText     | Место          | text     |
| address       | Адрес          | text     |
| city          | Город          | text     |
| country       | Страна         | text     |
| geo           | Координаты     | geo      |
| rating        | Оценка         | number   |
| quantity      | Количество     | number   |
| unit          | Единицы        | text     |
| url           | Ссылка         | url      |
| link          | Ссылка         | url      |
| object        | Объект         | text     |
| recurrence    | Повторяемость  | text     |
| reminder      | Напоминание    | text     |
| billingCycle  | Биллинг‑цикл   | text     |
| interval      | Интервал       | text     |
| distance      | Дистанция      | number   |
| calories      | Калории        | number   |
| duration      | Длительность   | number   |
| tripDate      | Дата поездки   | date     |
| targetDate    | Целевая дата   | date     |
| validUntil    | Действует до   | date     |
| startTime     | Начало         | time     |
| endTime       | Окончание      | time     |
| time          | Время          | time     |
| region        | Регион         | text     |
| zip           | Индекс         | text     |
| street        | Улица          | text     |
| building      | Дом            | text     |
| apartment     | Квартира       | text     |
| merchant      | Мерчант        | text     |
| store         | Магазин        | text     |
| cardLast4     | Карта (посл.4) | text     |
| iban          | IBAN           | text     |
| account       | Счёт           | text     |
| invoice       | Счёт/инвойс    | text     |
| billId        | Счёт/чек ID    | text     |
| receiptNumber | Номер чека     | text     |
| orderId       | ID заказа      | text     |
| phone         | Телефон        | text     |
| email         | Email          | text     |
| website       | Сайт           | url      |
| table         | Стол           | text     |
| seat          | Место          | text     |
| mood          | Настроение     | text     |
| weather       | Погода         | text     |
| temperature   | Температура    | number   |
| emotions      | Эмоции         | text     |
| participants  | Участники      | text     |
| project       | Проект         | text     |
| decisions     | Решения        | text     |
| intent        | Намерение      | text     |
| priority      | Приоритет      | text     |
| summary       | Конспект       | text     |
| source        | Источник       | text     |
| metrics       | Метрики        | json     |
| listId        | ID списка      | text     |
| list          | Список         | text     |
| group         | Группа         | text     |
| device        | Устройство     | text     |
| context       | Контекст       | text     |
| docType       | Тип документа  | text     |
| medicine      | Лекарство      | text     |
| dosage        | Дозировка      | text     |
| schedule      | Расписание     | text     |
| pet           | Питомец        | text     |
| procedure     | Процедура      | text     |
| service       | Сервис         | text     |
| serviceType   | Тип сервиса    | text     |
| mileage       | Пробег         | number   |
| goalAmount    | Целевая сумма  | money    |
| currentAmount | Текущая сумма  | money    |
| jsonField     | Тех. JSON      | json     |
| numberField   | Числовое поле  | number   |

## Правила работы с полями

1. Пользователь может **удалить любое предложенное поле**.
2. Поля добавляются **динамически**, на основе рецепта.
3. При добавлении дополнительных полей UI предлагает **релевантные группы** (финансы, люди/место, планы, здоровье и т.д.), чтобы ИИ мог быстро подставить подходящий набор, а не россыпь одиночных полей.
4. Пустые поля не хранятся (чтобы не плодить шум).
5. Поля можно **сворачивать/разворачивать**, чтобы не перегружать карточку (mobile‑first).
