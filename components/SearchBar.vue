<template>
  <div class="w-full mb-4">
    <div class="relative">
      <MagnifyingGlassIcon class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-vanilla-400" />
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search repositories by name, description, or language..."
        class="w-full pl-10 pr-4 py-3 bg-ink-300 border border-ink-200 rounded-md text-vanilla-300 placeholder-vanilla-400 focus:outline-none focus:border-juniper focus:ring-1 focus:ring-juniper"
        aria-label="Search repositories"
        @input="handleSearch"
      />
      <button
        v-if="searchQuery"
        class="absolute right-3 top-1/2 transform -translate-y-1/2 text-vanilla-400 hover:text-juniper"
        aria-label="Clear search"
        @click="clearSearch"
      >
        <XMarkIcon class="w-5 h-5" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { MagnifyingGlassIcon, XMarkIcon } from '@heroicons/vue/24/outline'

const searchQuery = defineModel({ type: String, default: '' })

const emit = defineEmits(['search', 'clear'])

function handleSearch() {
  emit('search', searchQuery.value)
}

function clearSearch() {
  searchQuery.value = ''
  emit('clear')
}
</script>
