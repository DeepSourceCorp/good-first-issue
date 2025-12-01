<template>
  <header class="w-full py-4 border-b border-vanilla-300 dark:border-ink-200 bg-vanilla-100 dark:bg-ink-400 transition-colors duration-200">
    <nav class="flex items-center justify-center flex-wrap px-4">
      <NuxtLink to="/" class="flex items-center text-gray-700 font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12 dark:brightness-100 brightness-0" />
      </NuxtLink>
      <span v-if="activeTag" class="text-2xl cursor-pointer">
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
      <span class="flex-1"></span>
      <ThemeToggle />
    </nav>
  </header>
</template>

<script setup>
import Tags from '~/data/tags.json'

const route = useRoute()

const activeTag = computed(() => {
  return Tags.find(tag => tag.slug === route.params.slug)
})
</script>
