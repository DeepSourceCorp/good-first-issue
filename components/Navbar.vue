<template>
  <header class="w-full py-4 px-4 border-b border-ink-200 bg-ink-400">
    <nav
      aria-label="Primary navigation"
      class="max-w-7xl mx-auto flex items-center justify-center flex-wrap gap-1"
    >
      <NuxtLink
        to="/"
        aria-label="Good First Issue home"
        class="inline-flex items-center rounded focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper"
      >
        <img
          src="~/assets/gfi-logo-white.svg"
          alt="Good First Issue"
          class="h-12 w-auto"
        />
      </NuxtLink>

      <NuxtLink
        v-if="activeTag"
        :to="`/language/${activeTag.slug}`"
        aria-current="page"
        class="inline-flex items-center text-xl sm:text-2xl rounded px-1.5 py-0.5 hover:bg-ink-300/60 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper"
      >
        <span class="font-normal mr-2 text-slate select-none" aria-hidden="true">/</span>
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