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
import Tags from '~/data/tags.json'

const route = useRoute()
const searchQuery = useSearchQuery()

const repositories = Repositories.filter((repository) => repository.slug === route.params.slug)

const filteredRepositories = computed(() => {
  if (!searchQuery.value) {
    return repositories
  }
  const query = searchQuery.value.toLowerCase().trim()
  return repositories.filter((repo) => {
    return (
      repo.name.toLowerCase().includes(query) ||
      repo.owner.toLowerCase().includes(query) ||
      (repo.description && repo.description.toLowerCase().includes(query)) ||
      (repo.language && repo.language.toLowerCase().includes(query))
    )
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
