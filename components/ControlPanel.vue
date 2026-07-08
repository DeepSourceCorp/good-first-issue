<template>
  <div class="flex flex-col sm:flex-row space-y-3 sm:space-y-0 sm:space-x-4 mb-6 w-full">
    <!-- Search Input -->
    <div class="relative flex-grow">
      <span class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <MagnifyingGlassIcon class="w-5 h-5 text-vanilla-400" />
      </span>
      <input
        type="text"
        :value="searchQuery"
        @input="$emit('update:searchQuery', $event.target.value)"
        placeholder="Search projects by name or description..."
        class="bg-ink-300 border border-ink-200 text-vanilla-100 placeholder-vanilla-400 w-full h-11 pl-10 pr-4 rounded-md focus:border-juniper focus:outline-none transition-colors text-sm"
      />
    </div>
    <!-- Sort Dropdown -->
    <div class="relative w-full sm:w-56 flex-shrink-0">
      <select
        :value="sortBy"
        @change="$emit('update:sortBy', $event.target.value)"
        class="bg-ink-300 border border-ink-200 text-vanilla-100 w-full h-11 pl-4 pr-10 rounded-md focus:border-juniper focus:outline-none transition-colors appearance-none text-sm cursor-pointer"
      >
        <option value="default">Sort: Default</option>
        <option value="stars-desc">Stars: High to Low</option>
        <option value="stars-asc">Stars: Low to High</option>
        <option value="issues-desc">Issues: Most first</option>
        <option value="activity-desc">Activity: Recent first</option>
      </select>
      <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
        <ChevronDownIcon class="w-4 h-4 text-vanilla-400" />
      </span>
    </div>
  </div>
</template>

<script setup>
import { MagnifyingGlassIcon, ChevronDownIcon } from '@heroicons/vue/24/outline'

defineProps({
  searchQuery: {
    type: String,
    default: ''
  },
  sortBy: {
    type: String,
    default: 'default'
  }
})

defineEmits(['update:searchQuery', 'update:sortBy'])
</script>
