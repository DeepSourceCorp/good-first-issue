<template>
  <div class="p-4 w-full">
    <RepoFilters @change="filters = $event" />
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
    <p v-if="repositories.length === 0" class="py-8 text-center text-sm text-vanilla-400">
      No repositories match the selected filters.
    </p>
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

const filters = ref({
  minStars: 0,
  activityMonths: 'all'
})

const repositories = computed(() => {
  const minStars = Number(filters.value.minStars) || 0
  const activityCutoff = filters.value.activityMonths === 'all' ? null : new Date()

  if (activityCutoff) {
    activityCutoff.setMonth(activityCutoff.getMonth() - Number(filters.value.activityMonths))
  }

  const filteredRepositories = Repositories.filter((repository) => {
    const hasEnoughStars = (Number(repository.stars) || 0) >= minStars
    const isRecentEnough = activityCutoff
      ? new Date(repository.last_modified).getTime() >= activityCutoff.getTime()
      : true

    return hasEnoughStars && isRecentEnough
  })

  if (minStars === 0 && !activityCutoff) {
    return filteredRepositories
  }

  return filteredRepositories.sort((firstRepository, secondRepository) => {
    if (minStars > 0) {
      const starsDifference = (Number(secondRepository.stars) || 0) - (Number(firstRepository.stars) || 0)

      if (starsDifference !== 0) {
        return starsDifference
      }
    }

    if (activityCutoff) {
      return new Date(secondRepository.last_modified).getTime() - new Date(firstRepository.last_modified).getTime()
    }

    return 0
  })
})

useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
    {
      name: 'description',
      content:
        'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
    }
  ]
})
</script>
