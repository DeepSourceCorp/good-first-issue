<template>
  <div class="p-4 w-full">
    <RepoFilters @change="filters = $event" />
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
    <p v-if="repositories.length === 0" class="py-8 text-center text-sm text-vanilla-400">
      No repositories match the selected filters.
    </p>
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import { filterAndSortRepositories } from '~/utils/repoFilters'

const filters = ref({
  minStars: 0,
  activityMonths: 'all'
})

const repositories = computed(() => {
  return filterAndSortRepositories(Repositories, filters.value)
})

useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
    {
      name: 'description',
      content:
        'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
    }
  ]
})
</script>
