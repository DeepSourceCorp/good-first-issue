<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.sample.json'

const route = useRoute()

const filteredRepositories = computed(() => {
  const tagsParam = route.query.tags

  if (!tagsParam) {
    return Repositories
  }

  const selected = Array.isArray(tagsParam)
    ? tagsParam.flatMap(t => t.split(',')).filter(Boolean)
    : tagsParam.split(',').filter(Boolean)

  if (!selected.length) {
    return Repositories
  }

  const selectedSet = new Set(selected)

  return Repositories.filter(repo => selectedSet.has(repo.slug))
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
