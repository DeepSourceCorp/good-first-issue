<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in sortedRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'
import { useStarsSortOrder, useActivitySortOrder } from '~/composables/states'

const route = useRoute()

// Get the filtered repositories by language
const filteredRepositories = Repositories.filter(repository => repository.slug === route.params.slug)

// Get the sort order states
const starsSortOrder = useStarsSortOrder()
const activitySortOrder = useActivitySortOrder()

// Computed property for sorted repositories
const sortedRepositories = computed(() => {
  let repos = [...filteredRepositories] // Create a copy to avoid mutating the original
  
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

const tag = Tags.find(t => t.slug === route.params.slug)

useHead({
  title: `${tag.language} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
  }]
})
</script>
