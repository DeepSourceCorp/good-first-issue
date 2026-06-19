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
import { filterAndSortRepositories } from '~/utils/repoFilters'

const route = useRoute()

const filters = ref({
  minStars: 0,
  activityMonths: 'all'
})

const repositories = computed(() => {
  return filterAndSortRepositories(Repositories, {
    ...filters.value,
    slug: route.params.slug
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
