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
import Tags from '~/data/tags.json'

const route = useRoute()

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
    const matchesLanguage = repository.slug === route.params.slug
    const hasEnoughStars = (Number(repository.stars) || 0) >= minStars
    const isRecentEnough = activityCutoff
      ? new Date(repository.last_modified).getTime() >= activityCutoff.getTime()
      : true

    return matchesLanguage && hasEnoughStars && isRecentEnough
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

const tag = Tags.find((t) => t.slug === route.params.slug)

useHead({
  title: `${tag.language} | Good First Issue`,
  meta: [
    {
      name: 'description',
      content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
    }
  ]
})
</script>
