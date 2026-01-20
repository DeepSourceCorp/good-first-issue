<template>
  <button
    @click="toggle"
    class="p-2 rounded-md transition
           bg-gray-200 dark:bg-gray-800
           text-gray-800 dark:text-gray-200"
    aria-label="Toggle Dark Mode"
  >
    <span v-if="colorMode.value === 'dark'">🌙</span>
    <span v-else>☀️</span>
  </button>
</template>

<script setup>
const colorMode = useColorMode()

const toggle = () => {
  colorMode.preference =
    colorMode.value === 'dark' ? 'light' : 'dark'
}
</script>
