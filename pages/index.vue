<template>
  <div class="p-4 w-full">
    <!-- Filter Controls -->
    <div class="mb-6 p-4 bg-ink-200 rounded-lg">
      <h3 class="text-lg font-semibold mb-4">Filter Repositories</h3>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Minimum Stars Filter -->
        <div>
          <label class="block text-sm font-medium mb-2">
            Minimum Stars: <span class="font-mono">{{ minStars }}</span>
          </label>
          <input 
            v-model.number="minStars" 
            type="range" 
            min="0" 
            max="10000" 
            step="100"
            class="w-full"
          >
        </div>
        
        <!-- Maximum Last Activity Filter -->
        <div>
          <label class="block text-sm font-medium mb-2">
            Maximum Days Since Last Activity: <span class="font-mono">{{ maxDaysSinceActivity }}</span>
          </label>
          <input 
            v-model.number="maxDaysSinceActivity" 
            type="range" 
            min="1" 
            max="365" 
            step="1"
            class="w-full"
          >
        </div>
        
        <!-- Reset Filters -->
        <div class="flex items-end">
          <button 
            @click="resetFilters"
            class="w-full px-4 py-2 bg-juniper text-white rounded hover:bg-juniper-dark transition-colors"
          >
            Reset Filters
          </button>
        </div>
      </div>
      
      <!-- Active Filters Display -->
      <div class="mt-4 text-sm text-gray-600">
        <span>Showing {{ filteredRepositories.length }} of {{ Repositories.length }} repositories</span>
      </div>
    </div>

    <!-- Repository List -->
    <RepoBox 
      v-for="repo in filteredRepositories" 
      :key="repo.id" 
      :repo="repo" 
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'
import dayjs from 'dayjs'

const minStars = ref(0)
const maxDaysSinceActivity = ref(365)

// Filter repositories based on criteria
const filteredRepositories = computed(() => {
  return Repositories.filter(repo => {
    // Filter by minimum stars
    const meetsStarRequirement = repo.stars >= minStars.value
    
    // Filter by last activity
    const lastModifiedDate = dayjs(repo.last_modified)
    const daysSinceActivity = dayjs().diff(lastModifiedDate, 'day')
    const meetsActivityRequirement = daysSinceActivity <= maxDaysSinceActivity.value
    
    return meetsStarRequirement && meetsActivityRequirement
  })
})

// Reset all filters to default values
function resetFilters() {
  minStars.value = 0
  maxDaysSinceActivity.value = 365
}

useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
  {
    name: 'description',
    content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
  }
  ]
})
</script>
