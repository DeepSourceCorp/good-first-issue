<template>
  <div class="p-4 w-full">
    <div v-if="!tag" class="text-center py-8">
      <h1 class="text-2xl font-bold text-vanilla-100 mb-4">Language Not Found</h1>
      <p class="text-vanilla-400 mb-6">Sorry, we don't have curated issues for "{{ slug }}" yet.</p>
      <NuxtLink to="/" class="text-juniper hover:underline">← Back to all languages</NuxtLink>
    </div>
    <div v-else-if="repositories.length === 0" class="text-center py-8">
      <h1 class="text-2xl font-bold text-vanilla-100 mb-4">No Projects Found</h1>
      <p class="text-vanilla-400 mb-6">No {{ tag.language }} projects with good first issues are available right now.</p>
      <NuxtLink to="/" class="text-juniper hover:underline">← Back to all languages</NuxtLink>
    </div>
    <div v-else>
      <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
    </div>
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()
const slug = route.params.slug

const repositories = Repositories.filter(repository => repository.slug === slug)

const tag = Tags.find(t => t.slug === slug)
const languageName = tag?.language ?? 'this language'

useHead({
  title: `${languageName} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${languageName} from popular open-source projects that you can easily fix.`
  }]
})
</script>
