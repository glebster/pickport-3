<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import Button from '$lib/components/ui/button/button.svelte';
	import { Users, Plus } from 'lucide-svelte';
</script>

<PageShell title="Группы">
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<Users class="size-4" />
			<span>Совместные пространства (мок)</span>
		</div>
	</svelte:fragment>
	<section class="space-y-3">
		<div class="rounded-2xl border border-border bg-card/70 p-4">
			<p class="text-sm text-muted-foreground">Совместные списки появятся позже. Пока — заглушка.</p>
		</div>
		<Button variant="secondary" class="gap-1.5">
			<Plus class="size-4" />
			Создать группу
		</Button>
	</section>
</PageShell>

