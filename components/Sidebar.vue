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
          :to="languageLink(tag.slug)"
          :class="{
            'active-pill': selectedSlugs.includes(tag.slug),
            'border-slate hover:text-juniper hover:border-juniper': !selectedSlugs.includes(tag.slug)
          }"
          class="group mx-1 border px-2 py-1 inline-block rounded-sm my-1 text-sm"
          >{{ tag.language }}
          <span
            :class="{
              'text-vanilla-400 group-hover:text-juniper': !selectedSlugs.includes(tag.slug)
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
import {HeartIcon} from '@heroicons/vue/24/solid'

const route = useRoute()

const selectedSlugs = computed(() => {
  const queryLanguages = route.query.languages
  const languages = typeof queryLanguages === 'string' ? queryLanguages.split(',') : []
  const routeLanguage = typeof route.params.slug === 'string' ? route.params.slug : ''

  return [...new Set([routeLanguage, ...languages].filter(Boolean))]
})

function languageLink(slug) {
  const languages = selectedSlugs.value.includes(slug)
    ? selectedSlugs.value.filter(selectedSlug => selectedSlug !== slug)
    : [...selectedSlugs.value, slug]

  if (languages.length === 0) {
    return '/'
  }

  return {
    path: `/language/${languages[0]}`,
    query: languages.length > 1 ? { languages: languages.join(',') } : undefined
  }
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
