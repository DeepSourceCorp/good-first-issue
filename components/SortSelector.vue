<template>
  <div ref="dropdownRef" class="relative inline-block text-left mb-6 font-sans">
    <div class="flex items-center space-x-2">
      <span class="text-sm font-bold uppercase tracking-wider text-slate">Sort By:</span>
      <button
        type="button"
        class="inline-flex items-center justify-between w-56 rounded-md border border-ink-200 bg-ink-300 px-4 py-2 text-sm font-medium text-vanilla-300 hover:bg-ink-200 hover:text-juniper hover:border-juniper/50 focus:outline-none transition-all duration-200"
        @click="isOpen = !isOpen"
      >
        <span class="flex items-center space-x-2">
          <component :is="selectedOption.icon" class="h-4 w-4 text-vanilla-400" />
          <span>{{ selectedOption.label }}</span>
        </span>
        <ChevronDownIcon class="ml-2 -mr-1 h-4 w-4 transition-transform duration-200" :class="{ 'transform rotate-180': isOpen }" />
      </button>
    </div>

    <transition
      enter-active-class="transition ease-out duration-100"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div
        v-if="isOpen"
        class="absolute left-16 z-20 mt-2 w-56 origin-top-left rounded-md bg-ink-300 border border-ink-200 shadow-xl ring-1 ring-black ring-opacity-5 focus:outline-none overflow-hidden"
      >
        <div class="py-1">
          <button
            v-for="option in options"
            :key="option.key"
            class="flex items-center w-full px-4 py-2.5 text-sm transition-colors duration-150 text-left"
            :class="[
              sortKey === option.key
                ? 'bg-ink-200 text-juniper font-semibold'
                : 'text-vanilla-300 hover:bg-ink-100 hover:text-juniper'
            ]"
            @click="selectOption(option.key)"
          >
            <component :is="option.icon" class="mr-3 h-4 w-4" :class="[sortKey === option.key ? 'text-juniper' : 'text-vanilla-400']" />
            {{ option.label }}
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import {
  ChevronDownIcon,
  StarIcon,
  ClockIcon,
  ExclamationCircleIcon,
  ArrowPathIcon
} from '@heroicons/vue/24/outline'

const sortKey = useSortKey()
const isOpen = ref(false)
const dropdownRef = ref(null)

const options = [
  { key: 'random', label: 'Default (Random)', icon: ArrowPathIcon },
  { key: 'activity-desc', label: 'Recently Active', icon: ClockIcon },
  { key: 'stars-desc', label: 'Stars: High to Low', icon: StarIcon },
  { key: 'stars-asc', label: 'Stars: Low to High', icon: StarIcon },
  { key: 'issues-desc', label: 'Most Issues', icon: ExclamationCircleIcon }
]

const selectedOption = computed(() => {
  return options.find(o => o.key === sortKey.value) || options[0]
})

function selectOption(key) {
  sortKey.value = key
  isOpen.value = false
}

function handleClickOutside(event) {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    isOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>
