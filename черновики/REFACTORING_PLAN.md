# План рефакторинга компонентов

## Созданные компоненты dashboard

### Базовые компоненты
1. **PeriodSummary** - Итог периода (темная карточка)
2. **IncomeExpenseCard** - Карточка дохода/расхода
3. **KeyMetric** - Ключевой показатель (иконка + бейдж)
4. **QuickSection** - Быстрый раздел (иконка + текст)
5. **QuickSections** - Контейнер быстрых разделов (со слотом)
6. **CategoryStatItem** - Элемент статистики категории
7. **CategoryStats** - Контейнер статистики категорий (со слотом)
8. **TopCategoryItem** - Элемент топа категорий
9. **TopCategories** - Контейнер топа категорий (со слотом)
10. **RecentPlaceItem** - Элемент последнего места
11. **RecentPlaces** - Контейнер последних мест (со слотом)
12. **SectionHeader** - Заголовок секции с кнопкой действия

### Утилитарные компоненты
13. **EmptyState** - Пустое состояние (иконка + заголовок + описание + кнопка)
14. **LoadingState** - Состояние загрузки (скелетоны)
15. **MetricGrid** - Сетка метрик (2/3/4 колонки)

## Где заменить

### src/routes/+page.svelte (Главная страница)

#### ✅ Заменить:
1. **PeriodSummary** (строки 335-348)
   - Заменить Card на PeriodSummary
   
2. **IncomeExpenseCard** (строки 352-377)
   - Заменить 2 Card на IncomeExpenseCard
   
3. **KeyMetric** (строки 380-441)
   - Заменить 6 button на KeyMetric
   - Использовать MetricGrid для обертки
   
4. **QuickSections + QuickSection** (строки 443-495)
   - Заменить весь блок на QuickSections с QuickSection внутри
   
5. **SectionHeader** (строки 500-510)
   - Заменить заголовок на SectionHeader
   
6. **EmptyState** (строки 527-544)
   - Заменить Empty на EmptyState
   
7. **CategoryStats + CategoryStatItem** (строки 554-588)
   - Заменить Card на CategoryStats
   - Использовать CategoryStatItem для элементов
   
8. **TopCategories + TopCategoryItem** (строки 590-613)
   - Заменить Card на TopCategories
   - Использовать TopCategoryItem для элементов
   
9. **RecentPlaces + RecentPlaceItem** (строки 615-640)
   - Заменить Card на RecentPlaces
   - Использовать RecentPlaceItem для элементов
   
10. **LoadingState** (строки 322-326)
    - Заменить скелетоны на LoadingState

### src/routes/entries/+page.svelte

#### ✅ Заменить:
1. **EmptyState** - для пустого состояния записей
2. **LoadingState** - для состояния загрузки

### Другие страницы

#### src/routes/settings/+page.svelte
- Можно использовать EmptyState если есть пустые состояния

## Преимущества

1. ✅ Единый стиль всех блоков
2. ✅ Легче поддерживать и изменять
3. ✅ Переиспользуемость компонентов
4. ✅ Чистый код без дублирования
5. ✅ Соответствие Svelte 5
6. ✅ Без использования Card компонентов (как требовалось)

## Следующие шаги

1. Заменить все блоки на главной странице
2. Протестировать все компоненты
3. Убедиться что все работает корректно
4. Удалить неиспользуемые импорты Card

