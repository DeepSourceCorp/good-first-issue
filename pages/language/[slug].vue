<template>
  <div class="p-4 w-full">
    <div v-if="repositories.length === 0" class="text-center py-8">
      <p class="text-vanilla-400">No repositories match the selected filters.</p>
    </div>
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'
import dayjs from 'dayjs'

const route = useRoute()
const starsFilter = useStarsFilter()
const activityFilter = useActivityFilter()

const repositories = computed(() => {
  let filtered = Repositories.filter(repository => repository.slug === route.params.slug)

  // Filter by minimum stars
  if (starsFilter.value > 0) {
    filtered = filtered.filter(repo => repo.stars >= starsFilter.value)
  }

  // Filter by last activity (in months)
  if (activityFilter.value !== null && activityFilter.value !== undefined) {
    const cutoffDate = dayjs().subtract(activityFilter.value, 'months')
    filtered = filtered.filter(repo => dayjs(repo.last_modified).isAfter(cutoffDate))
  }

  // Sort by stars (descending) as secondary sort
  return filtered.sort((a, b) => b.stars - a.stars)
})

const tag = Tags.find(t => t.slug === route.params.slug)

useHead({
  title: `${tag.language} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
  }]
})
</script>
