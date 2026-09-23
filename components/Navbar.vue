<template>
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center flex-wrap">
      <NuxtLink to="/" class="flex items-center text-gray-700 font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
      </NuxtLink>
      <span v-if="activeTag" class="text-2xl cursor-pointer">
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
    </nav>
  </header>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const activeTag = computed(() => {
  if (!route.params.slug) return null
  const tag = Tags.find((t) => t.slug === route.params.slug)
  if (tag) return tag
  const repo = Repositories.find((r) => r.slug === route.params.slug)
  return repo ? { language: repo.language, slug: repo.slug } : null
})
</script>
