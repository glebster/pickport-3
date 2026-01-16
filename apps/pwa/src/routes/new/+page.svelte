<script lang="ts">
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import { PageShell } from '$lib/components/layout';
	import { demoEntries, demoLists, quickSources } from '$lib/mocks/demo-data.js';
	import { cn } from '$lib/utils.js';
	import {
		BellPlus,
		Camera,
		Check,
		ChevronLeft,
		FileUp,
		Mic,
		Sparkles,
		Text,
		Upload,
		Wand2
	} from 'lucide-svelte';

	let step = $state<'capture' | 'draft'>('capture');
	const draftPreview = demoEntries.find((e) => e.status === 'draft');
	const draftList = demoLists[0];
</script>

<PageShell title="Новая запись">
	<svelte:fragment slot="subheader">
		<div class="flex items-center justify-between gap-3 text-sm text-muted-foreground px-0">
			<p>Шаг 1/2 — собрать контент; шаг 2/2 — подтвердить AI черновик и напоминания.</p>
			<Badge variant="secondary" class="gap-1.5">
				<Check class="size-3.5" />
				Автосохранение
			</Badge>
		</div>
	</svelte:fragment>
	<svelte:fragment slot="footer">
		<div class="flex items-center gap-2 text-sm">
			<div class="h-2 flex-1 rounded-full bg-accent">
				<div class={cn('h-2 rounded-full bg-emerald-500 transition-all', step === 'capture' ? 'w-1/2' : 'w-full')} />
			</div>
			<span class="text-muted-foreground">{step === 'capture' ? 'Шаг 1/2' : 'Шаг 2/2'}</span>
		</div>
	</svelte:fragment>
	<section class="space-y-5">
		{#if step === 'capture'}
			<div class="space-y-4">
				<div class="rounded-2xl border border-border bg-card/70 p-4">
					<div class="flex items-center justify-between gap-3">
						<div>
							<p class="text-sm font-semibold">Быстрый ввод</p>
							<p class="text-xs text-muted-foreground">
								Фокус сразу в поле. Можно комбинировать текст, фото, файл, ссылку.
							</p>
						</div>
						<Badge variant="outline" class="text-xs">Шаг 1</Badge>
					</div>
					<label class="mt-3 block">
						<p class="text-xs text-muted-foreground mb-1">Что произошло?</p>
						<textarea
							class="w-full rounded-xl border border-border bg-background px-3 py-2 text-sm shadow-inner focus:border-emerald-400 focus:outline-none"
							rows="3"
							placeholder="Например: «Сфоткал чек из Перекрёстка, нужно распознать и разделить по людям»"
						/>
					</label>
					<div class="mt-3 grid grid-cols-2 gap-2">
						{#each quickSources as source}
							<Button variant="outline" size="sm" class="justify-between">
								<span class="flex items-center gap-2">
									{#if source.id === 'voice'}
										<Mic class="size-4" />
									{:else if source.id === 'photo'}
										<Camera class="size-4" />
									{:else if source.id === 'file'}
										<FileUp class="size-4" />
									{:else}
										<Text class="size-4" />
									{/if}
									{source.label}
								</span>
								<span class="text-xs text-muted-foreground">{source.hint}</span>
							</Button>
						{/each}
					</div>
					<div class="mt-3 rounded-xl border border-dashed border-border px-3 py-2 text-sm text-muted-foreground">
						<Upload class="mr-2 inline size-4 align-text-bottom" />
						Перетащи сюда фото/файл или вставь ссылку — покажем превью и спросим контекст.
					</div>
					<div class="mt-3 flex flex-col gap-1.5 text-sm text-muted-foreground">
						<div class="flex items-center justify-between">
							<span>Вложения</span>
							<Badge variant="outline" class="text-xs">до 3 фото</Badge>
						</div>
						<div class="flex flex-wrap gap-2">
							<span class="rounded-lg bg-accent px-3 py-1">Фото чека · 1.2 МБ</span>
							<span class="rounded-lg bg-accent px-3 py-1">Ссылка на оплату</span>
						</div>
					</div>
					<div class="mt-4 flex flex-wrap gap-2">
						<Button class="flex-1" on:click={() => (step = 'draft')}>
							<Sparkles class="size-4" />
							<span>Продолжить</span>
						</Button>
						<Button variant="secondary" class="flex-1">Сохранить черновик</Button>
						<Button variant="ghost" class="flex-1">Отмена</Button>
					</div>
				</div>
			</div>
		{:else}
			<div class="space-y-4">
				<div class="rounded-2xl border border-border bg-card/70 p-4">
					<div class="flex items-center justify-between gap-3">
						<div>
							<p class="text-sm font-semibold">AI черновик</p>
							<p class="text-xs text-muted-foreground">
								Проверь, отредактируй и подтверди. Можно вернуться к вводу без потери данных.
							</p>
						</div>
						<Badge variant="outline" class="text-xs">Шаг 2</Badge>
					</div>
					{#if draftPreview}
						<article class="mt-3 space-y-2 rounded-xl border border-border/80 bg-background p-3">
							<div class="flex items-start justify-between gap-2">
								<div>
									<p class="text-xs uppercase text-muted-foreground">AI · {draftPreview.source}</p>
									<h2 class="text-base font-semibold leading-tight">{draftPreview.title}</h2>
									<p class="text-sm text-muted-foreground">{draftPreview.summary}</p>
								</div>
								<Button variant="ghost" size="icon-sm" aria-label="Назад" on:click={() => (step = 'capture')}>
									<ChevronLeft class="size-4" />
								</Button>
							</div>
							<div class="flex flex-wrap gap-1.5">
								{#if draftPreview.tags}
									{#each draftPreview.tags as tag}
										<Badge variant="outline" class="text-xs">{tag}</Badge>
									{/each}
								{/if}
								<Badge variant="secondary" class="text-xs">Уверенность: {draftPreview.confidence}</Badge>
							</div>
							<div class="rounded-lg bg-accent px-3 py-2 text-sm text-muted-foreground">
								<Wand2 class="mr-2 inline size-4 align-text-bottom" />
								ИИ нашёл позиции и предложил напоминание. Можно удалить/добавить поля.
							</div>
						</article>
					{/if}

					{#if draftList}
						<div class="mt-3 rounded-xl border border-dashed border-border px-3 py-2">
							<p class="text-sm font-semibold">{draftList.title}</p>
							<p class="text-xs text-muted-foreground">
								{draftList.summary} · {draftList.entriesCount} позиций · {draftList.total} ₽
							</p>
							<div class="mt-2 flex flex-wrap gap-1.5">
								{#each draftList.tags ?? [] as tag}
									<Badge variant="outline" class="text-xs">{tag}</Badge>
								{/each}
								<Badge variant="secondary" class="text-xs">source: {draftList.source}</Badge>
							</div>
						</div>
					{/if}

					<div class="mt-3 flex flex-col gap-2">
						<p class="text-sm font-semibold">Напоминание</p>
						<div class="flex flex-col gap-2 rounded-xl border border-border bg-background p-3">
							<div class="flex items-start gap-2">
								<BellPlus class="mt-0.5 size-4 text-emerald-500" />
								<div>
									<p class="text-sm font-medium">Подтвердить долги и чек</p>
									<p class="text-xs text-muted-foreground">Завтра, 10:00 · пуш + оффлайн уведомление</p>
								</div>
							</div>
							<div class="grid grid-cols-2 gap-2">
								<Button variant="outline" size="sm">Сместить на день</Button>
								<Button variant="ghost" size="sm">Удалить</Button>
							</div>
						</div>
					</div>

					<div class="mt-4 flex flex-wrap gap-2">
						<Button class="flex-1">
							<Check class="size-4" />
							<span>Подтвердить и сохранить</span>
						</Button>
						<Button variant="secondary" class="flex-1" on:click={() => (step = 'capture')}>
							<ChevronLeft class="size-4" />
							<span>Вернуться к вводу</span>
						</Button>
						<Button variant="ghost" class="flex-1">Сохранить черновик</Button>
					</div>
				</div>
			</div>
		{/if}
	</section>
</PageShell>

