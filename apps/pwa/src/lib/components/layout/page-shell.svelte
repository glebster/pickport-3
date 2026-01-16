<script lang="ts">
	type Action = () => void;

	let {
		title = '',
		showBack = false,
		showClose = false,
		autoScroll = false,
		onBack,
		onClose,
		header = undefined,
		subheader = undefined,
		bottomBar = undefined,
		footer = undefined,
		children
	}: {
		title?: string;
		showBack?: boolean;
		showClose?: boolean;
		autoScroll?: boolean;
		onBack?: Action;
		onClose?: Action;
		header?: any;
		subheader?: any;
		bottomBar?: any;
		footer?: any;
		children?: any;
	} = $props();

	let scrollEl = $state<HTMLElement | null>(null);

	const fallbackBack: Action = () => {
		if (typeof history !== 'undefined') history.back();
	};

	const fallbackClose: Action = () => {
		if (typeof history !== 'undefined') history.back();
	};

	const handleBack = () => {
		if (onBack) return onBack();
		fallbackBack();
	};

	const handleClose = () => {
		if (onClose) return onClose();
		fallbackClose();
	};

	$effect(() => {
		if (autoScroll && scrollEl) {
			scrollEl.scrollTop = scrollEl.scrollHeight;
		}
	});
</script>

<div class="flex min-h-dvh flex-col bg-background text-foreground">
	<header class="sticky top-0 z-20 flex items-center justify-between gap-2 border-b border-border bg-background/90 px-4 py-3 backdrop-blur">
		{#if header}
			{@render header()}
		{:else}
			<div class="flex items-center gap-3">
				{#if showBack}
					<button
						type="button"
						class="rounded-full border border-border px-3 py-1.5 text-sm font-medium hover:bg-accent focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500 focus-visible:ring-offset-2"
						onclick={handleBack}
					>
						Назад
					</button>
				{/if}
				<h1 class="text-lg font-semibold leading-tight">{title}</h1>
			</div>
			{#if showClose}
				<button
					type="button"
					class="rounded-full border border-border px-3 py-1.5 text-sm font-medium hover:bg-accent focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500 focus-visible:ring-offset-2"
					onclick={handleClose}
				>
					Закрыть
				</button>
			{:else}
				<div class="w-[72px]" aria-hidden="true" />
			{/if}
		{/if}
	</header>

	{#if subheader}
		<div class="sticky top-[56px] z-10 border-b border-border bg-background/90 px-4 py-2 backdrop-blur">
			{@render subheader()}
		</div>
	{/if}

	<div class="relative flex flex-1 flex-col">
		<div
			class="flex-1 overflow-y-auto px-4 pb-4 pt-3"
			bind:this={scrollEl}
			data-auto-scroll={autoScroll ? 'true' : 'false'}
		>
			{@render children?.()}
		</div>

		{#if bottomBar}
			<div class="border-t border-border bg-background px-4 py-2">
				{@render bottomBar()}
			</div>
		{/if}

		{#if footer}
			<div class="border-t border-border bg-background px-4 py-3">
				{@render footer()}
			</div>
		{/if}
	</div>
</div>

