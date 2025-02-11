<template>
  <section class="masthead font-sans border-r border-ink-200 flex-none w-full md:max-w-sm bg-ink-900">
    <div class="h-full flex flex-col px-1 py-2 
    space-y-10">
      <!-- About section -->
      <div class="space-y-3">
        <h3 class="section-heading">About</h3>
        <p class="text-sm leading-relaxed text-vanilla-300">
          Good First Issue curates easy pickings from popular open-source projects, and helps you make your first
          contribution to open-source.
        </p>
      </div>

      <!-- Browse by language section -->
      <div class="space-y-4">
        <h3 class="section-heading">Browse by language</h3>
        <div class="flex flex-wrap gap-2">
          <nuxt-link
            v-for="tag in Tags"
            :key="tag.slug"
            :to="'/language/' + tag.slug"
            :class="{
              'active-pill': $route.params.slug === tag.slug,
              'hover:text-juniper hover:border-juniper': $route.params.slug !== tag.slug
            }"
            class="px-2 py-1.5 border rounded-md text-sm transition-colors duration-200 group"
          >
            {{ tag.language }}
            <span
              :class="{
                'text-vanilla-400 group-hover:text-juniper': $route.params.slug !== tag.slug
              }"
            >&times; {{ tag.count }}</span>
          </nuxt-link>
        </div>
      </div>

      <!-- Add project section -->
      <div class="space-y-4 mt-auto">
        <a
          class="block w-full bg-juniper hover:bg-light_juniper text-ink-400 uppercase rounded-md font-bold text-center px-4 py-3.5 transition-colors duration-200"
          href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
          target="_blank"
          rel="noopener noreferrer"
        >
          <span class="inline-flex items-center justify-center space-x-2">
            <PlusCircleIcon class="h-5 w-5 stroke-2" />
            <span>Add your project</span>
          </span>
        </a>

        <!-- DeepSource attribution -->
        <div class="flex justify-center pt-4">
          <a
            class="inline-flex items-center space-x-2 text-sm hover:text-vanilla-100 transition-colors duration-200"
            target="_blank"
            rel="noopener noreferrer"
            href="https://deepsource.com?ref=gfi"
          >
            <HeartIcon class="w-4 h-4 text-cherry" />
            <span>
              A <span class="text-juniper hover:underline">DeepSource</span> initiative
            </span>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import Tags from '~/data/tags.json'
import { PlusCircleIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'
</script>

<style>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate;
  letter-spacing: 0.05em;
}

.active-pill {
  @apply text-juniper font-semibold border-juniper;
}

.active-pill > span {
  @apply text-juniper;
}
</style>