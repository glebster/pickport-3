<script lang="ts">
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import { PageShell } from '$lib/components/layout';
	import { demoLists } from '$lib/mocks/demo-data.js';
	import { cn } from '$lib/utils.js';
	import { ArrowRight, Layers, Sparkles, Wand2 } from 'lucide-svelte';
</script>

<PageShell title="Списки">
	<svelte:fragment slot="subheader">
		<div class="flex items-start justify-between gap-3 text-sm text-muted-foreground px-0">
			<p>Пачки связанных записей (чеки, поездки, совместные расходы).</p>
			<Button size="sm" variant="secondary" class="gap-1.5" href="/new">
				<Sparkles class="size-4" />
				<span>Новый</span>
			</Button>
		</div>
	</svelte:fragment>
	<section class="space-y-4">
		<div class="rounded-2xl border border-emerald-500/20 bg-emerald-50/60 p-4 text-sm text-emerald-900 dark:bg-emerald-500/10 dark:text-emerald-100">
			<div class="flex items-start gap-2">
				<Wand2 class="mt-0.5 size-4" />
				<p>
					Создаём `List`, если есть два и более связанных события. Общий контекст выводим из записей,
					а не храним отдельно — так UX проще и не дублируем данные.
				</p>
			</div>
		</div>

		<div class="grid gap-3">
			{#each demoLists as list}
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
								class={cn(
									'mt-1 text-xs',
									list.status === 'draft' ? 'border-dashed' : '',
									list.status === 'synced' ? 'bg-emerald-100 text-emerald-800' : ''
								)}
							>
								{list.status === 'draft'
									? 'Черновик'
									: list.status === 'ready'
										? 'Готово'
										: 'Синхронизировано'}
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
						<Button variant="ghost" size="sm" class="gap-1.5" href={`/lists/${list.id}`}>
							<span>Открыть</span>
							<ArrowRight class="size-4" />
						</Button>
					</div>
				</article>
			{/each}
		</div>
	</section>
</PageShell>
