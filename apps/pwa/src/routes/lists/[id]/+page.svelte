<script lang="ts">
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import { PageShell } from '$lib/components/layout';
	import type { PageData } from './$types';
	import { ArrowLeft, ArrowRight, Layers, Sparkles, Tag } from 'lucide-svelte';

	let { data }: { data: PageData } = $props();
	const { list, entries, reminders } = data;
</script>

<PageShell title={list.title} showBack>
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<span>List · {list.source}</span>
			<span class="rounded-full bg-accent px-2.5 py-1">{list.date}</span>
			<span class="rounded-full bg-accent px-2.5 py-1">
				<Layers class="mr-1 inline size-3.5" />
				{list.entriesCount} записей
			</span>
			{#if list.total}
				<span class="rounded-full bg-accent px-2.5 py-1">
					{list.total} {list.currency ?? '₽'}
				</span>
			{/if}
			<span class="rounded-full bg-accent px-2.5 py-1">Уверенность: {list.confidence}</span>
		</div>
	</svelte:fragment>
	<svelte:fragment slot="footer">
		<div class="flex flex-wrap gap-2">
			<Button variant="secondary" href="/new">Добавить запись</Button>
			<Button variant="ghost" href="/lists">К спискам</Button>
			<Button variant="ghost" href="/">В ленту</Button>
		</div>
	</svelte:fragment>
	<section class="space-y-4">
		{#if list.tags?.length}
			<div class="flex flex-wrap gap-1.5">
				{#each list.tags as tag}
					<Badge variant="outline" class="text-xs">
						<Tag class="mr-1 size-3.5" />
						{tag}
					</Badge>
				{/each}
			</div>
		{/if}

		<div class="space-y-3 rounded-2xl border border-border/80 bg-card/70 p-4">
			<p class="text-sm font-semibold">Записи списка</p>
			<div class="space-y-2">
				{#each entries as entry}
					<div class="flex items-start justify-between gap-2 rounded-xl bg-background px-3 py-2">
						<div class="space-y-0.5">
							<p class="text-xs uppercase text-muted-foreground">
								{entry.type === 'debt'
									? 'Долг'
									: entry.type === 'visit'
										? 'Посещение'
										: entry.type === 'reminder'
											? 'Напоминание'
											: 'Запись'}
							</p>
							<p class="text-sm font-medium leading-tight">{entry.title}</p>
							<p class="text-xs text-muted-foreground">{entry.summary}</p>
							<div class="flex flex-wrap gap-1.5">
								{#if entry.tags}
									{#each entry.tags as tag}
										<Badge variant="outline" class="text-[11px]">{tag}</Badge>
									{/each}
								{/if}
							</div>
						</div>
						<div class="flex flex-col items-end gap-2 text-right">
							<Badge variant={entry.status === 'ready' ? 'secondary' : 'outline'} class={entry.status === 'draft' ? 'border-dashed' : ''}>
								{entry.status === 'draft'
									? 'AI черновик'
									: entry.status === 'ready'
										? 'Готово'
										: 'Синхронизировано'}
							</Badge>
							{#if entry.amount}
								<p class="text-sm font-semibold">
									{entry.amount} {entry.currency ?? '₽'}
								</p>
							{/if}
							<Button variant="ghost" size="sm" href={`/entries/${entry.id}`} class="gap-1.5">
								<span>Открыть</span>
								<ArrowRight class="size-4" />
							</Button>
						</div>
					</div>
				{/each}
			</div>
		</div>

		{#if reminders.length}
			<div class="rounded-2xl border border-border bg-muted/40 p-4">
				<p class="text-sm font-semibold">Напоминания по списку</p>
				<div class="mt-2 space-y-2">
					{#each reminders as reminder}
						<div class="flex items-center justify-between gap-2 rounded-xl bg-background px-3 py-2 text-sm">
							<span>{reminder.title}</span>
							<span class="rounded-full bg-accent px-2.5 py-1 text-xs">{reminder.due}</span>
						</div>
					{/each}
				</div>
			</div>
		{/if}
	</section>
</PageShell>

