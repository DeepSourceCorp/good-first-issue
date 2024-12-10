<template>
  <aside class="w-full md:max-w-sm p-6 border-r border-ink-200 bg-ink-500 text-vanilla-300">
    <section>
      <h3 class="section-heading">About</h3>
      <p class="text-sm">
        Good First Issue curates easy pickings from popular open-source projects, and helps you make your first
        contribution to open-source.
      </p>
    </section>

    <section class="pt-6">
      <h3 class="section-heading">Browse by language</h3>
      <div>
        <nuxt-link
          v-for="tag in Tags"
          :key="tag.slug"
          :to="'/language/' + tag.slug"
          :class="{ 'active-pill': isActiveTag(tag.slug) }"
          class="mx-1 my-1 px-2 py-1 border rounded-sm text-sm inline-block group border-slate hover:border-juniper hover:text-juniper"
        >
          {{ tag.language }}
          <span
            class="text-vanilla-400 group-hover:text-juniper ml-1"
          >&times; {{ tag.count }}</span>
        </nuxt-link>
      </div>
    </section>

    <section class="pt-6">
      <a
        href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
        target="_blank"
        rel="noopener noreferrer"
        class="cta-button"
      >
        <PlusCircleIcon class="h-5 w-5 stroke-2" />
        <span>Add your project</span>
      </a>
    </section>

    <section class="pt-6 text-sm">
      <a
        href="https://deepsource.com?ref=gfi"
        target="_blank"
        rel="noopener noreferrer"
        class="flex items-center justify-center"
      >
        <HeartIcon class="w-4 h-4 text-cherry" />
        <span class="ml-2">
          A
          <span class="inline hover:underline text-juniper">DeepSource</span>
          initiative
        </span>
      </a>
    </section>
  </aside>
</template>

<script setup>
import Tags from '~/data/tags.json';
import { PlusCircleIcon } from '@heroicons/vue/24/outline';
import { HeartIcon } from '@heroicons/vue/24/solid';

const route = useRoute();
const isActiveTag = slug => route.params.slug === slug;
</script>

<style>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate;
}
.active-pill {
  @apply border-juniper text-juniper font-semibold;
}
.cta-button {
  @apply bg-juniper hover:bg-light_juniper text-ink-400 font-bold uppercase rounded-md px-4 py-2 flex items-center space-x-2;
}
</style>
