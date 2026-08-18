<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
    <div v-if="filteredRepositories.length === 0" class="text-center py-8 text-vanilla-400">
      No repositories found matching "{{ searchQuery }}".
    </div>
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

const searchQuery = useSearchQuery()

const filteredRepositories = computed(() => {
  if (!searchQuery.value) {
    return Repositories
  }
  const query = searchQuery.value.toLowerCase().trim()
  return Repositories.filter((repo) => {
    return (
      repo.name.toLowerCase().includes(query) ||
      repo.owner.toLowerCase().includes(query) ||
      (repo.description && repo.description.toLowerCase().includes(query)) ||
      (repo.language && repo.language.toLowerCase().includes(query))
    )
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
