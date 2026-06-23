<template>
  <div class="p-4 w-full">
    <Filters />
    <div v-if="filteredRepositories.length === 0" class="text-center py-8 text-vanilla-400">
      No repositories match the selected filters.
    </div>
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import dayjs from 'dayjs'

const minStars = useFilterMinStars()
const activityDays = useFilterActivityDays()

const filteredRepositories = computed(() => {
  let repos = [...Repositories]

  // Filter by min stars
  if (minStars.value > 0) {
    repos = repos.filter(repo => repo.stars >= minStars.value)
  }

  // Filter by activity
  if (activityDays.value !== 'all') {
    const limitDate = dayjs().subtract(Number(activityDays.value), 'day')
    repos = repos.filter(repo => dayjs(repo.last_modified).isAfter(limitDate))
  }

  // Sort
  if (minStars.value > 0 && activityDays.value !== 'all') {
    repos.sort((a, b) => b.stars - a.stars || dayjs(b.last_modified).diff(dayjs(a.last_modified)))
  } else if (minStars.value > 0) {
    repos.sort((a, b) => b.stars - a.stars)
  } else if (activityDays.value !== 'all') {
    repos.sort((a, b) => dayjs(b.last_modified).diff(dayjs(a.last_modified)))
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
