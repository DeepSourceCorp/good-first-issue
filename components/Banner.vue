<template>
  <header
    role="banner"
    aria-live="polite"
    class="w-full py-3.5 px-4 sm:px-6 border-b border-ink-200 transition-colors motion-reduce:transition-none duration-1000"
    :class="
      isHighlighted
        ? 'bg-robin text-ink-400'
        : 'bg-ink-300 text-vanilla-300'
    "
  >
    <div class="max-w-7xl mx-auto flex items-center justify-center text-sm font-medium">
      <div class="flex flex-wrap items-center justify-center gap-x-2 gap-y-1 text-center md:text-left">
        <slot />
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from 'vue'

interface Props {
  activeDuration?: number
  triggerKey?: string | number | boolean
}

const props = withDefaults(defineProps<Props>(), {
  activeDuration: 2000,
  triggerKey: true
})

const isHighlighted = ref(true)
let timeoutId: ReturnType<typeof setTimeout> | null = null

const clearTimer = () => {
  if (timeoutId !== null) {
    clearTimeout(timeoutId)
    timeoutId = null
  }
}

const startHighlight = () => {
  clearTimer()
  if (props.activeDuration <= 0) {
    isHighlighted.value = false
    return
  }

  isHighlighted.value = true
  timeoutId = setTimeout(() => {
    isHighlighted.value = false
  }, props.activeDuration)
}

watch(() => props.triggerKey, () => {
  startHighlight()
})

onMounted(() => {
  startHighlight()
})

onUnmounted(() => {
  clearTimer()
})
</script>