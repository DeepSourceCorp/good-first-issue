<template>
  <div class="p-4 w-full">
    <!-- Search Bar -->
    <input
      v-model="searchQuery"
      type="text"
      placeholder="Search repositories..."
      class="mb-4 p-2 border border-gray-300 rounded w-full focus:outline-none focus:ring-2 focus:ring-blue-400"
    />
    <!-- Repo List -->
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'

const searchQuery = ref('')

const filteredRepositories = computed(() => {
  if (!searchQuery.value) return Repositories
  const q = searchQuery.value.toLowerCase()
  return Repositories.filter(repo =>
    repo.name.toLowerCase().includes(q) ||
    repo.owner.toLowerCase().includes(q) ||
    (repo.description && repo.description.toLowerCase().includes(q))
  )
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
