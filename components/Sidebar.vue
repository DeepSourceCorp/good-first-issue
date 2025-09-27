<template>
  <aside
    class="masthead font-sans pt-6 border-r border-ink-200 px-6 text-vanilla-300 w-full md:max-w-sm flex-none bg-white dark:bg-gray-900 h-full overflow-y-auto"
  >
    <!-- About Section -->
    <div class="mb-8">
      <h3 class="section-heading">About</h3>
      <p class="text-sm leading-relaxed">
        Good First Issue curates easy pickings from popular open-source projects, and helps you make your first
        contribution to open-source.
      </p>
    </div>

    <!-- Browse by Language -->
    <div class="mb-8">
      <h3 class="section-heading">Browse by language</h3>
      <div class="flex flex-wrap">
        <nuxt-link
          v-for="tag in Tags"
          :key="tag.slug"
          :to="'/language/' + tag.slug"
          :class="[
            'group mx-1 my-1 px-3 py-1 rounded-full text-sm transition-colors duration-200 border',
            $route.params.slug === tag.slug
              ? 'active-pill'
              : 'border-gray-300 hover:border-juniper hover:text-juniper'
          ]"
        >
          {{ tag.language }}
          <span
            :class="{
              'ml-1 text-gray-400 group-hover:text-juniper': $route.params.slug !== tag.slug
            }"
          >&times; {{ tag.count }}</span>
        </nuxt-link>
      </div>
    </div>

    <!-- Add Project Button -->
    <div class="mb-8">
      <a
        class="bg-juniper hover:bg-light_juniper text-white uppercase rounded-md font-bold text-center px-3 py-2 flex items-center justify-center space-x-2 transition-all duration-200 transform hover:scale-105 shadow hover:shadow-lg"
        href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
        target="_blank"
        rel="noopener noreferrer"
      >
        <PlusCircleIcon class="h-5 w-5 stroke-2" />
        <span>Add your project</span>
      </a>
    </div>

    <!-- Footer / Attribution -->
    <div class="text-sm">
      <a
        class="flex items-center justify-center text-gray-500 hover:text-juniper transition-colors duration-200"
        target="_blank"
        rel="noopener noreferrer"
        href="https://deepsource.com?ref=gfi"
      >
        <HeartIcon class="w-4 h-4 text-cherry" />
        <span class="ml-2">
          A
          <span class="inline hover:underline text-juniper" title="Visit DeepSource website">DeepSource</span>
          initiative
        </span>
      </a>
    </div>
  </aside>
</template>

<script setup>
import Tags from '~/data/tags.json'
import { PlusCircleIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'
</script>

<style>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate-600 dark:text-gray-300;
}

.active-pill {
  @apply bg-juniper text-white font-semibold border-juniper shadow-md;
}

.active-pill > span {
  @apply text-white;
}
</style>
