<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import { demoLists } from '$lib/mocks/demo-data.js';
	import { Settings2 } from 'lucide-svelte';

	const categories = ['еда', 'долги', 'путешествие', 'здоровье', 'заметки'];
</script>

<PageShell title="Предпочтения">
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<Settings2 class="size-4" />
			<span>Категории, рецепты, поля для авто‑распознавания</span>
		</div>
	</svelte:fragment>
	<section class="space-y-4">
		<div class="rounded-2xl border border-border bg-card/70 p-4">
			<p class="text-sm font-semibold">Категории по умолчанию</p>
			<div class="mt-2 flex flex-wrap gap-2">
				{#each categories as cat}
					<Badge variant="outline" class="text-xs">{cat}</Badge>
				{/each}
			</div>
		</div>

		<div class="rounded-2xl border border-border bg-card/70 p-4">
			<p class="text-sm font-semibold">Шаблоны списков</p>
			<div class="mt-2 space-y-2">
				{#each demoLists as list}
					<div class="flex items-center justify-between rounded-xl border border-border/70 px-3 py-2">
						<div>
							<p class="text-sm font-medium">{list.title}</p>
							<p class="text-xs text-muted-foreground">{list.summary}</p>
						</div>
						<Button variant="ghost" size="sm">Отключить</Button>
					</div>
				{/each}
			</div>
		</div>
	</section>
</PageShell>

