<template>
  <header class="w-full py-4 border-b border-slate/20 dark:border-ink-200 bg-vanilla-200 dark:bg-ink-400">
    <nav class="flex items-center justify-center flex-wrap relative">
      <NuxtLink to="/" class="flex items-center text-gray-700 font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
      </NuxtLink>
      <span v-if="activeTag" class="text-2xl cursor-pointer">
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
      <button 
        @click="toggleTheme" 
        class="absolute right-4 p-2 rounded-full hover:bg-ink-300 transition-colors"
        :title="theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'"
      >
        <SunIcon v-if="theme === 'dark'" class="h-5 w-5 text-vanilla-300" />
        <MoonIcon v-else class="h-5 w-5 text-vanilla-300" />
      </button>
    </nav>
  </header>
</template>

<script setup>
import Tags from '~/data/tags.json'
import { SunIcon, MoonIcon } from '@heroicons/vue/24/outline'
import { useTheme } from '~/composables/states'

const route = useRoute()
const theme = useTheme()

const activeTag = computed(() => {
  return Tags.find(tag => tag.slug === route.params.slug)
})

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark'
}
</script>
