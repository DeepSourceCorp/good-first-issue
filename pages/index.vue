<template>
  <div class="p-4 w-full">
    <!-- Search Bar -->
    <input
      type="text"
      v-model="searchQuery"
      placeholder="Search repositories..."
      class="search-bar"
    />

    <!-- Display Filtered Repositories -->
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'

// Reactive variable for search input
const searchQuery = ref('')

// Computed property to filter repositories based on search
const filteredRepositories = computed(() => {
  return Repositories.filter(repo =>
    repo.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

// Set page metadata
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

<style scoped>
.search-bar {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
