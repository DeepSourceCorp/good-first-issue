<template>
  <header
    role="banner"
    aria-live="polite"
    class="w-full py-4 px-6 border-b border-ink-200 transition-colors motion-reduce:transition-none duration-1000"
    :class="bannerActive ? 'bg-robin text-ink-400' : 'bg-ink-300 text-vanilla-300'"
  >
    <div class="max-w-7xl mx-auto flex items-center justify-center flex-wrap text-sm font-medium">
      <div class="md:flex items-center gap-2">
        <slot />
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const BANNER_ACTIVE_TIME = 2000
const bannerActive = ref(true)
let timeoutId = null

onMounted(() => {
  timeoutId = window.setTimeout(() => {
    bannerActive.value = false
  }, BANNER_ACTIVE_TIME)
})

onUnmounted(() => {
  if (timeoutId !== null) {
    window.clearTimeout(timeoutId)
  }
})
</script>