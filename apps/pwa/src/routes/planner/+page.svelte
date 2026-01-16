<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import { demoEntries, demoLists, demoReminders } from '$lib/mocks/demo-data.js';
	import { CalendarDays, Clock, Bell } from 'lucide-svelte';

	function resolveContext(context: string) {
		const entry = demoEntries.find((e) => e.id === context);
		if (entry) return { title: entry.title, href: `/entries/${entry.id}` };
		const list = demoLists.find((l) => l.id === context);
		if (list) return { title: list.title, href: `/lists/${list.id}` };
		return { title: context, href: undefined };
	}
</script>

<PageShell title="Планировщик">
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<CalendarDays class="size-4" />
			<span>Напоминания, привязанные к записям и спискам</span>
		</div>
	</svelte:fragment>
	<section class="space-y-3">
		<div class="rounded-2xl border border-border bg-card/70 p-4">
			<p class="text-sm text-muted-foreground">Календарь (mock) — позже подключим датапикер/таймлайн.</p>
		</div>

		<div class="space-y-2">
			{#each demoReminders as reminder}
				{@const ctx = resolveContext(reminder.context)}
				<div class="flex items-start justify-between rounded-xl border border-border/70 bg-background px-3 py-2 text-sm">
					<div class="space-y-0.5">
						<p class="font-medium">{reminder.title}</p>
						<p class="text-xs text-muted-foreground">{reminder.due}</p>
						<p class="text-xs text-muted-foreground">Контекст: {ctx.title}</p>
					</div>
					<div class="flex items-center gap-2 text-xs text-muted-foreground">
						<Bell class="size-4" />
						{#if ctx.href}
							<a class="underline" href={ctx.href}>Открыть</a>
						{/if}
					</div>
				</div>
			{/each}
		</div>
	</section>
</PageShell>

