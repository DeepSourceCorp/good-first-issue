<template>
  <header
    v-if="!isDismissed"
    role="banner"
    aria-live="polite"
    :data-highlighted="isHighlighted ? 'true' : 'false'"
    class="relative w-full py-3.5 px-4 sm:px-6 border-b border-ink-200 transition-colors motion-reduce:transition-none duration-1000"
    :class="headerClasses"
    @mouseenter="pauseTimer"
    @mouseleave="resumeTimer"
    @focusin="pauseTimer"
    @focusout="resumeTimer"
  >
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4 text-sm font-medium">
      <div class="flex-1 flex flex-wrap items-center justify-center gap-x-2 gap-y-1 text-center md:text-left">
        <slot name="badge" :highlighted="isHighlighted" />
        <slot :highlighted="isHighlighted" />
      </div>

      <div class="flex items-center gap-2 shrink-0">
        <slot name="actions" />

        <button
          v-if="dismissible"
          type="button"
          :aria-label="dismissLabel"
          class="rounded p-1 text-current opacity-75 hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-current transition-opacity"
          @click="dismiss"
        >
          <XMarkIcon class="w-4 h-4" aria-hidden="true" />
        </button>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { XMarkIcon } from '@heroicons/vue/20/solid'

type BannerVariant = 'accent' | 'neutral'

interface Props {
  activeDuration?: number
  variant?: BannerVariant
  dismissible?: boolean
  dismissLabel?: string
  storageKey?: string
}

const props = withDefaults(defineProps<Props>(), {
  activeDuration: 2000,
  variant: 'accent',
  dismissible: false,
  dismissLabel: 'Close banner',
  storageKey: undefined
})

const emit = defineEmits<{
  dismiss: []
  highlightEnd: []
}>()

const isHighlighted = ref(true)
const isDismissed = ref(false)
const isPaused = ref(false)

let timeoutId: ReturnType<typeof setTimeout> | null = null
let remainingTime = props.activeDuration
let lastStartTime = 0

const headerClasses = computed(() => {
  if (isHighlighted.value && props.variant === 'accent') {
    return 'bg-robin text-ink-400'
  }
  return 'bg-ink-300 text-vanilla-300'
})

const clearTimer = () => {
  if (timeoutId !== null) {
    clearTimeout(timeoutId)
    timeoutId = null
  }
}

const finishHighlight = () => {
  clearTimer()
  remainingTime = 0
  isPaused.value = false
  if (isHighlighted.value) {
    isHighlighted.value = false
    emit('highlightEnd')
  }
}

const scheduleFade = (duration: number) => {
  clearTimer()
  if (duration <= 0) {
    finishHighlight()
    return
  }

  lastStartTime = Date.now()
  timeoutId = setTimeout(() => {
    finishHighlight()
  }, duration)
}

const replayHighlight = (duration = props.activeDuration) => {
  if (isDismissed.value) return
  remainingTime = duration
  isPaused.value = false
  isHighlighted.value = true
  scheduleFade(remainingTime)
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
    finishHighlight()
  }
}

const readDismissedState = (): boolean => {
  if (!props.storageKey || typeof window === 'undefined') return false
  try {
    return window.localStorage.getItem(props.storageKey) === 'dismissed'
  } catch {
    return false
  }
}

const writeDismissedState = () => {
  if (!props.storageKey || typeof window === 'undefined') return
  try {
    window.localStorage.setItem(props.storageKey, 'dismissed')
  } catch {
    // Ignora erros de armazenamento (ex.: modo privado restrito)
  }
}

const dismiss = () => {
  clearTimer()
  isDismissed.value = true
  writeDismissedState()
  emit('dismiss')
}

defineExpose({
  replayHighlight,
  dismiss
})

onMounted(() => {
  if (readDismissedState()) {
    isDismissed.value = true
    return
  }
  replayHighlight(props.activeDuration)
})

onUnmounted(() => {
  clearTimer()
})
</script>