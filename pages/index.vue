<template>
  <div class="p-4 w-full">
    <div class="mb-4 flex gap-2">
      <p>Fliter by:</p>
      <span
        v-for="option in sortOptions"
        :key="option.value"
        @click="selectedSort = option.value"
        class="cursor-pointer px-3 py-1 rounded-full font-mono border text-sm"
        :class="{
          'bg-juniper text-ink-400 border-transparent': selectedSort === option.value,
          'bg-ink-200 text-ink-600 border-ink-200 hover:bg-juniper hover:text-ink-400': selectedSort !== option.value
        }">
        {{ option.label }}
      </span>
    </div>
    <RepoBox v-for="repo in sortedRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'

useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
  {
    name: 'description',
    content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
  }
  ]
})

const sortOptions = [
  { value: 'date', label: 'Last activity' },
  { value: 'issues', label: 'Number of issues' }
]

const selectedSort = ref('date')

const sortedRepositories = computed(() => {
  if (selectedSort.value === 'issues') {
    return [...Repositories].sort((a, b) => b.issues.length - a.issues.length)
  }
  return [...Repositories].sort((a, b) => new Date(b.last_modified) - new Date(a.last_modified))
})
</script>
