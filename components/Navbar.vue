<template>
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center flex-wrap">
      <NuxtLink to="/" class="flex items-center text-gray-700 font-bold" aria-label="Go to homepage">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue Logo" class="h-12" />
      </NuxtLink>
      <span v-if="activeTag" class="text-2xl cursor-pointer">
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
    </nav>
  </header>
</template>

<script setup>
import Tags from '~/data/tags.json'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// Use computed to get the active tag based on the route params
const activeTag = computed(() => {
  return Tags.find(tag => tag.slug === route.params.slug)
})
</script>

<style scoped>
/* Adjust logo size and text size for small screens */
@media (max-width: 768px) {
  .h-12 {
    height: 8rem; /* Adjust logo size */
  }
  .text-2xl {
    font-size: 1.5rem; /* Adjust text size */
  }
}
</style>
