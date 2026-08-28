<template>
  <div class="p-4 w-full">
    <div class="mb-4 p-4 border border-ink-200 rounded-md grid gap-3 sm:grid-cols-3">
      <label class="text-sm">
        <span class="block mb-1 text-vanilla-400">Minimum stars</span>
        <select v-model.number="minimumStars" class="w-full bg-ink-400 border border-ink-200 rounded px-3 py-2">
          <option :value="0">Any</option>
          <option :value="100">100+</option>
          <option :value="1000">1,000+</option>
          <option :value="5000">5,000+</option>
          <option :value="10000">10,000+</option>
        </select>
      </label>
      <label class="text-sm">
        <span class="block mb-1 text-vanilla-400">Last activity</span>
        <select v-model.number="activityDays" class="w-full bg-ink-400 border border-ink-200 rounded px-3 py-2">
          <option :value="0">Any time</option>
          <option :value="30">Last 30 days</option>
          <option :value="90">Last 3 months</option>
          <option :value="180">Last 6 months</option>
        </select>
      </label>
      <label class="text-sm">
        <span class="block mb-1 text-vanilla-400">Sort by</span>
        <select v-model="sortBy" class="w-full bg-ink-400 border border-ink-200 rounded px-3 py-2">
          <option value="stars">Most stars</option>
          <option value="activity">Most recent activity</option>
        </select>
      </label>
    </div>
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
    <p v-if="repositories.length === 0" class="p-6 text-center text-vanilla-400">
      No repositories match these filters.
    </p>
  </div>
</template>

<script setup>
import dayjs from 'dayjs'
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()
const minimumStars = ref(0)
const activityDays = ref(0)
const sortBy = ref('stars')

const repositories = computed(() => {
  const activityCutoff = activityDays.value ? dayjs().subtract(activityDays.value, 'day') : null

  return Repositories.filter((repository) => (repository.slugs || [repository.slug]).includes(route.params.slug))
    .filter((repository) => repository.stars >= minimumStars.value)
    .filter((repository) => !activityCutoff || dayjs(repository.last_modified).isAfter(activityCutoff))
    .sort((left, right) => {
      if (sortBy.value === 'activity') {
        return dayjs(right.last_modified).valueOf() - dayjs(left.last_modified).valueOf()
      }
      return right.stars - left.stars
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
