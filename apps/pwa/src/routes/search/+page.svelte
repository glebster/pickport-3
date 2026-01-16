<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import { demoEntries } from '$lib/mocks/demo-data.js';
	import { Search, Wand2 } from 'lucide-svelte';

	let query = $state('');
	const hints = ['паста в пятницу', 'чек перекресток', 'напомни стоматолог', 'долги за ужин'];
</script>

<PageShell title="Поиск" autoScroll={false}>
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<Wand2 class="size-4" />
			<span>Ищем по локальным данным; AI подсказки после запроса</span>
		</div>
	</svelte:fragment>
	<section class="space-y-4">
		<label class="flex items-center gap-2 rounded-xl border border-border bg-background px-3 py-2">
			<Search class="size-4 text-muted-foreground" />
			<input
				class="w-full bg-transparent text-sm focus:outline-none"
				placeholder="Что ищем? (событие, сумма, место)"
				bind:value={query}
			/>
		</label>

		<div class="flex flex-wrap gap-2 text-xs">
			{#each hints as hint}
				<button class="rounded-full border border-border px-3 py-1 hover:bg-accent" type="button" onclick={() => (query = hint)}>
					{hint}
				</button>
			{/each}
		</div>

		{#if query}
			<div class="space-y-2">
				<p class="text-sm text-muted-foreground">Результаты по «{query}»</p>
				{#each demoEntries.filter((e) => e.title.toLowerCase().includes(query.toLowerCase())) as entry (entry.id)}
					<div class="rounded-xl border border-border/80 bg-card/70 px-3 py-2">
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm font-semibold">{entry.title}</p>
								<p class="text-xs text-muted-foreground">{entry.summary}</p>
							</div>
							<Badge variant={entry.status === 'ready' ? 'secondary' : 'outline'} class={entry.status === 'draft' ? 'border-dashed' : ''}>
								{entry.status}
							</Badge>
						</div>
					</div>
				{/each}
			</div>
		{:else}
			<p class="text-sm text-muted-foreground">Введите запрос или выберите подсказку.</p>
		{/if}
	</section>
</PageShell>

