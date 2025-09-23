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
      <!-- Dark mode toggle button -->
      <button 
        @click="toggleDark" 
        class="ml-auto px-4 py-2 rounded bg-gray-300 dark:bg-gray-700 text-gray-800 dark:text-gray-200 hover:bg-gray-400 dark:hover:bg-gray-600 transition"
        aria-label="Toggle dark mode"
      >
        {{ isDark ? '🌙 Dark' : '☀️ Light' }}
      </button>
    </nav>
  </header>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Tags from '~/data/tags.json'

const route = useRoute()

const activeTag = computed(() => {
  return Tags.find(tag => tag.slug === route.params.slug)
})
const isDark = ref(false)

function toggleDark() {
  isDark.value = !isDark.value
  if (isDark.value) {
    document.documentElement.classList.add('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  }
}

// On component mount, set dark mode from localStorage if available
onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme === 'dark') {
    isDark.value = true
    document.documentElement.classList.add('dark')
  }
})
</script>
