<template>
  <div>
    <RepoBox 
      v-for="repo in paginatedRepos" 
      :key="repo.id" 
      :repo="repo" 
    />

    <div class="flex items-center justify-center gap-4 mt-8 mb-8">
      <button 
        @click="prevPage" 
        :disabled="currentPage === 1"
        class="px-4 py-2 bg-gray-800 text-white rounded disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-700"
      >
        Previous
      </button>

      <span class="text-white font-medium">
        Page {{ currentPage }} of {{ totalPages }}
      </span>

      <button 
        @click="nextPage" 
        :disabled="currentPage === totalPages"
        class="px-4 py-2 bg-gray-800 text-white rounded disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-700"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

import { ref, computed } from 'vue'


const currentPage = ref(1)
const itemsPerPage = 20

const totalPages = computed(() => {
  return Math.ceil(Repositories.length / itemsPerPage)
})

const paginatedRepos = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return Repositories.slice(start, end)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
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
