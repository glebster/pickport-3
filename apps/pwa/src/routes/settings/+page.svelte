<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import Button from '$lib/components/ui/button/button.svelte';
	import { Shield, Download, Upload, Bell } from 'lucide-svelte';
</script>

<PageShell title="Настройки">
	<svelte:fragment slot="subheader">
		<p class="text-sm text-muted-foreground px-0">Приватность, резервные копии, уведомления</p>
	</svelte:fragment>
	<section class="space-y-4">
		<div class="space-y-2 rounded-2xl border border-border bg-card/70 p-4">
			<div class="flex items-center gap-2">
				<Shield class="size-4 text-emerald-500" />
				<p class="text-sm font-semibold">Приватность</p>
			</div>
			<p class="text-sm text-muted-foreground">Данные хранятся локально (IndexedDB). Синхронизация — только по opt-in.</p>
		</div>

		<div class="space-y-2 rounded-2xl border border-border bg-card/70 p-4">
			<div class="flex items-center gap-2">
				<Download class="size-4 text-emerald-500" />
				<p class="text-sm font-semibold">Экспорт</p>
			</div>
			<Button size="sm" variant="secondary">Сохранить дамп</Button>
		</div>

		<div class="space-y-2 rounded-2xl border border-border bg-card/70 p-4">
			<div class="flex items-center gap-2">
				<Upload class="size-4 text-emerald-500" />
				<p class="text-sm font-semibold">Импорт</p>
			</div>
			<Button size="sm" variant="outline">Загрузить файл</Button>
		</div>

		<div class="space-y-2 rounded-2xl border border-border bg-card/70 p-4">
			<div class="flex items-center gap-2">
				<Bell class="size-4 text-emerald-500" />
				<p class="text-sm font-semibold">Уведомления</p>
			</div>
			<p class="text-sm text-muted-foreground">Включить напоминания оффлайн/пуш при opt-in.</p>
		</div>
	</section>
</PageShell>

