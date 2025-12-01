<template>
  <button
    @click="toggleTheme"
    class="p-2 rounded-md transition-colors duration-200 hover:bg-ink-200 dark:hover:bg-ink-200"
    :title="isDark ? 'Switch to light mode' : 'Switch to dark mode'"
  >
    <SunIcon v-if="isDark" class="w-5 h-5 text-vanilla-300" />
    <MoonIcon v-else class="w-5 h-5 text-ink-300" />
  </button>
</template>

<script setup>
import { SunIcon, MoonIcon } from '@heroicons/vue/24/outline'

const colorMode = useColorMode()

const isDark = computed(() => colorMode.value === 'dark')

function toggleTheme() {
  colorMode.preference = isDark.value ? 'light' : 'dark'
}
</script>
