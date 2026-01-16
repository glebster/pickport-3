import { demoEntries, demoLists, demoReminders } from '$lib/mocks/demo-data.js';
import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => {
	const entry = demoEntries.find((e) => e.id === params.id);
	if (!entry) {
		throw error(404, 'Entry not found');
	}

	const parentList = entry.listId ? demoLists.find((l) => l.id === entry.listId) : undefined;
	const reminders = demoReminders.filter(
		(r) => r.context === entry.id || (entry.listId && r.context === entry.listId)
	);

	return {
		entry,
		parentList,
		reminders
	};
};

