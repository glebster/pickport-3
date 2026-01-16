<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import Button from '$lib/components/ui/button/button.svelte';
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import { quickSources } from '$lib/mocks/demo-data.js';
	import { Upload, Mic, Camera, FileUp, Text } from 'lucide-svelte';
</script>

<PageShell title="Быстрый ввод">
	<svelte:fragment slot="subheader">
		<p class="text-sm text-muted-foreground px-0">Минимальный экран для мгновенного добавления</p>
	</svelte:fragment>
	<section class="space-y-4">
		<label class="block">
			<p class="text-xs text-muted-foreground mb-1">Что произошло?</p>
			<textarea
				class="w-full rounded-xl border border-border bg-background px-3 py-2 text-sm focus:border-emerald-400 focus:outline-none"
				rows="3"
				placeholder="Например: «Сфоткал чек из Перекрёстка…»"
			/>
		</label>

		<div class="grid grid-cols-2 gap-2">
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

		<div class="rounded-xl border border-dashed border-border px-3 py-2 text-sm text-muted-foreground">
			<Upload class="mr-2 inline size-4 align-text-bottom" />
			Перетащи фото/файл или вставь ссылку — сохраним как черновик.
		</div>

		<div class="flex gap-2">
			<Button class="flex-1">Сохранить во входящие</Button>
			<Button variant="ghost" class="flex-1">Отмена</Button>
		</div>

		<Badge variant="secondary" class="text-xs">Автосохранение локально (offline-first)</Badge>
	</section>
</PageShell>

