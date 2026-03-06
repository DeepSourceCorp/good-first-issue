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
      <h3 class="section-heading">Filter by stars</h3>
      <select v-model.number="minStars" class="filter-select">
        <option :value="0">All</option>
        <option :value="100">100+</option>
        <option :value="500">500+</option>
        <option :value="1000">1K+</option>
        <option :value="5000">5K+</option>
        <option :value="10000">10K+</option>
      </select>
    </div>
    <div class="pt-4">
      <h3 class="section-heading">Filter by last activity</h3>
      <select v-model.number="maxInactivityMonths" class="filter-select">
        <option :value="0">All</option>
        <option :value="1">Last month</option>
        <option :value="3">Last 3 months</option>
        <option :value="6">Last 6 months</option>
        <option :value="12">Last year</option>
        <option :value="24">Last 2 years</option>
      </select>
    </div>
    <div v-if="isFilterActive" class="pt-4">
      <button
        class="w-full bg-ink-200 hover:bg-cherry text-vanilla-300 hover:text-ink-400 uppercase rounded-md font-bold text-center text-sm px-1 py-3 transition-colors"
        @click="clearFilters"
      >
        Clear filters
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
const maxInactivityMonths = useMaxInactivityMonths()
const router = useRouter()
const route = useRoute()

const isFilterActive = computed(() => {
  return minStars.value > 0 || maxInactivityMonths.value > 0 || route.params.slug
})

function clearFilters() {
  minStars.value = 0
  maxInactivityMonths.value = 0
  router.push('/')
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

.filter-select {
  @apply w-full bg-ink-300 border border-ink-200 text-vanilla-300 text-sm rounded-md px-3 py-2 cursor-pointer;
  @apply hover:border-juniper focus:border-juniper focus:outline-none;
}
</style>
