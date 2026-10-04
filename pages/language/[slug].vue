<template>
  <div class="p-4 w-full">
    <div class="mb-4 flex items-center justify-end">
      <label for="sort" class="mr-2 text-sm text-vanilla-300">
        Sort by:
      </label>

      <select
        id="sort"
        v-model="sortBy"
        class="border border-ink-200 rounded-md px-3 py-2 bg-ink-300 text-vanilla-300"
      >
        <option value="default">Default</option>
        <option value="stars">Most Stars</option>
        <option value="updated">Recently Updated</option>
      </select>
    </div>

    <RepoBox
      v-for="repo in sortedRepositories"
      :key="repo.id"
      :repo="repo"
    />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const repositories = Repositories.filter(
  repository => repository.slug === route.params.slug
)

const sortBy = ref('default')

const sortedRepositories = computed(() => {
  const result = [...repositories]

  if (sortBy.value === 'stars') {
    return result.sort((a, b) => b.stars - a.stars)
  }

  if (sortBy.value === 'updated') {
    return result.sort(
      (a, b) => new Date(b.last_modified) - new Date(a.last_modified)
    )
  }

  return result
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