<template>
  <div class="p-4 w-full">
    <!-- Search bar -->
    <input
      type="text"
      v-model="searchQuery"
      placeholder="Search projects..."
      class="search-input"
    />

    <label for="min-stars" class="mt-4">Minimum Stars:</label>
    <input
      type="number"
      id="min-stars"
      v-model="minStars"
      class="stars-input"
      placeholder="0"
    />

    <!-- Repositories list -->
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>


<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const repositories = Repositories.filter(repository => repository.slug === route.params.slug)

const tag = Tags.find(t => t.slug === route.params.slug)

const searchQuery = ref('')
const minStars = ref(0)

// Computed property to filter repositories
const filteredRepositories = computed(() => {
  return repositories.filter(repo => {
    const matchesSearchQuery = repo.name.toLowerCase().includes(searchQuery.value.toLowerCase())
    const hasMinStars = repo.stars >= minStars.value // Assuming the repo data has a 'stars' field
    return matchesSearchQuery && hasMinStars
  })
})

useHead({
  title: `${tag.language} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
  }]
})
</script>

<style scoped>
.search-input {
  padding: 10px;
  margin-bottom: 20px;
  width: 100%;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  color: teal;
}
.stars-input {
  padding: 5px;
  margin-bottom: 20px;
  width: 100%;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  color: teal;
}
</style>

