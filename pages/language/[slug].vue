<template>
  <div class="p-4 w-full">
    <div class="mb-4 flex flex-col md:flex-row md:items-end gap-3">
      <label class="text-sm text-vanilla-400">
        Minimum stars
        <select v-model.number="minimumStars" class="ml-2 bg-ink-300 border border-ink-200 rounded px-2 py-1 text-vanilla-200">
          <option v-for="starsOption in minimumStarsOptions" :key="starsOption" :value="starsOption">
            {{ starsOption }}
          </option>
        </select>
      </label>
      <label class="text-sm text-vanilla-400">
        Recent activity
        <select v-model.number="activityMonths" class="ml-2 bg-ink-300 border border-ink-200 rounded px-2 py-1 text-vanilla-200">
          <option v-for="activityOption in activityOptions" :key="activityOption.value" :value="activityOption.value">
            {{ activityOption.label }}
          </option>
        </select>
      </label>
    </div>

    <p class="text-sm text-vanilla-400 mb-4">
      Showing {{ filteredRepositories.length }} of {{ totalRepositories }}
    </p>

    <p v-if="filteredRepositories.length === 0" class="text-sm border border-ink-200 rounded-md p-4">
      No repositories match the selected filters.
    </p>

    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'
import { filterAndSortRepositories } from '~/utils/repoFilters'

const route = useRoute()

const minimumStarsOptions = [0, 50, 100, 500, 1000, 5000]

const activityOptions = [
  { label: 'Any', value: 0 },
  { label: '1 month', value: 1 },
  { label: '3 months', value: 3 },
  { label: '6 months', value: 6 },
  { label: '12 months', value: 12 }
]

const minimumStars = ref(0)
const activityMonths = ref(0)

const tag = computed(() => Tags.find(t => t.slug === route.params.slug))

const totalRepositories = computed(() => {
  return Repositories.filter(repository => repository.slug === route.params.slug).length
})

const filteredRepositories = computed(() => {
  // Ordering rule: stars desc, then last_modified desc.
  return filterAndSortRepositories(Repositories, {
    slug: route.params.slug,
    minStars: minimumStars.value,
    activityMonths: activityMonths.value
  })
})

useHead(() => {
  const language = tag.value?.language || 'Language'

  return {
    title: `${language} | Good First Issue`,
    meta: [{
      name: 'description',
      content: `Curated list of issues in ${language} from popular open-source projects that you can easily fix.`
    }]
  }
})
</script>
