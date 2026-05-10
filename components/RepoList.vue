<template>
  <div class="w-full space-y-4">
    <div
      class="flex flex-col gap-3 sm:flex-row sm:flex-wrap sm:items-center sm:justify-between md:sticky md:top-0 md:z-10 md:-mx-4 md:px-4 md:py-3 md:bg-ink-400/95 md:backdrop-blur-sm md:border-b md:border-ink-200"
    >
      <label class="flex min-w-0 flex-1 flex-col gap-1 sm:max-w-md">
        <span class="text-xs font-semibold uppercase tracking-wider text-slate">Search</span>
        <span class="relative">
          <MagnifyingGlassIcon
            class="pointer-events-none absolute left-3 top-1/2 h-5 w-5 -translate-y-1/2 text-vanilla-400"
            aria-hidden="true"
          />
          <input
            v-model.trim="searchQuery"
            type="search"
            placeholder="Filter by name, owner, or description…"
            autocomplete="off"
            class="w-full rounded-md border border-ink-200 bg-ink-300 py-2 pl-10 pr-3 text-sm text-vanilla-300 placeholder:text-vanilla-400 focus:border-juniper focus:outline-none focus:ring-1 focus:ring-juniper"
          />
        </span>
      </label>
      <label class="flex flex-col gap-1 sm:w-48">
        <span class="text-xs font-semibold uppercase tracking-wider text-slate">Sort by</span>
        <select
          v-model="sortKey"
          class="rounded-md border border-ink-200 bg-ink-300 py-2 px-3 text-sm text-vanilla-300 focus:border-juniper focus:outline-none focus:ring-1 focus:ring-juniper"
        >
          <option value="stars">Stars (high → low)</option>
          <option value="activity">Last activity (recent first)</option>
          <option value="name">Name (A → Z)</option>
          <option value="issues">Open curated issues (most first)</option>
        </select>
      </label>
    </div>

    <p class="text-sm text-vanilla-400" role="status">
      Showing <span class="font-mono text-vanilla-300">{{ displayedCount }}</span> of
      <span class="font-mono text-vanilla-300">{{ props.repositories.length }}</span> repositories
      <span v-if="searchQuery"> matching “{{ searchQuery }}”</span>
    </p>

    <RepoBox v-for="repo in sortedRepos" :key="repo.id" :repo="repo" />

    <p
      v-if="sortedRepos.length === 0"
      class="rounded-md border border-dashed border-ink-200 bg-ink-300 px-4 py-8 text-center text-sm text-vanilla-400"
    >
      No repositories match your filters.
      <button type="button" class="ml-2 text-juniper underline hover:text-light_juniper" @click="searchQuery = ''">
        Clear search
      </button>
    </p>
  </div>
</template>

<script setup>
import { MagnifyingGlassIcon } from '@heroicons/vue/24/outline'

const props = defineProps({
  repositories: {
    type: Array,
    required: true
  }
})

const searchQuery = ref('')
const sortKey = ref('stars')

const normalizedQuery = computed(() => searchQuery.value.toLowerCase())

const filteredRepos = computed(() => {
  const q = normalizedQuery.value
  if (!q) return props.repositories
  return props.repositories.filter(repo => {
    const haystack = `${repo.owner} ${repo.name} ${repo.description ?? ''}`.toLowerCase()
    return haystack.includes(q)
  })
})

const sortedRepos = computed(() => {
  const list = [...filteredRepos.value]
  const key = sortKey.value
  if (key === 'stars') {
    list.sort((a, b) => (b.stars ?? 0) - (a.stars ?? 0))
  } else if (key === 'activity') {
    list.sort((a, b) => new Date(b.last_modified).getTime() - new Date(a.last_modified).getTime())
  } else if (key === 'name') {
    list.sort((a, b) => `${a.owner}/${a.name}`.localeCompare(`${b.owner}/${b.name}`, undefined, { sensitivity: 'base' }))
  } else if (key === 'issues') {
    list.sort((a, b) => (b.issues?.length ?? 0) - (a.issues?.length ?? 0))
  }
  return list
})

const displayedCount = computed(() => sortedRepos.value.length)
</script>
