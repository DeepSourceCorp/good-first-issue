<template>
  <aside
    class="font-sans pt-6 pb-8 border-b md:border-b-0 md:border-r border-ink-200 px-6 text-vanilla-300 flex-none w-full md:max-w-sm"
  >
    <div>
      <h2 class="text-xs font-bold uppercase tracking-wider mb-2 text-slate">
        About
      </h2>
      <p class="text-sm leading-relaxed text-vanilla-300/90">
        Good First Issue curates easy pickings from popular open-source
        projects, and helps you make your first contribution to open-source.
      </p>
    </div>

    <nav aria-label="Browse issues by programming language" class="pt-6">
      <div class="flex items-center justify-between mb-3">
        <h2 class="text-xs font-bold uppercase tracking-wider text-slate">
          Browse by language
        </h2>
        <NuxtLink
          v-if="currentSlug"
          to="/"
          class="text-xs text-juniper hover:underline"
        >
          Clear filter
        </NuxtLink>
      </div>

      <div class="flex flex-wrap gap-2">
        <NuxtLink
          v-for="tag in sortedTags"
          :key="tag.slug"
          :to="isActive(tag.slug) ? '/' : `/language/${tag.slug}`"
          :aria-current="isActive(tag.slug) ? 'page' : undefined"
          :class="[
            'group border px-2.5 py-1 rounded text-sm transition-all duration-150 focus:outline-none focus:ring-2 focus:ring-juniper/50',
            isActive(tag.slug)
              ? 'text-juniper font-semibold border-juniper bg-juniper/10'
              : 'border-slate/60 hover:text-juniper hover:border-juniper'
          ]"
        >
          <span>{{ tag.language }}</span>
          <span
            :class="[
              'ml-1 text-xs',
              isActive(tag.slug)
                ? 'text-juniper'
                : 'text-vanilla-400 group-hover:text-juniper'
            ]"
          >
            &times; {{ tag.count }}
          </span>
        </NuxtLink>
      </div>
    </nav>

    <div class="pt-6">
      <a
        class="bg-juniper hover:bg-light_juniper active:scale-[0.99] text-ink-400 uppercase rounded-md font-bold text-sm tracking-wide text-center px-4 py-3 flex items-center justify-center gap-2 transition-all focus:outline-none focus:ring-2 focus:ring-juniper focus:ring-offset-2 focus:ring-offset-ink-400"
        href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
        target="_blank"
        rel="noopener noreferrer"
      >
        <PlusCircleIcon class="h-5 w-5 stroke-2" aria-hidden="true" />
        <span>Add your project</span>
      </a>
    </div>

    <footer class="text-sm pt-6">
      <a
        class="flex justify-center items-center gap-1.5 text-vanilla-400 hover:text-vanilla-200 transition-colors group"
        target="_blank"
        rel="noopener noreferrer"
        href="https://deepsource.com?ref=gfi"
      >
        <HeartIcon class="w-4 h-4 text-cherry group-hover:scale-110 transition-transform" aria-hidden="true" />
        <span>
          A
          <span class="group-hover:underline text-juniper font-medium">
            DeepSource
          </span>
          initiative
        </span>
      </a>
    </footer>
  </aside>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import rawTags from '~/data/tags.json'
import { PlusCircleIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'

interface LanguageTag {
  language: string
  slug: string
  count: number
}

const route = useRoute()

const currentSlug = computed(() =>
  typeof route.params.slug === 'string' ? route.params.slug : null
)

const sortedTags = computed<LanguageTag[]>(() =>
  [...(rawTags as LanguageTag[])].sort((a, b) => b.count - a.count)
)

const isActive = (slug: string): boolean => currentSlug.value === slug
</script>