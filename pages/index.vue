<template>
  <div class="p-4 w-full">
    <SearchBar v-model="searchQuery" @search="handleSearch" @clear="handleClear" />
    <div v-if="filteredRepositories.length === 0" class="text-center py-12 text-vanilla-400">
      <p class="text-lg">No repositories found matching "{{ searchQuery }}"</p>
      <p class="text-sm mt-2">Try adjusting your search terms</p>
    </div>
    <div v-else class="text-sm text-vanilla-400 mb-2">
      Showing {{ filteredRepositories.length }} of {{ Repositories.length }} repositories
    </div>
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

const searchQuery = ref('')
const filteredRepositories = ref(Repositories)

function handleSearch(query) {
  if (!query || query.trim() === '') {
    filteredRepositories.value = Repositories
    return
  }

  const lowerQuery = query.toLowerCase()
  filteredRepositories.value = Repositories.filter(repo => {
    return (
      repo.name.toLowerCase().includes(lowerQuery) ||
      repo.owner.toLowerCase().includes(lowerQuery) ||
      repo.description.toLowerCase().includes(lowerQuery) ||
      repo.language.toLowerCase().includes(lowerQuery)
    )
  })
}

function handleClear() {
  searchQuery.value = ''
  filteredRepositories.value = Repositories
}

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
