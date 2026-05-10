<template>
  <div class="p-4 w-full">
    <RepoList :repositories="repositories" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const tag = Tags.find(t => t.slug === route.params.slug)

if (!tag) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Language filter not found'
  })
}

const repositories = Repositories.filter(repository => repository.slug === route.params.slug)

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
