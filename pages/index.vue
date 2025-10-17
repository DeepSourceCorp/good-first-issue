<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in Repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const Repositories = ref([])
try {
  const mod = await import('~/data/generated.json')
  Repositories.value = mod.default || mod
} catch (err) {
  // fallback to sample data to avoid build errors
  try {
    const sample = await import('~/data/generated.sample.json')
    Repositories.value = sample.default || sample
  } catch (e) {
    Repositories.value = []
    console.warn('No generated data found; page will be empty.')
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
