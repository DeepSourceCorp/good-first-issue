<template>
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-between flex-wrap px-4">

      <div class="flex items-center">
        <button
          @click="isMenuOpen = !isMenuOpen"
          class="lg:hidden p-2 text-xl font-bold border rounded mr-2"
        >
          {{ isMenuOpen ? 'X' : '☰' }}
        </button>

        <NuxtLink to="/" class="flex items-center text-gray-700 font-bold">
          <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
        </NuxtLink>

        <span v-if="activeTag" class="text-2xl cursor-pointer ml-4">
          <span class="font-normal ml-2 mr-1 text-slate">/</span>
          <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
        </span>
      </div>

      <!-- Right-side visual toggle placed at the far right -->
      <div class="flex items-center">
        <button
          @click="handleToggle"
          class="group flex items-center ml-4"
          :aria-pressed="isDark"
          aria-label="Toggle theme"
        >
          <div :class="['w-12 h-6 rounded-full p-1 transition-colors duration-200', isDark ? 'bg-emerald-400' : 'bg-white/40']">
            <div :class="['bg-white w-4 h-4 rounded-full shadow transform transition-transform duration-200', isDark ? 'translate-x-6' : 'translate-x-0']"></div>
          </div>
        </button>
      </div>
    </nav>
  </header>
</template>

<script setup>
import Tags from '~/data/tags.json'
import { ref, computed } from 'vue'
import useTheme from '~/composables/useTheme'

const isMenuOpen = ref(false)

const { isDark, toggle } = useTheme()

const emit = defineEmits(['toggle'])

function handleToggle() {
  toggle()
  emit('toggle', isDark.value)
}

const route = useRoute()
const activeTag = computed(() => {
  return Tags.find(tag => tag.slug === route.params.slug)
})
</script>
