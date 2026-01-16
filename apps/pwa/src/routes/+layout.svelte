<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import Button from '$lib/components/ui/button/button.svelte';
	import { cn } from '$lib/utils.js';
	import { page } from '$app/stores';
	import { Home, List, Plus, Radio } from 'lucide-svelte';

	let { children } = $props();

	const pageMaxWidth = 'max-w-md';
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="min-h-dvh bg-background text-foreground flex flex-col">
	<div class={`relative mx-auto ${pageMaxWidth} w-full flex min-h-dvh flex-col`}>
		<main class="flex-1 px-4 pb-24 pt-3">{@render children()}</main>
	</div>

	<a
		href="/new"
		class="pointer-events-auto fixed z-50 grid size-14 place-items-center rounded-full bg-emerald-500 text-white shadow-lg shadow-emerald-500/30 transition hover:bg-emerald-600 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500 focus-visible:ring-offset-2"
		style="right: max(12px, calc((100vw - 28rem) / 2 + 12px)); bottom: calc(env(safe-area-inset-bottom, 16px) + 16px);"
		aria-label="Создать новую запись"
	>
		<Plus class="size-6" />
	</a>
</div>
