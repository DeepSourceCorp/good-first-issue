<template>
  <div class="p-4 w-full">
    <p v-if="repositories.length === 0" class="text-slate text-sm py-8 text-center">
      No repositories match the selected filters.
    </p>
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import AllRepositories from '~/data/generated.json'

const minStars = useMinStars()
const maxAgeDays = useMaxAgeDays()

const repositories = computed(() => {
  let repos = [...AllRepositories]

  if (minStars.value > 0) {
    repos = repos.filter(r => r.stars >= minStars.value)
  }

  if (maxAgeDays.value > 0) {
    const cutoff = Date.now() - maxAgeDays.value * 24 * 60 * 60 * 1000
    repos = repos.filter(r => new Date(r.last_modified).getTime() >= cutoff)
  }

  if (minStars.value > 0) {
    repos = [...repos].sort((a, b) => b.stars - a.stars)
  } else if (maxAgeDays.value > 0) {
    repos = [...repos].sort((a, b) => new Date(b.last_modified) - new Date(a.last_modified))
  }

  return repos
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
