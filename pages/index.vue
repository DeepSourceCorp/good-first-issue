<template>
  <div class="p-4 w-full">
    <!-- 🔍 Search Input -->
    <input
      v-model="searchQuery"
      placeholder="Search by name, description, or tags..."
      class="border p-3 w-full mb-6 rounded-lg shadow-sm 
             focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400
             text-black bg-white placeholder-gray-400 
             dark:text-white dark:bg-gray-800"
    />

    <!-- 📦 Repository List -->
    <RepoBox
      v-for="repo in filteredRepositories"
      :key="repo.id"
      :repo="repo"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'

const searchQuery = ref('')

/* 🔍 Filter logic */
const filteredRepositories = computed(() => {
  if (!searchQuery.value) return Repositories

  const query = searchQuery.value.toLowerCase()

  return Repositories.filter(repo =>
    repo.name?.toLowerCase().includes(query) ||
    repo.description?.toLowerCase().includes(query) ||
    repo.tags?.join(" ").toLowerCase().includes(query)
  )
})

/* 🌐 SEO */
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