<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import { demoEntries, demoLists } from '$lib/mocks/demo-data.js';
	import { BarChart2, ListChecks } from 'lucide-svelte';

	const total = demoEntries.reduce((acc, e) => acc + (e.amount ?? 0), 0);
</script>

<PageShell title="Сводка (мок)">
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<BarChart2 class="size-4" />
			<span>Быстрые цифры по демо-данным</span>
		</div>
	</svelte:fragment>
	<section class="space-y-3">
		<div class="rounded-2xl border border-border bg-card/70 p-4">
			<p class="text-sm text-muted-foreground">Всего сумм: {total} ₽</p>
			<p class="text-sm text-muted-foreground">Записей: {demoEntries.length}</p>
			<p class="text-sm text-muted-foreground">Списков: {demoLists.length}</p>
		</div>

		<div class="rounded-2xl border border-border bg-card/70 p-4">
			<div class="flex items-center gap-2">
				<ListChecks class="size-4 text-emerald-500" />
				<p class="text-sm font-semibold">Демо-аналитика</p>
			</div>
			<p class="text-sm text-muted-foreground mt-1">
				Тут будет чарт/таблицы после подключения реальных данных.
			</p>
		</div>
	</section>
</PageShell>

