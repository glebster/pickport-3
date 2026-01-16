<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import { demoEntries } from '$lib/mocks/demo-data.js';
	import { Clock4 } from 'lucide-svelte';

	const timeline = demoEntries
		.map((e) => ({ ...e }))
		.sort((a, b) => (a.date > b.date ? -1 : 1));
</script>

<PageShell title="Линия жизни">
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<Clock4 class="size-4" />
			<span>Ключевые события по времени (мок)</span>
		</div>
	</svelte:fragment>
	<div class="relative space-y-4">
		{#each timeline as item}
			<div class="relative flex gap-3">
				<div class="flex flex-col items-center">
					<div class="size-3 rounded-full bg-emerald-500" />
					<div class="h-full w-px bg-border" />
				</div>
				<div class="rounded-2xl border border-border/80 bg-card/70 px-3 py-2">
					<p class="text-xs text-muted-foreground">{item.date} · {item.time}</p>
					<p class="text-sm font-semibold">{item.title}</p>
					<p class="text-xs text-muted-foreground">{item.summary}</p>
				</div>
			</div>
		{/each}
	</div>
</PageShell>

