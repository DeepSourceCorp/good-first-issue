<template>
  <div class="p-4 w-full">
    <ControlPanel
      v-model:searchQuery="searchQuery"
      v-model:sortBy="sortBy"
    />
    <div v-if="filteredRepositories.length > 0">
      <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
    </div>
    <div v-else class="text-center py-12 text-vanilla-400">
      <p class="text-lg font-semibold mb-2">No projects found</p>
      <p class="text-sm">Try adjusting your search keywords.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'

const searchQuery = ref('')
const sortBy = ref('default')

const filteredRepositories = computed(() => {
  let result = [...Repositories]

  // Filter by search query
  if (searchQuery.value.trim()) {
    const query = searchQuery.value.toLowerCase().trim()
    result = result.filter(repo => {
      const nameMatch = `${repo.owner}/${repo.name}`.toLowerCase().includes(query)
      const descMatch = repo.description && repo.description.toLowerCase().includes(query)
      return nameMatch || descMatch
    })
  }

  // Sort
  if (sortBy.value === 'stars-desc') {
    result.sort((a, b) => (b.stars || 0) - (a.stars || 0))
  } else if (sortBy.value === 'stars-asc') {
    result.sort((a, b) => (a.stars || 0) - (b.stars || 0))
  } else if (sortBy.value === 'issues-desc') {
    result.sort((a, b) => (b.issues?.length || 0) - (a.issues?.length || 0))
  } else if (sortBy.value === 'activity-desc') {
    result.sort((a, b) => new Date(b.last_modified).getTime() - new Date(a.last_modified).getTime())
  }

  return result
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

