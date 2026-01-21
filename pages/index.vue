<template>
  <div class="p-4 w-full">
    <input
      v-model="searchQuery"
      type="text"
      placeholder="Search projects..."
      class="mb-4 px-3 py-2 rounded border border-ink-200 w-full bg-ink-400 text-vanilla-100 text-sm placeholder:text-vanilla-400"
    />

    <div class="mb-4">
      <div class="inline-flex items-center border border-ink-200 bg-ink-400 text-vanilla-100 rounded px-3 py-1 text-sm">
        <label for="sortOrder" class="mr-2 text-slate font-semibold">Sort by:</label>
        <select
          v-model="sortOrder"
          id="sortOrder"
          class="bg-ink-400 text-vanilla-100 font-semibold border-none outline-none cursor-pointer"
        >
          <option value="">Best match</option>
          <option value="newest">Newest</option>
          <option value="oldest">Oldest</option>
        </select>
      </div>
    </div>

    <RepoBox
      v-for="repo in filteredAndSortedRepos"
      :key="repo.id"
      :repo="repo"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Repositories from '~/data/generated.json'
import { useFilteredRepos } from '~/composables/useFilteredRepos'

const allRepos = ref(Repositories)

const {
  searchQuery,
  sortOrder,
  filteredAndSortedRepos
} = useFilteredRepos(allRepos)

useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
    {
      name: 'description',
      content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
    }
  ]
})
</script>
