<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />

    <p v-if="repositories.length === 0" class="text-center text-vanilla-400 py-8">
      No repositories found for {{ tag.language }}.
    </p>
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const tag = Tags.find((t) => t.slug === route.params.slug)

if (!tag) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Language not found'
  })
}

const repositories = Repositories.filter((repository) => repository.slug === tag.slug)

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
