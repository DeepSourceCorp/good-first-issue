<template>
  <header class="w-full py-4 px-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center flex-wrap gap-2">
      <NuxtLink to="/" class="flex items-center font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12 w-auto" />
      </NuxtLink>

      <NuxtLink
        v-if="activeTag"
        :to="`/language/${activeTag.slug}`"
        class="inline-flex items-center text-2xl hover:opacity-90 transition-opacity"
      >
        <span class="font-normal mx-2 text-slate select-none" aria-hidden="true">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </NuxtLink>
    </nav>
  </header>
</template>

<script setup>
import { computed } from 'vue'
import Tags from '~/data/tags.json'

const route = useRoute()

const activeTag = computed(() =>
  Tags.find((tag) => tag.slug === route.params.slug)
)
</script>