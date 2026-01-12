# Архитектура Recipes (кубики)

## Принцип

**Семантическое ядро (Action + Object) — в коде, immutable**  
**Recipes (кубики) — в конфиге, легко расширяемые**

> **Кубик = рецепт создания записи**, который фиксирует `action + object`, задаёт лейбл/иконку, форму и AI режим.  
> Кубики НЕ меняют семантическое ядро. Они только управляют UX.

## Два слоя кубиков

### A) Базовые (default)

- Лежат в `src/lib/config/recipes.default.json` (единственный источник)
- Нельзя удалить, но можно **toggle ON/OFF**
- Примеры: "Расход", "Был в месте", "Хочу сходить"

### B) Пользовательские (custom)

- Хранятся в БД (`user_recipes`)
- Можно создавать/редактировать/удалять
- Можно **toggle ON/OFF**

---

## Структура

### 1. Ядро (`src/lib/core/semantic.ts`)

```typescript
// Это КОД, не конфиг
export type Action = 'noted' | 'visited' | 'planned' | 'spent' | ...
export type Object = 'money' | 'place' | 'food' | 'item' | ...
```

**Правила:**

- Один entry = один action
- Action/Object только из enum
- Всё остальное в context
- Fallback: `noted + note`

### 2. Recipes (`src/lib/config/recipes.ts`)

```typescript
export interface Recipe {
  id: string;
  action: Action;      // из ядра
  object: Object;      // из ядра
  label: string;       // для UI
  form: RecipeForm;    // какие поля показывать
  ai?: RecipeAI;       // как AI должен работать
  category?: string;   // для группировки
}
```

**Это КОНФИГ** — легко добавлять новые recipes без изменения кода.

## Как добавить новый Recipe

### Пример: Добавить "Потратил на услугу"

```typescript
// В src/lib/config/recipes.ts
{
  id: 'service_spent',
  action: 'spent',        // из ядра
  object: 'service',      // из ядра
  label: 'Потратил на услугу',
  icon: 'Wrench',
  category: 'money',
  form: {
    fields: ['title', 'amount', 'currency', 'category', 'date', 'placeText', 'tags'],
    required: ['title', 'amount', 'date']
  },
  ai: {
    mode: 'receipt',
    extract: ['title', 'amount', 'currency', 'category', 'date', 'placeText']
  }
}
```

**Всё!** Никаких изменений в коде не требуется.

## Использование в приложении

### 1. Выбор Recipe в UI

```typescript
import { getAllRecipes, getRecipesByCategory } from '$lib/config/recipes';

// Показать все recipes
const recipes = getAllRecipes();

// Показать recipes по категории
const moneyRecipes = getRecipesByCategory('money');
```

### 2. Создание Entry из Recipe

```typescript
import { getRecipeById } from '$lib/config/recipes';

const recipe = getRecipeById('money_spent');
// recipe.action = 'spent'
// recipe.object = 'money'

const entry: Entry = {
  action: recipe.action,
  object: recipe.object,
  title: 'Кофе',
  amount: 250,
  // ... остальные поля
};
```

### 3. Генерация формы из Recipe

```typescript
const recipe = getRecipeById('money_spent');

// recipe.form.fields = ['title', 'amount', 'currency', ...]
// recipe.form.required = ['title', 'amount', 'date']

// Генерируем форму динамически
recipe.form.fields.forEach(field => {
  // Показать поле
  // Проверить required
});
```

### 4. AI обработка по Recipe

```typescript
const recipe = getRecipeById('money_spent');

if (recipe.ai) {
  // recipe.ai.mode = 'receipt'
  // recipe.ai.extract = ['title', 'amount', ...]
  // recipe.ai.promptTemplate = '...'

  // Использовать для AI запроса
}
```

## Ограничения для пользовательских кубиков

Пользовательский кубик собирается только из разрешённых деталей:

- Выбирает `action` из enum
- Выбирает `object` из enum
- Выбирает поля формы из белого списка

**Запрещаем:**

- Добавлять новые action/object в MVP
- Менять логику аналитики
- Создавать "сложные правила"

---

## Преимущества

1. **Стабильность ядра**: Action/Object не меняются
2. **Гибкость UI**: Новые recipes без изменения кода
3. **Управляемый AI**: Каждый recipe знает как работать с AI
4. **Расширяемость**: Добавить новый recipe = добавить объект в массив
5. **Настраиваемость**: Пользователь настраивает приложение под себя без "редактора данных"

## Миграция с EntryType

Для обратной совместимости:

```typescript
import { entryTypeToSemantic, semanticToEntryType } from '$lib/core/migration';

// Старый EntryType -> Action + Object
const { action, object } = entryTypeToSemantic('money.expense');

// Action + Object -> EntryType (для миграции)
const type = semanticToEntryType('spent', 'money');
```

## Структура данных Entry

```typescript
interface Entry {
  // Семантическое ядро (primary)
  action: Action;
  object: Object;

  // Legacy (для миграции)
  type?: EntryType;

  // Context (динамический)
  title: string;
  amount?: number;
  // ... остальные поля
}
```

## Категории Recipes

Recipes группируются по категориям для UI:

### Основные категории (10)

1. **Деньги** (`money`) — денежные операции
2. **Вещи** (`items`) — покупки, подарки, обмен
3. **Места** (`places`) — посещения, путешествия
4. **Еда** (`food`) — прием пищи, покупки еды
5. **Услуги** (`services`) — оплата, подписки
6. **Желания** (`wishes`) — планы и цели
7. **Заметки** (`notes`) — общие записи
8. **Опыт** (`experience`) — впечатления, переживания
9. **Спорт** (`sport`) — тренировки, соревнования
10. **Хобби** (`hobby`) — увлечения и творчество

### Подкатегории

Подкатегории (`subcategory`) используются для внутренней группировки рецептов внутри категории, но **не отображаются отдельно в UI**.

В UI выводятся:

- **Категории** — с иконкой и названием (через `getCategoryLabel()` и `getCategoryIcon()`)
- **Рецепты** — внутри каждой категории, отсортированные по `sortOrder` из JSON

### Что выводится в UI

1. **Категории** — группируют рецепты, отображаются с иконкой и названием
2. **Рецепты** — внутри категорий, каждый со своим `label`, `icon`, `description`
3. **Сортировка** — по `sortOrder` из JSON (без hardcoded порядка)

Все данные (label, icon, description, sortOrder) берутся из `recipes.default.json` — нет дублирования в коде.

Используйте `getRecipesByCategory()` для фильтрации по категориям.
