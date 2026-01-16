<script lang="ts">
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import type { ListMock } from '$lib/mocks/demo-data';
	import { cn } from '$lib/utils.js';
	import { ArrowRight, Layers } from 'lucide-svelte';

	let { list, href }: { list: ListMock; href?: string } = $props();
</script>

<article class="rounded-2xl border border-border/80 bg-card/70 p-4">
	<div class="flex items-start justify-between gap-3">
		<div class="space-y-1">
			<p class="text-xs uppercase text-muted-foreground">List · {list.source}</p>
			<h2 class="text-base font-semibold leading-tight">{list.title}</h2>
			<p class="text-sm text-muted-foreground">{list.summary}</p>
			<div class="flex flex-wrap gap-1.5">
				{#if list.tags}
					{#each list.tags as tag}
						<Badge variant="outline" class="text-xs">{tag}</Badge>
					{/each}
				{/if}
				<Badge variant="secondary" class="text-xs">
					<Layers class="mr-1 size-3.5" />
					{list.entriesCount} записей
				</Badge>
			</div>
		</div>
		<div class="text-right">
			{#if list.total}
				<p class="text-lg font-semibold">
					{list.total} {list.currency ?? '₽'}
				</p>
			{/if}
			<p class="text-sm text-muted-foreground">{list.date}</p>
			<Badge
				variant={list.status === 'ready' ? 'secondary' : 'outline'}
				class={cn('mt-1 text-xs', list.status === 'draft' ? 'border-dashed' : '', list.status === 'synced' ? 'bg-emerald-100 text-emerald-800' : '')}
			>
				{list.status === 'draft' ? 'Черновик' : list.status === 'ready' ? 'Готово' : 'Синхронизировано'}
			</Badge>
		</div>
	</div>
	<div class="mt-3 flex items-center justify-between">
		<div class="flex gap-2 text-xs text-muted-foreground">
			<span class="rounded-full bg-accent px-2.5 py-1">
				Уверенность: {list.confidence}
			</span>
			<span class="rounded-full bg-accent px-2.5 py-1">{list.source}</span>
		</div>
		{#if href}
			<Button variant="ghost" size="sm" class="gap-1.5" href={href}>
				<span>Открыть</span>
				<ArrowRight class="size-4" />
			</Button>
		{/if}
	</div>
</article>

