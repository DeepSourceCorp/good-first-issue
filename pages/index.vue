<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in sortedRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import { useStarsSortOrder, useActivitySortOrder } from '~/composables/states'

// Get the sort order states
const starsSortOrder = useStarsSortOrder()
const activitySortOrder = useActivitySortOrder()

// Computed property for sorted repositories
const sortedRepositories = computed(() => {
  let repos = [...Repositories] // Create a copy to avoid mutating the original
  
  // Sort by stars if selected
  if (starsSortOrder.value !== 'none') {
    repos.sort((a, b) => {
      if (starsSortOrder.value === 'desc') {
        return b.stars - a.stars
      } else {
        return a.stars - b.stars
      }
    })
  }
  
  // Sort by activity if selected (and if stars sorting is not applied)
  if (activitySortOrder.value !== 'none' && starsSortOrder.value === 'none') {
    repos.sort((a, b) => {
      const dateA = new Date(a.last_modified)
      const dateB = new Date(b.last_modified)
      if (activitySortOrder.value === 'desc') {
        return dateB - dateA
      } else {
        return dateA - dateB
      }
    })
  }
  
  return repos
})

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
