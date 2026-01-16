<script lang="ts">
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import { PageShell } from '$lib/components/layout';
	import type { PageData } from './$types';
	import { ArrowRight, Image, Link2, MapPin, Sparkles, Tag } from 'lucide-svelte';

	let { data }: { data: PageData } = $props();
	const { entry, parentList, reminders } = data;

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

<PageShell title={entry.title} showBack>
	<svelte:fragment slot="subheader">
		<div class="flex flex-wrap items-center gap-2 text-xs text-muted-foreground px-0">
			<span class="rounded-full bg-accent px-2.5 py-1">{typeLabel}</span>
			<span class="rounded-full bg-accent px-2.5 py-1">{entry.date} · {entry.time}</span>
			{#if entry.amount}
				<span class="rounded-full bg-accent px-2.5 py-1">
					{entry.amount} {entry.currency ?? '₽'}
				</span>
			{/if}
			{#if entry.source}
				<span class="rounded-full bg-accent px-2.5 py-1">Источник: {entry.source}</span>
			{/if}
			{#if entry.confidence}
				<span class="rounded-full bg-accent px-2.5 py-1">Уверенность: {entry.confidence}</span>
			{/if}
			{#if parentList}
				<Button variant="ghost" size="sm" class="gap-1" href={`/lists/${parentList.id}`}>
					<MapPin class="size-3.5" />
					{parentList.title}
				</Button>
			{/if}
		</div>
	</svelte:fragment>
	<svelte:fragment slot="footer">
		<div class="flex flex-wrap gap-2">
			<Button variant="secondary" href="/new" class="gap-1.5">
				<Sparkles class="size-4" />
				<span>Доработать AI</span>
			</Button>
			{#if parentList}
				<Button variant="ghost" href={`/lists/${parentList.id}`} class="gap-1.5">
					<ArrowRight class="size-4" />
					<span>Открыть список</span>
				</Button>
			{/if}
			<Button variant="ghost" href="/" class="gap-1.5">
				<Link2 class="size-4" />
				<span>В ленту</span>
			</Button>
		</div>
	</svelte:fragment>
	<section class="space-y-4">
		<p class="text-sm text-muted-foreground">
			{#if entry.type === 'list'}
				AI распознал позиции, можно подтвердить или исправить.
			{:else if entry.type === 'debt'}
				Проверь сумму долга и назначь напоминание.
			{:else if entry.type === 'reminder'}
				Контекст: напоминание связано с записью или списком.
			{:else}
				Детали записи можно дописать позже, оффлайн сохранится.
			{/if}
		</p>

		{#if entry.tags?.length}
			<div class="flex flex-wrap gap-1.5">
				{#each entry.tags as tag}
					<Badge variant="outline" class="text-xs">
						<Tag class="mr-1 size-3.5" />
						{tag}
					</Badge>
				{/each}
			</div>
		{/if}

		<div class="space-y-3 rounded-2xl border border-border/80 bg-card/70 p-4">
			{#if entry.attachments}
				<div class="flex items-center gap-2 rounded-xl bg-accent px-3 py-2 text-sm">
					<Image class="size-4" />
					<span>{entry.attachments} вложения</span>
				</div>
			{/if}

			{#if reminders.length}
				<div class="rounded-xl border border-border bg-background p-3">
					<p class="text-sm font-semibold">Напоминания</p>
					<div class="mt-2 space-y-2 text-sm text-muted-foreground">
						{#each reminders as reminder}
							<div class="flex items-center justify-between gap-2">
								<span>{reminder.title}</span>
								<span class="rounded-full bg-accent px-2.5 py-1 text-xs">{reminder.due}</span>
							</div>
						{/each}
					</div>
				</div>
			{/if}
		</div>
	</section>
</PageShell>

