<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import { demoReminders } from '$lib/mocks/demo-data.js';
	import { Bell, Check, Clock } from 'lucide-svelte';
</script>

<PageShell title="Напоминания">
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<Clock class="size-4" />
			<span>{demoReminders.length} активных</span>
		</div>
	</svelte:fragment>
	<section class="space-y-3">
		{#each demoReminders as reminder}
			<div class="rounded-2xl border border-border bg-card/70 px-3 py-2">
				<div class="flex items-center justify-between gap-2">
					<div>
						<p class="text-sm font-medium leading-tight">{reminder.title}</p>
						<p class="text-xs text-muted-foreground">{reminder.due} · {reminder.context}</p>
					</div>
					<div class="flex items-center gap-2">
						<Badge variant="secondary" class="gap-1.5 text-xs">
							<Bell class="size-3.5" />
							Активно
						</Badge>
						<Button variant="ghost" size="icon-sm" aria-label="Завершить">
							<Check class="size-4" />
						</Button>
					</div>
				</div>
			</div>
		{/each}
	</section>
</PageShell>

