<template>
  <section class="masthead font-sans pt-6 border-r border-ink-200 px-6 text-vanilla-300 flex-none w-full md:max-w-sm">
    <div>
      <h3 class="section-heading">About</h3>
      <p class="text-sm">
        Good First Issue curates easy pickings from popular open-source projects, and helps you make your first
        contribution to open-source.
      </p>
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
        >
          {{ tag.language }}
          <span
            :class="{
              'text-vanilla-400 group-hover:text-juniper': $route.params.slug !== tag.slug
            }"
          >
            &times; {{ tag.count }}
          </span>
        </nuxt-link>
      </div>
    </div>

    <!-- ✅ ADDED FILTER SECTION (no existing code touched) -->
    <div v-if="$route.params.slug" class="pt-6">
      <h3 class="section-heading">Filter repositories</h3>

      <!-- Minimum Stars -->
      <div class="mb-5">
        <div class="flex justify-between items-center mb-1">
          <label class="text-xs font-semibold uppercase tracking-wider text-slate">
            Minimum Stars
          </label>
          <span class="text-xs font-mono text-juniper font-semibold">
            {{ minStarsDisplay }}
          </span>
        </div>

        <input
          v-model.number="minStars"
          type="range"
          min="0"
          max="50000"
          step="500"
          class="w-full accent-juniper cursor-pointer"
        />

        <div class="flex justify-between text-xs text-vanilla-400 font-mono mt-0.5">
          <span>Any</span>
          <span>50K+</span>
        </div>
      </div>

      <!-- Last Activity -->
      <div class="mb-4">
        <label class="text-xs font-semibold uppercase tracking-wider text-slate">
          Last Activity
        </label>

        <select
          v-model.number="maxMonths"
          class="w-full bg-ink-300 border border-ink-200 text-vanilla-300 text-sm rounded-md px-3 py-1.5 focus:outline-none focus:border-juniper"
        >
          <option :value="0">Any time</option>
          <option :value="1">Last month</option>
          <option :value="3">Last 3 months</option>
          <option :value="6">Last 6 months</option>
          <option :value="12">Last year</option>
          <option :value="24">Last 2 years</option>
        </select>
      </div>

      <!-- Reset -->
      <button
        v-if="minStars > 0 || maxMonths > 0"
        @click="resetFilters"
        class="text-xs text-vanilla-400 hover:text-juniper underline underline-offset-2"
      >
        Reset filters
      </button>
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
      </a>
    </div>

    <div class="text-sm pt-6">
      <a
        class="flex flex-row justify-center items-center"
        target="_blank"
        rel="noopener noreferrer"
        href="https://deepsource.com?ref=gfi"
      >
        <HeartIcon class="w-4 h-4 text-cherry" />
        <span class="ml-2">
          A
          <span class="inline hover:underline text-juniper">DeepSource</span>
          initative
        </span>
      </a>
    </div>
  </section>
</template>

<script setup>
import Tags from '~/data/tags.json'
import { PlusCircleIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'

const minStars = useMinStars()
const maxMonths = useMaxMonths()

const minStarsDisplay = computed(() => {
  if (minStars.value === 0) return 'Any'
  if (minStars.value >= 1000) return `${(minStars.value / 1000).toFixed(1)}K+`
  return `${minStars.value}+`
})

function resetFilters() {
  minStars.value = 0
  maxMonths.value = 0
}
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
</style>