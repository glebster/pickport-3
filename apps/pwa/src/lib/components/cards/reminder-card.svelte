<script lang="ts">
	import Badge from '$lib/components/ui/badge/badge.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
	import type { ReminderMock } from '$lib/mocks/demo-data';
	import { Bell, Link2 } from 'lucide-svelte';

	let {
		reminder,
		href,
		cta = 'Открыть'
	}: {
		reminder: ReminderMock;
		href?: string;
		cta?: string;
	} = $props();
</script>

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
			{#if href}
				<Button variant="ghost" size="icon-sm" aria-label={cta} href={href}>
					<Link2 class="size-4" />
				</Button>
			{/if}
		</div>
	</div>
</div>

