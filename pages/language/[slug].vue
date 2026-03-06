<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
    <p v-if="filteredRepositories.length === 0" class="text-vanilla-400 text-center py-8">
      No repositories match the selected filters.
    </p>
  </div>
</template>

<script setup>
import dayjs from 'dayjs'
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const minStars = useMinStars()
const maxInactivityMonths = useMaxInactivityMonths()

const filteredRepositories = computed(() => {
  let repos = Repositories.filter((repo) => {
    if (repo.slug !== route.params.slug) {
      return false
    }
    if (minStars.value > 0 && repo.stars < minStars.value) {
      return false
    }
    if (maxInactivityMonths.value > 0) {
      const cutoff = dayjs().subtract(maxInactivityMonths.value, 'month')
      if (dayjs(repo.last_modified).isBefore(cutoff)) {
        return false
      }
    }
    return true
  })

  // Sort by stars (highest first) when star filter is active,
  // otherwise sort by last activity (most recent first) when activity filter is active
  if (minStars.value > 0) {
    repos = repos.slice().sort((a, b) => b.stars - a.stars)
  } else if (maxInactivityMonths.value > 0) {
    repos = repos.slice().sort((a, b) => dayjs(b.last_modified).unix() - dayjs(a.last_modified).unix())
  }

  return repos
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
