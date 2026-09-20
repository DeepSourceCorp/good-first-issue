<template>
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center flex-wrap">
      <NuxtLink to="/" class="flex items-center text-gray-700 font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
      </NuxtLink>
      <span v-if="activeTags.length" class="text-2xl cursor-pointer">
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTags.map((tag) => tag.language).join(', ') }}</span>
      </span>
    </nav>
  </header>
</template>

<script setup>
import Tags from '~/data/tags.json'

const route = useRoute()

const activeTags = computed(() => {
  const queryLanguages = route.query.languages
  const languages = typeof queryLanguages === 'string' ? queryLanguages.split(',') : []
  const routeLanguage = typeof route.params.slug === 'string' ? route.params.slug : ''
  const selectedSlugs = [...new Set([routeLanguage, ...languages].filter(Boolean))]

  return Tags.filter((tag) => selectedSlugs.includes(tag.slug))
})
</script>
