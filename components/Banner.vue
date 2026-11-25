<template>
  <header
    v-if="!isDismissed"
    role="banner"
    aria-live="polite"
    class="relative w-full py-3.5 px-4 sm:px-6 border-b border-ink-200 transition-colors motion-reduce:transition-none duration-1000"
    :class="
      isHighlighted
        ? 'bg-robin text-ink-400'
        : 'bg-ink-300 text-vanilla-300'
    "
    @mouseenter="pauseTimer"
    @mouseleave="resumeTimer"
    @focusin="pauseTimer"
    @focusout="resumeTimer"
  >
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-4 text-sm font-medium">
      <div class="flex flex-wrap items-center justify-center gap-x-2 gap-y-1 text-center md:text-left">
        <slot />
      </div>

      <button
        v-if="dismissible"
        type="button"
        aria-label="Dismiss announcement"
        class="shrink-0 rounded p-1 opacity-75 hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-current transition-opacity"
        @click="handleDismiss"
      >
        <XMarkIcon class="w-4 h-4" aria-hidden="true" />
      </button>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { XMarkIcon } from '@heroicons/vue/20/solid'

interface Props {
  activeDuration?: number
  dismissible?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  activeDuration: 2000,
  dismissible: false
})

const emit = defineEmits<{
  dismiss: []
}>()

const isHighlighted = ref(true)
const isDismissed = ref(false)
const isPaused = ref(false)

let timeoutId: ReturnType<typeof setTimeout> | null = null
let remainingTime = props.activeDuration
let lastStartTime = 0

const clearTimer = () => {
  if (timeoutId !== null) {
    clearTimeout(timeoutId)
    timeoutId = null
  }
}

const scheduleFade = (duration: number) => {
  clearTimer()
  if (duration <= 0) {
    isHighlighted.value = false
    return
  }

  lastStartTime = Date.now()
  timeoutId = setTimeout(() => {
    isHighlighted.value = false
    remainingTime = 0
  }, duration)
}

const pauseTimer = () => {
  if (!isHighlighted.value || isPaused.value) return
  isPaused.value = true
  clearTimer()
  const elapsed = Date.now() - lastStartTime
  remainingTime = Math.max(0, remainingTime - elapsed)
}

const resumeTimer = () => {
  if (!isHighlighted.value || !isPaused.value) return
  isPaused.value = false
  if (remainingTime > 0) {
    scheduleFade(remainingTime)
  } else {
    isHighlighted.value = false
  }
}

const handleDismiss = () => {
  clearTimer()
  isDismissed.value = true
  emit('dismiss')
}

onMounted(() => {
  remainingTime = props.activeDuration
  scheduleFade(remainingTime)
})

onUnmounted(() => {
  clearTimer()
})
</script>