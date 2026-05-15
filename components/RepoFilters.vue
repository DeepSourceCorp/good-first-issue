<template>
  <div class="mb-4 grid gap-3 sm:grid-cols-2">
    <label class="text-sm font-semibold text-vanilla-300">
      Minimum stars
      <select v-model="filters.minStars" class="filter-select">
        <option v-for="option in starOptions" :key="option.value" :value="option.value">
          {{ option.label }}
        </option>
      </select>
    </label>

    <label class="text-sm font-semibold text-vanilla-300">
      Last activity
      <select v-model="filters.activityMonths" class="filter-select">
        <option v-for="option in activityOptions" :key="option.value" :value="option.value">
          {{ option.label }}
        </option>
      </select>
    </label>
  </div>
</template>

<script setup>
const emit = defineEmits(['change'])

const filters = reactive({
  minStars: 0,
  activityMonths: 'all'
})

const starOptions = [
  { label: 'Any', value: 0 },
  { label: '100+', value: 100 },
  { label: '500+', value: 500 },
  { label: '1,000+', value: 1000 },
  { label: '5,000+', value: 5000 },
  { label: '10,000+', value: 10000 }
]

const activityOptions = [
  { label: 'Any time', value: 'all' },
  { label: 'Past month', value: 1 },
  { label: 'Past 3 months', value: 3 },
  { label: 'Past 6 months', value: 6 },
  { label: 'Past year', value: 12 }
]

watch(
  filters,
  (currentFilters) => {
    emit('change', { ...currentFilters })
  },
  { deep: true, immediate: true }
)
</script>

<style scoped>
.filter-select {
  @apply mt-1 block w-full rounded-sm border border-ink-200 bg-ink-300 px-3 py-2 text-sm font-normal text-vanilla-300 outline-none focus:border-juniper;
}
</style>
