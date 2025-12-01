<template>
  <header
    class="w-full py-4 px-6 border-b border-vanilla-300 dark:border-ink-200 transition-all duration-1000"
    :class="[`${bannerActive ? 'bg-robin' : 'bg-vanilla-200 dark:bg-ink-300'}`]"
  >
    <span class="flex items-center justify-center flex-wrap text-sm font-medium">
      <span class="md:flex items-center">
        <slot></slot>
      </span>
    </span>
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const BANNER_ACTIVE_TIME = 2000
const bannerActive = ref(true)

onMounted(() => {
  setTimeout(() => {
    bannerActive.value = false
  }, BANNER_ACTIVE_TIME)
})
</script>
