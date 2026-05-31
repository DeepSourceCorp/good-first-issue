<template>
  <div class="p-4 w-full">

    <div class="flex gap-4 mb-6 px-4">
      <select
        v-model="minStars"
        class="bg-ink-300 text-white border border-ink-200 rounded px-3 py-2 text-sm cursor-pointer focus:outline-none"
      >
        <option :value="0">Any stars</option>
        <option :value="100">100+ stars</option>
        <option :value="1000">1,000+ stars</option>
        <option :value="10000">10,000+ stars</option>
      </select>

      <select
        v-model="maxMonthsAgo"
        class="bg-ink-300 text-white border border-ink-200 rounded px-3 py-2 text-sm cursor-pointer focus:outline-none"
      >
        <option :value="null">Any activity</option>
        <option :value="3">Last 3 months</option>
        <option :value="6">Last 6 months</option>
        <option :value="12">Last year</option>
      </select>
    </div>

    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const minStars = ref(0)
const maxMonthsAgo = ref(null)

const repositories = computed(() => {
  return Repositories.filter(repo => {

    if (repo.slug !== route.params.slug) return false

    if (minStars.value > 0 && repo.stars < minStars.value) return false

    if (maxMonthsAgo.value !== null) {
      const cutoff = new Date()
      cutoff.setMonth(cutoff.getMonth() - maxMonthsAgo.value)
      const lastModified = new Date(repo.last_modified)
      if (lastModified < cutoff) return false
    }

    return true
  })
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