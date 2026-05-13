<template>
  <div class="p-4 w-full">
    <p v-if="filteredRepos.length === 0" class="text-vanilla-400 text-center py-12 text-lg">
      No repositories match the current filters. Try adjusting the minimum stars or activity window.
    </p>
    <RepoBox v-for="repo in filteredRepos" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

const filteredRepos = useFilteredRepos(Repositories)

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
