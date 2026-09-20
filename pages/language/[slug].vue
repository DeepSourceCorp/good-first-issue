<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const selectedSlugs = computed(() => {
  const queryLanguages = route.query.languages
  const languages = typeof queryLanguages === 'string' ? queryLanguages.split(',') : []
  const routeLanguage = typeof route.params.slug === 'string' ? route.params.slug : ''

  return [...new Set([routeLanguage, ...languages].filter(Boolean))]
})

const repositories = computed(() => {
  return Repositories.filter(repository => selectedSlugs.value.includes(repository.slug))
})

const selectedTags = computed(() => Tags.filter(tag => selectedSlugs.value.includes(tag.slug)))
const languageNames = computed(() => selectedTags.value.map(tag => tag.language).join(', '))

useHead({
  title: `${languageNames.value} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${languageNames.value} from popular open-source projects that you can easily fix.`
  }]
})
</script>
