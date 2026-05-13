<template>
  <section class="masthead font-sans pt-6 border-r border-ink-200 px-6 text-vanilla-300 flex-none w-full md:max-w-sm">
    <div>
      <h3 class="section-heading">About</h3>
      <p class="text-sm">
        Good First Issue curates easy pickings from popular open-source projects, and helps you make your first
        contribution to open-source.
      </p>
    </div>

    <!-- Minimum Stars Filter -->
    <div class="pt-6">
      <h3 class="section-heading">Minimum Stars</h3>
      <div class="flex flex-col gap-2">
        <input
          id="min-stars-slider"
          v-model.number="minStars"
          type="range"
          :min="0"
          :max="10000"
          :step="100"
          class="filter-range w-full"
        />
        <div class="flex justify-between items-center text-xs font-mono text-vanilla-400">
          <span>0</span>
          <span class="text-juniper font-semibold text-sm">{{ minStarsLabel }}</span>
          <span>10K</span>
        </div>
      </div>
    </div>

    <!-- Activity Filter -->
    <div class="pt-6">
      <h3 class="section-heading">Recent Activity</h3>
      <div class="flex flex-wrap gap-1">
        <button
          v-for="option in activityOptions"
          :key="option.value"
          :id="`activity-${option.value}`"
          :class="{
            'active-pill border-juniper': activityFilter === option.value,
            'border-slate hover:text-juniper hover:border-juniper': activityFilter !== option.value
          }"
          class="border px-3 py-1 rounded-sm text-sm cursor-pointer transition-colors duration-150"
          @click="activityFilter = option.value"
        >{{ option.label }}</button>
      </div>
    </div>

    <div class="pt-6">
      <h3 class="section-heading">Browse by language</h3>
      <div>
        <nuxt-link
          v-for="tag in Tags"
          :key="tag.slug"
          :to="'/language/' + tag.slug"
          :class="{
            'active-pill': $route.params.slug === tag.slug,
            'border-slate hover:text-juniper hover:border-juniper': $route.params.slug !== tag.slug
          }"
          class="group mx-1 border px-2 py-1 inline-block rounded-sm my-1 text-sm"
          >{{ tag.language }}
          <span
            :class="{
              'text-vanilla-400 group-hover:text-juniper': $route.params.slug !== tag.slug
            }"
            >&times; {{ tag.count }}</span
          ></nuxt-link
        >
      </div>
    </div>
    <div class="pt-6">
      <a
        class="bg-juniper hover:bg-light_juniper text-ink-400 uppercase rounded-md font-bold text-center px-1 py-3 flex flex-row items-center justify-center space-x-1"
        href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
        target="_blank"
        rel="noopener noreferrer"
        >
          <PlusCircleIcon class="h-5 w-5 stroke-2" />
          <span>Add your project</span>
        </a
      >
    </div>

    <div class="text-sm pt-6">
      <a
        class="flex flex-row justify-center items-center"
        target="_blank"
        rel="noopener noreferrer"
        href="https://deepsource.com?ref=gfi"
      >
        <HeartIcon class="w-4 h-4 text-cherry" />
        <span class="ml-2"
          >A
          <span class="inline hover:underline text-juniper" title="Visit DeepSource website">DeepSource</span>
          initative</span
        >
      </a>
    </div>
  </section>
</template>

<script setup>
import Tags from '~/data/tags.json'
import { PlusCircleIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'

const minStars = useMinStars()
const activityFilter = useActivityFilter()

const activityOptions = [
  { value: 'all', label: 'All time' },
  { value: '1m', label: 'Last month' },
  { value: '6m', label: 'Last 6 months' },
  { value: '1y', label: 'Last year' }
]

const minStarsLabel = computed(() => {
  if (minStars.value === 0) return 'Any'
  if (minStars.value >= 1000) return `≥ ${(minStars.value / 1000).toFixed(1)}K`
  return `≥ ${minStars.value}`
})
</script>
<style>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate;
}
.active-pill {
  @apply text-juniper font-semibold border-juniper;
}

.active-pill > span {
  @apply text-juniper;
}

/* Custom range slider styling */
.filter-range {
  -webkit-appearance: none;
  appearance: none;
  height: 6px;
  border-radius: 3px;
  background: #2c303a;
  outline: none;
  cursor: pointer;
}

.filter-range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #33cb9a;
  border: 2px solid #16181d;
  cursor: pointer;
  transition: box-shadow 0.15s ease;
}

.filter-range::-webkit-slider-thumb:hover {
  box-shadow: 0 0 0 4px rgba(51, 203, 154, 0.25);
}

.filter-range::-moz-range-thumb {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #33cb9a;
  border: 2px solid #16181d;
  cursor: pointer;
}

.filter-range::-moz-range-track {
  height: 6px;
  border-radius: 3px;
  background: #2c303a;
}
</style>
