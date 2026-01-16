<script lang="ts">
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import { PageShell } from '$lib/components/layout';
	import { demoEntries, demoReminders, heroState } from '$lib/mocks/demo-data.js';
	import { cn } from '$lib/utils.js';
	import {
		Bell,
		FileText,
		Image,
		Link2,
		Sparkles,
		Wand2,
		WifiOff
	} from 'lucide-svelte';

	const filters = ['Все', 'AI черновик', 'Долги', 'Напоминания'] as const;
	let activeFilter = $state<(typeof filters)[number]>('Все');

	const moodEmoji = {
		positive: '🙂',
		neutral: '😐',
		negative: '🙁'
	} satisfies Record<string, string>;

	function getFilteredEntries() {
		if (activeFilter === 'Все') return demoEntries;
		if (activeFilter === 'AI черновик') return demoEntries.filter((e) => e.status === 'draft');
		if (activeFilter === 'Долги') return demoEntries.filter((e) => e.type === 'debt');
		if (activeFilter === 'Напоминания') return demoEntries.filter((e) => e.type === 'reminder');
		return demoEntries;
	}
</script>

<PageShell title="Последние записи">
	<svelte:fragment slot="subheader">
		<div class="flex items-center justify-between gap-3 text-sm text-muted-foreground px-0">
			<div>
				<p>
					{heroState.inbox} во входящих · {heroState.drafts} черновика · AI обрабатывает {heroState.aiPending}
				</p>
			</div>
			<Button size="sm" variant="secondary" class="gap-1.5" href="/new">
				<Sparkles class="size-4" />
				<span>Новая</span>
			</Button>
		</div>
	</svelte:fragment>
	<section class="space-y-4">
		<div class="flex flex-wrap items-center gap-2">
			{#if heroState.offline}
				<Badge variant="outline" class="gap-1.5 border-dashed bg-amber-50 text-amber-700">
					<WifiOff class="size-3.5" />
					<span>Оффлайн, черновики локально</span>
				</Badge>
			{/if}
			<Badge variant="secondary" class="gap-1.5">
				<Wand2 class="size-3.5" />
				AI черновики: {heroState.aiPending}
			</Badge>
		</div>

		<div class="flex gap-2 overflow-x-auto pb-1">
			{#each filters as filter}
				<button
					class={cn(
						'rounded-full border px-4 py-2 text-sm font-medium transition-colors',
						activeFilter === filter
							? 'bg-emerald-500 text-white border-emerald-500'
							: 'border-border bg-background hover:bg-accent text-foreground'
					)}
					type="button"
					onclick={() => (activeFilter = filter)}
				>
					{filter}
				</button>
			{/each}
		</div>

		<div class="grid gap-3">
			{#each getFilteredEntries() as entry}
				<article class="rounded-2xl border border-border/80 bg-card/70 p-4">
					<div class="flex items-start justify-between gap-2">
						<div class="space-y-1">
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
								class={cn(
									'text-xs',
									entry.status === 'draft' ? 'border-dashed' : '',
									entry.status === 'synced' ? 'bg-emerald-100 text-emerald-800' : ''
								)}
							>
								{entry.status === 'draft'
									? 'AI черновик'
									: entry.status === 'ready'
										? 'Готово'
										: 'Синхронизировано'}
							</Badge>
							<p class="text-sm text-muted-foreground">
								{entry.date} · {entry.time}
							</p>
							{#if entry.amount}
								<p class="text-lg font-semibold">
									{entry.amount} {entry.currency ?? '₽'}
								</p>
							{/if}
							{#if entry.mood}
								<p class="text-xs text-muted-foreground">
									{moodEmoji[entry.mood] ?? ''} настроение
								</p>
							{/if}
						</div>
					</div>
					<div class="mt-3 flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
						<span class="rounded-full bg-accent px-2.5 py-1">
							Источник: {entry.source ?? 'text'}
						</span>
						<span class="rounded-full bg-accent px-2.5 py-1">
							Уверенность: {entry.confidence}
						</span>
						{#if entry.attachments}
							<span class="flex items-center gap-1 rounded-full bg-accent px-2.5 py-1">
								<Image class="size-3.5" />
								{entry.attachments} вложения
							</span>
						{/if}
						<Button variant="ghost" size="sm" class="ml-auto gap-1" href={`/entries/${entry.id}`}>
							<Link2 class="size-3.5" />
							Открыть
						</Button>
					</div>
				</article>
			{/each}
		</div>

		<section class="rounded-2xl border border-border bg-muted/40 p-4">
			<div class="flex items-center justify-between">
				<div>
					<p class="text-sm font-semibold">Напоминания</p>
					<p class="text-xs text-muted-foreground">Быстро закрыть задолженности и чеки</p>
				</div>
				<Badge variant="secondary" class="gap-1.5">
					<Bell class="size-3.5" />
					{demoReminders.length}
				</Badge>
			</div>
			<div class="mt-3 space-y-2">
				{#each demoReminders as reminder}
					<div class="flex items-start justify-between gap-2 rounded-xl bg-background px-3 py-2">
						<div>
							<p class="text-sm font-medium leading-tight">{reminder.title}</p>
							<p class="text-xs text-muted-foreground">{reminder.due} · {reminder.context}</p>
						</div>
						<Button variant="ghost" size="icon-sm" aria-label="Открыть">
							<Link2 class="size-4" />
						</Button>
					</div>
				{/each}
			</div>
		</section>

		<section class="rounded-2xl border border-border/80 bg-card p-4">
			<div class="flex items-center gap-2">
				<FileText class="size-4 text-muted-foreground" />
				<p class="text-sm font-semibold">Черновики AI</p>
			</div>
			<p class="mt-1 text-sm text-muted-foreground">
				Список/чек, долги, эмоции и напоминания — можно доработать позже, оффлайн.
			</p>
			<div class="mt-3 flex flex-wrap gap-2">
				<Button variant="secondary" size="sm" href="/new">Дописать сейчас</Button>
				<Button variant="ghost" size="sm">Скрыть подсказку</Button>
			</div>
		</section>
	</section>
</PageShell>
