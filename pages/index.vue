<template>
  <div class="p-4 w-full">
    <h1 class="text-3xl font-bold mb-4">Welcome to Good First Issue 🚀 (Edited by Nishant)</h1>
    <RepoBox v-for="repo in Repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

useHead({
  title: 'Good First Issue 🚀: Make your first open-source contribution (Edited by Nishant)',
  meta: [
  {
    name: 'description',
    content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
  }
  ]
})
</script>
