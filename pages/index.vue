<template>
  <div class="p-4 w-full">
    <SortSelector />
    <RepoBox v-for="repo in sortedRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import Repositories from '~/data/generated.json'

const sortKey = useSortKey()

const sortedRepositories = computed(() => {
  const list = [...Repositories]
  if (sortKey.value === 'stars-desc') {
    return list.sort((a, b) => b.stars - a.stars)
  } else if (sortKey.value === 'stars-asc') {
    return list.sort((a, b) => a.stars - b.stars)
  } else if (sortKey.value === 'issues-desc') {
    return list.sort((a, b) => b.issues.length - a.issues.length)
  } else if (sortKey.value === 'activity-desc') {
    return list.sort((a, b) => new Date(b.last_modified) - new Date(a.last_modified))
  }
  return list
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
