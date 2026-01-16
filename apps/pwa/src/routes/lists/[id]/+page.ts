import { demoEntries, demoLists, demoReminders } from '$lib/mocks/demo-data.js';
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
	const list = demoLists.find((l) => l.id === params.id);
	if (!list) {
		throw error(404, 'List not found');
	}

	const entries = demoEntries.filter((e) => e.listId === list.id);
	const reminders = demoReminders.filter((r) => r.context === list.id);

	return {
		list,
		entries,
		reminders
	};
};

