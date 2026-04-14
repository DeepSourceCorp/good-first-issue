<template>
  <div class="p-4 w-full">
    <template v-if="repositories.length">
      <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
    </template>
    <p v-else class="text-vanilla-400 text-center py-8">No repositories found for this language.</p>
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const repositories = Repositories.filter(repository => repository.slug === route.params.slug)

const tag = Tags.find(t => t.slug === route.params.slug)

if (tag) {
  useHead({
    title: ${tag.language} | Good First Issue,
    meta: [{
      name: 'description',
      content: Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.
    }]
  })
}
</script>
