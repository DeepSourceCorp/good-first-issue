<template>
  <header
    class="w-full py-4 px-6 border-b border-ink-200 transition-colors duration-1000"
    :class="bannerActive ? 'bg-robin' : 'bg-ink-300'"
  >
    <div class="flex items-center justify-center flex-wrap text-sm font-medium">
      <div class="md:flex items-center">
        <slot />
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const BANNER_ACTIVE_TIME = 2000
const bannerActive = ref(true)
let timerId = null

onMounted(() => {
  timerId = setTimeout(() => {
    bannerActive.value = false
  }, BANNER_ACTIVE_TIME)
})

onUnmounted(() => {
  if (timerId) clearTimeout(timerId)
})
</script>