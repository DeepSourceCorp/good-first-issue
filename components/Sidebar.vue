<template>
  <aside
    class="masthead font-sans pt-6 border-r border-ink-200 px-6 text-vanilla-300 flex-none w-full md:max-w-sm"
  >
    <div>
      <h2 class="section-heading">About</h2>
      <p class="text-sm leading-relaxed">
        Good First Issue curates easy pickings from popular open-source
        projects, and helps you make your first contribution to open-source.
      </p>
    </div>

    <nav aria-label="Filter by programming language" class="pt-6">
      <h2 class="section-heading">Browse by language</h2>
      <div class="flex flex-wrap gap-2">
        <NuxtLink
          v-for="tag in Tags"
          :key="tag.slug"
          :to="`/language/${tag.slug}`"
          :aria-current="isCurrentTag(tag.slug) ? 'page' : undefined"
          :class="[
            'group border px-2.5 py-1 rounded-sm text-sm transition-colors',
            isCurrentTag(tag.slug)
              ? 'active-pill'
              : 'border-slate hover:text-juniper hover:border-juniper'
          ]"
        >
          {{ tag.language }}
          <span
            :class="
              isCurrentTag(tag.slug)
                ? 'text-juniper'
                : 'text-vanilla-400 group-hover:text-juniper'
            "
          >
            &times; {{ tag.count }}
          </span>
        </NuxtLink>
      </div>
    </nav>

    <div class="pt-6">
      <a
        class="bg-juniper hover:bg-light_juniper text-ink-400 uppercase rounded-md font-bold text-center px-3 py-3 flex items-center justify-center gap-2 transition-colors"
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
        class="flex justify-center items-center gap-2 group"
        target="_blank"
        rel="noopener noreferrer"
        href="https://deepsource.com?ref=gfi"
      >
        <HeartIcon class="w-4 h-4 text-cherry" aria-hidden="true" />
        <span>
          A
          <span class="group-hover:underline text-juniper">
            DeepSource
          </span>
          initiative
        </span>
      </a>
    </footer>
  </aside>
</template>

<script setup>
import { useRoute } from 'vue-router'
import Tags from '~/data/tags.json'
import { PlusCircleIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'

const route = useRoute()

const isCurrentTag = (slug) => route.params.slug === slug
</script>

<style scoped>
.section-heading {
  @apply text-xs font-bold uppercase tracking-wider mb-3 text-slate;
}

.active-pill {
  @apply text-juniper font-semibold border-juniper bg-juniper/10;
}
</style>
