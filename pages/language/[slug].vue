<template>
  <div class="p-4 w-full">
    <SearchBar v-model="searchQuery" @search="handleSearch" @clear="handleClear" />
    <div v-if="filteredRepositories.length === 0" class="text-center py-12 text-vanilla-400">
      <p class="text-lg">No repositories found matching "{{ searchQuery }}"</p>
      <p class="text-sm mt-2">Try adjusting your search terms</p>
    </div>
    <div v-else class="text-sm text-vanilla-400 mb-2">
      Showing {{ filteredRepositories.length }} of {{ repositories.length }} repositories
    </div>
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const repositories = Repositories.filter(repository => repository.slug === route.params.slug)

const searchQuery = ref('')
const filteredRepositories = ref(repositories)

function handleSearch(query) {
  if (!query || query.trim() === '') {
    filteredRepositories.value = repositories
    return
  }

  const lowerQuery = query.toLowerCase()
  filteredRepositories.value = repositories.filter(repo => {
    return (
      repo.name.toLowerCase().includes(lowerQuery) ||
      repo.owner.toLowerCase().includes(lowerQuery) ||
      repo.description.toLowerCase().includes(lowerQuery)
    )
  })
}

function handleClear() {
  searchQuery.value = ''
  filteredRepositories.value = repositories
}

const tag = Tags.find(t => t.slug === route.params.slug)

useHead({
  title: `${tag.language} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
  }]
})
</script>
