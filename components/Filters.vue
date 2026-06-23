<template>
  <div class="flex flex-col sm:flex-row space-y-3 sm:space-y-0 sm:space-x-6 mb-6 p-4 bg-ink-300 rounded-md border border-ink-200 text-sm">
    <div class="flex items-center space-x-2">
      <label for="filter-stars" class="text-vanilla-400 font-semibold tracking-wide">Min Stars:</label>
      <select
        id="filter-stars"
        v-model="minStars"
        class="bg-ink-400 border border-ink-200 text-vanilla-300 rounded px-3 py-1.5 focus:outline-none focus:border-juniper font-mono cursor-pointer transition-colors duration-200"
      >
        <option :value="0">All</option>
        <option :value="100">100+</option>
        <option :value="500">500+</option>
        <option :value="1000">1,000+</option>
        <option :value="5000">5,000+</option>
        <option :value="10000">10,000+</option>
      </select>
    </div>
    <div class="flex items-center space-x-2">
      <label for="filter-activity" class="text-vanilla-400 font-semibold tracking-wide">Last Activity:</label>
      <select
        id="filter-activity"
        v-model="activityDays"
        class="bg-ink-400 border border-ink-200 text-vanilla-300 rounded px-3 py-1.5 focus:outline-none focus:border-juniper font-mono cursor-pointer transition-colors duration-200"
      >
        <option value="all">Any time</option>
        <option :value="30">Within 30 days</option>
        <option :value="90">Within 3 months</option>
        <option :value="180">Within 6 months</option>
        <option :value="365">Within 1 year</option>
      </select>
    </div>
  </div>
</template>

<script setup>
const minStars = useFilterMinStars()
const activityDays = useFilterActivityDays()
</script>
