<template>
  <div
    class="p-4 w-full min-h-screen
           bg-vanilla-100 dark:bg-ink-400
           text-ink-100 dark:text-vanilla-100
           transition-colors duration-200"
  >
    <RepoBox
      v-for="repo in Repositories"
      :key="repo.id"
      :repo="repo"
    />
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
