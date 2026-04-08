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
    <div v-if="$route.params.slug" class="pt-6">
      <h3 class="section-heading">Filter repositories</h3>
      <div class="mb-4">
        <label class="text-xs font-semibold text-slate uppercase mb-2 block">Minimum stars</label>
        <select
          v-model.number="starsFilter"
          class="w-full px-3 py-2 rounded-md bg-ink-400 text-vanilla-300 border border-ink-200 hover:border-juniper focus:outline-none focus:border-juniper"
        >
          <option :value="0">Any</option>
          <option :value="10">10+</option>
          <option :value="50">50+</option>
          <option :value="100">100+</option>
          <option :value="500">500+</option>
          <option :value="1000">1K+</option>
          <option :value="5000">5K+</option>
          <option :value="10000">10K+</option>
        </select>
      </div>
      <div>
        <label class="text-xs font-semibold text-slate uppercase mb-2 block">Last activity (months ago)</label>
        <select
          v-model.number="activityFilter"
          class="w-full px-3 py-2 rounded-md bg-ink-400 text-vanilla-300 border border-ink-200 hover:border-juniper focus:outline-none focus:border-juniper"
        >
          <option :value="null">Any</option>
          <option :value="1">Last month</option>
          <option :value="3">Last 3 months</option>
          <option :value="6">Last 6 months</option>
          <option :value="12">Last year</option>
        </select>
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
import {HeartIcon} from '@heroicons/vue/24/solid'

const starsFilter = useStarsFilter()
const activityFilter = useActivityFilter()
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
