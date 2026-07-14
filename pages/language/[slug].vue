<template>
  <div class="p-4 w-full">
    <SortSelector />
    <RepoBox v-for="repo in sortedRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()
const sortKey = useSortKey()

const repositories = computed(() => {
  return Repositories.filter(repository => repository.slug === route.params.slug)
})

const sortedRepositories = computed(() => {
  const list = [...repositories.value]
  if (sortKey.value === 'stars-desc') {
    return list.sort((a, b) => b.stars - a.stars)
  } else if (sortKey.value === 'stars-asc') {
    return list.sort((a, b) => a.stars - b.stars)
  } else if (sortKey.value === 'issues-desc') {
    return list.sort((a, b) => b.issues.length - a.issues.length)
  } else if (sortKey.value === 'activity-desc') {
    return list.sort((a, b) => new Date(b.last_modified) - new Date(a.last_modified))
  }
  return list
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
