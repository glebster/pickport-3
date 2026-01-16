<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import { demoEntries } from '$lib/mocks/demo-data.js';
	import { cn } from '$lib/utils.js';
	import { Filter, Link2, ListFilter } from 'lucide-svelte';

	const kinds = ['Все', 'AI черновик', 'Долги', 'Напоминания', 'Чеки'] as const;
	let active = $state<(typeof kinds)[number]>('Все');

	function filtered() {
		if (active === 'Все') return demoEntries;
		if (active === 'AI черновик') return demoEntries.filter((e) => e.status === 'draft');
		if (active === 'Долги') return demoEntries.filter((e) => e.type === 'debt');
		if (active === 'Напоминания') return demoEntries.filter((e) => e.type === 'reminder');
		if (active === 'Чеки') return demoEntries.filter((e) => e.type === 'list');
		return demoEntries;
	}
</script>

<PageShell title="Все записи">
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<ListFilter class="size-4" />
			<span>{demoEntries.length} записей · фильтр {active}</span>
		</div>
	</svelte:fragment>
	<section class="space-y-4">
		<div class="flex gap-2 overflow-x-auto pb-1">
			{#each kinds as kind}
				<button
					class={cn(
						'rounded-full border px-4 py-2 text-sm font-medium transition-colors',
						active === kind ? 'bg-emerald-500 text-white border-emerald-500' : 'border-border bg-background hover:bg-accent'
					)}
					type="button"
					onclick={() => (active = kind)}
				>
					{kind}
				</button>
			{/each}
		</div>

		<div class="space-y-3">
			{#each filtered() as entry}
				<div class="rounded-2xl border border-border/80 bg-card/70 p-4">
					<div class="flex items-start justify-between gap-2">
						<div>
							<p class="text-xs uppercase text-muted-foreground">
								{entry.type === 'list'
									? 'Список/чек'
									: entry.type === 'debt'
										? 'Долг'
										: entry.type === 'reminder'
											? 'Напоминание'
											: entry.type === 'visit'
												? 'Посещение'
												: 'Заметка'}
							</p>
							<h2 class="text-base font-semibold leading-tight">{entry.title}</h2>
							<p class="text-sm text-muted-foreground">{entry.summary}</p>
							<div class="mt-1 flex flex-wrap gap-1.5">
								{#if entry.categoryLabel ?? entry.category}
									<Badge variant="secondary" class="text-xs">{entry.categoryLabel ?? entry.category}</Badge>
								{/if}
								{#if entry.subcategoryLabel ?? entry.subcategory}
									<Badge variant="outline" class="text-xs">{entry.subcategoryLabel ?? entry.subcategory}</Badge>
								{/if}
							</div>
						</div>
						<Badge variant={entry.status === 'ready' ? 'secondary' : 'outline'} class={entry.status === 'draft' ? 'border-dashed' : ''}>
							{entry.status === 'draft' ? 'AI черновик' : entry.status === 'ready' ? 'Готово' : 'Синхронизировано'}
						</Badge>
					</div>
					<div class="mt-2 flex items-center gap-2 text-xs text-muted-foreground">
						<span class="rounded-full bg-accent px-2.5 py-1">{entry.date} · {entry.time}</span>
						{#if entry.amount}
							<span class="rounded-full bg-accent px-2.5 py-1">
								{entry.amount} {entry.currency ?? '₽'}
							</span>
						{/if}
						<Button variant="ghost" size="sm" class="ml-auto gap-1" href={`/entries/${entry.id}`}>
							<Link2 class="size-3.5" />
							Открыть
						</Button>
					</div>
				</div>
			{/each}
		</div>
	</section>
</PageShell>

