<template>
<div class="pt-24 md:pt-24 ml-[384px]"></div>
  <div class="4 w-full">
    <RepoBox v-for="repo in Repositories" :key="repo.id" :repo="repo" />
  </div>
</div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

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
