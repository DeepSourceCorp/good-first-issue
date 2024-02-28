<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in paginatedRepos" :key="repo.id" :repo="repo" />
    <Pagination
    :currentPage="currentPage"
    :totalPages="totalPages"
    @update:currentPage="currentPage = $event"
  />
  </div>
</template>

<script setup>
import Pagination from '../components/Pagination.vue'
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'

const currentPage = ref(1)
const itemsPerPage = 10
const totalPages = computed(() => Math.ceil(Repositories.length / itemsPerPage))

const paginatedRepos = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return Repositories.slice(start, end)
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
