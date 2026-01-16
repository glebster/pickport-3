<script lang="ts">
	import { PageShell } from '$lib/components/layout';
	import Button from '$lib/components/ui/button/button.svelte';
	import { demoEntries } from '$lib/mocks/demo-data.js';
	import { Sparkles, Send, Bot, User } from 'lucide-svelte';

	let messages = $state([
		{ role: 'bot', text: 'Привет! Что найти или распарсить?' },
		{ role: 'user', text: 'Покажи долги по ужину' },
		{ role: 'bot', text: 'Нашёл 2 долга в списке «Пиццерия на Арбате».' }
	]);
	let input = $state('');

	const short = demoEntries
		.filter((e) => e.type === 'debt')
		.map((e) => `${e.title} — ${e.amount ?? ''} ${e.currency ?? ''}`.trim());

	function send() {
		if (!input.trim()) return;
		messages = [...messages, { role: 'user', text: input }];
		input = '';
	}
</script>

<PageShell title="AI-чат" autoScroll>
	<svelte:fragment slot="subheader">
		<div class="flex items-center gap-2 text-sm text-muted-foreground px-0">
			<Sparkles class="size-4" />
			<span>Вопросы про данные + генерация списков и напоминаний</span>
		</div>
	</svelte:fragment>
	<svelte:fragment slot="bottomBar">
		<form class="flex items-center gap-2" on:submit|preventDefault={send}>
			<input
				class="flex-1 rounded-full border border-border bg-background px-3 py-2 text-sm focus:border-emerald-400 focus:outline-none"
				placeholder="Спроси про чеки, долги, напоминания…"
				bind:value={input}
			/>
			<Button type="submit" size="sm" class="gap-1.5">
				<Send class="size-4" />
				<span>Отправить</span>
			</Button>
		</form>
	</svelte:fragment>
	<div class="space-y-3">
		{#each messages as msg, i}
			<div class="flex gap-2">
				<div class="mt-1">
					{#if msg.role === 'bot'}
						<Bot class="size-4 text-emerald-500" />
					{:else}
						<User class="size-4 text-muted-foreground" />
					{/if}
				</div>
				<div class="rounded-2xl border border-border/70 bg-card/70 px-3 py-2 text-sm">
					<p>{msg.text}</p>
					{#if msg.role === 'bot' && i === messages.length - 1 && short.length}
						<ul class="mt-2 space-y-1 text-xs text-muted-foreground">
							{#each short as line}
								<li>• {line}</li>
							{/each}
						</ul>
					{/if}
				</div>
			</div>
		{/each}
	</div>
</PageShell>

