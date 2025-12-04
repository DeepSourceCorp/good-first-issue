<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup lang="ts">
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const repositories = Repositories.filter(repository => repository.slug === route.params.slug)

const tag = Tags.find(t => t.slug === route.params.slug)

useHead({
  title: tag ? `${tag.language} | Good First Issue` : 'Good First Issue',
  meta: [{
    name: 'description',
    content: tag ? `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.` : 'Curated list of issues from popular open-source projects that you can easily fix.'
  }]
})
</script>
