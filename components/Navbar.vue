<template>
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center">
      <NuxtLink to="/" class="flex items-center font-bold text-gray-700">
        <img src="~/assets/gfi-logo-white.svg" alt="Logo" class="h-12" />
      </NuxtLink>
      <span v-if="activeTag" class="text-2xl cursor-pointer ml-2">
        / <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
    </nav>
  </header>
</template>

<script setup>
import Tags from '~/data/tags.json'

const route = useRoute()
const activeTag = computed(() => Tags.find(tag => tag.slug === route.params.slug))
</script>
