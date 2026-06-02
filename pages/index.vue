<template>
  <div class="p-4 w-full">
    <div v-if="Repositories.length === 0" class="text-center py-16 text-vanilla-400">
      <p class="text-lg">No repositories available at the moment.</p>
      <p class="text-sm mt-2">Check back later for updates.</p>
    </div>
    <RepoBox v-for="repo in Repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
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
</script>
