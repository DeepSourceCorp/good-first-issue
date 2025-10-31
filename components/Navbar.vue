<template>
  <!-- Navbar Header -->
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center flex-wrap">
      <!-- App Logo and Home Link -->
      <NuxtLink to="/" class="flex items-center text-gray-700 font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
      </NuxtLink>

      <!-- Active Language Tag Display -->
      <span v-if="activeTag" class="text-2xl cursor-pointer">
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
    </nav>
  </header>
</template>

<script setup>
// Import available tags from JSON file
import Tags from '~/data/tags.json'

// Access the current route using Nuxt's useRoute composable
const route = useRoute()

// Compute which tag is currently active based on the route parameter
const activeTag = computed(() => {
  return Tags.find(tag => tag.slug === route.params.slug)
})
</script>
