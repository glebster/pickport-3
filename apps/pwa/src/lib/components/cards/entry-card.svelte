<script lang="ts">
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import type { EntryMock } from '$lib/mocks/demo-data';
	import { cn } from '$lib/utils.js';
	import { Image, Link2 } from 'lucide-svelte';

	let {
		entry,
		href,
		actionLabel = 'Открыть'
	}: {
		entry: EntryMock;
		href?: string;
		actionLabel?: string;
	} = $props();

	const typeLabel =
		entry.type === 'list'
			? 'Список/чек'
			: entry.type === 'debt'
				? 'Долг'
				: entry.type === 'reminder'
					? 'Напоминание'
					: entry.type === 'visit'
						? 'Посещение'
						: 'Заметка';
</script>

<article class="rounded-2xl border border-border/80 bg-card/70 p-4">
	<div class="flex items-start justify-between gap-2">
		<div class="space-y-1">
			<p class="text-xs uppercase text-muted-foreground">{typeLabel}</p>
			<h2 class="text-base font-semibold leading-tight">{entry.title}</h2>
			<p class="text-sm text-muted-foreground">{entry.summary}</p>
			<div class="flex flex-wrap gap-1.5">
				{#if entry.categoryLabel ?? entry.category}
					<Badge variant="secondary" class="text-xs">{entry.categoryLabel ?? entry.category}</Badge>
				{/if}
				{#if entry.subcategoryLabel ?? entry.subcategory}
					<Badge variant="outline" class="text-xs">{entry.subcategoryLabel ?? entry.subcategory}</Badge>
				{/if}
				{#if entry.tags}
					{#each entry.tags as tag}
						<Badge variant="outline" class="text-xs">{tag}</Badge>
					{/each}
				{/if}
				{#if entry.listId}
					<Badge variant="secondary" class="text-xs">list {entry.listId}</Badge>
				{/if}
			</div>
		</div>
		<div class="flex flex-col items-end gap-2 text-right">
			<Badge
				variant={entry.status === 'ready' ? 'secondary' : 'outline'}
				class={cn('text-xs', entry.status === 'draft' ? 'border-dashed' : '', entry.status === 'synced' ? 'bg-emerald-100 text-emerald-800' : '')}
			>
				{entry.status === 'draft' ? 'AI черновик' : entry.status === 'ready' ? 'Готово' : 'Синхронизировано'}
			</Badge>
			<p class="text-sm text-muted-foreground">{entry.date} · {entry.time}</p>
			{#if entry.amount}
				<p class="text-lg font-semibold">
					{entry.amount} {entry.currency ?? '₽'}
				</p>
			{/if}
		</div>
	</div>
	<div class="mt-3 flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
		<span class="rounded-full bg-accent px-2.5 py-1">
			Источник: {entry.source ?? 'text'}
		</span>
		{#if entry.confidence}
			<span class="rounded-full bg-accent px-2.5 py-1">
				Уверенность: {entry.confidence}
			</span>
		{/if}
		{#if entry.attachments}
			<span class="flex items-center gap-1 rounded-full bg-accent px-2.5 py-1">
				<Image class="size-3.5" />
				{entry.attachments} вложения
			</span>
		{/if}
		{#if href}
			<Button variant="ghost" size="sm" class="ml-auto gap-1" href={href}>
				<Link2 class="size-3.5" />
				{actionLabel}
			</Button>
		{/if}
	</div>
</article>

