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
import Tags from '~/data/tags.json'

const route = useRoute()
const searchQuery = ref('')
const sortBy = ref('default')

// Filter repositories of this language first
const languageRepositories = computed(() => {
  return Repositories.filter(repository => repository.slug === route.params.slug)
})

const filteredRepositories = computed(() => {
  let result = [...languageRepositories.value]

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

const tag = Tags.find(t => t.slug === route.params.slug)
const languageName = computed(() => {
  if (tag) return tag.language
  if (languageRepositories.value.length > 0) return languageRepositories.value[0].language
  return route.params.slug ? (route.params.slug.charAt(0).toUpperCase() + route.params.slug.slice(1)) : 'Unknown'
})

useHead({
  title: `${languageName.value} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${languageName.value} from popular open-source projects that you can easily fix.`
  }]
})
</script>

