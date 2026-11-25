<template>
  <aside
    class="font-sans py-6 border-b md:border-b-0 md:border-r border-ink-200 px-6 text-vanilla-300 flex flex-col justify-between flex-none w-full md:max-w-sm"
  >
    <div class="space-y-6">
      <!-- About Section -->
      <section aria-labelledby="about-heading">
        <h2
          id="about-heading"
          class="text-xs font-bold uppercase tracking-wider mb-2 text-slate"
        >
          About
        </h2>
        <p class="text-sm leading-relaxed text-vanilla-300/90">
          Good First Issue curates easy pickings from popular open-source
          projects, and helps you make your first contribution to open-source.
        </p>
      </section>

      <!-- Language Navigation -->
      <nav aria-labelledby="languages-heading">
        <div class="flex items-center justify-between mb-3">
          <h2
            id="languages-heading"
            class="text-xs font-bold uppercase tracking-wider text-slate"
          >
            Browse by language
          </h2>
          <NuxtLink
            v-if="currentSlug"
            to="/"
            class="text-xs font-medium text-juniper hover:underline focus:outline-none focus:ring-2 focus:ring-juniper/50 rounded px-1"
          >
            Reset filter
          </NuxtLink>
        </div>

        <!-- Quick Search Input (aparece se houver mais de 10 linguagens) -->
        <div v-if="tags.length > 10" class="relative mb-3">
          <MagnifyingGlassIcon
            class="w-4 h-4 text-slate absolute left-2.5 top-1/2 -translate-y-1/2 pointer-events-none"
            aria-hidden="true"
          />
          <input
            v-model.trim="searchQuery"
            type="search"
            placeholder="Filter languages..."
            aria-label="Filter programming languages"
            class="w-full bg-ink-300/50 border border-ink-200 rounded text-xs text-vanilla-200 placeholder-slate pl-8 pr-3 py-1.5 focus:outline-none focus:border-juniper transition-colors"
          />
        </div>

        <!-- Tags List -->
        <div v-if="visibleTags.length > 0" class="flex flex-wrap gap-2">
          <NuxtLink
            v-for="tag in visibleTags"
            :key="tag.slug"
            :to="isActive(tag.slug) ? '/' : `/language/${tag.slug}`"
            :aria-current="isActive(tag.slug) ? 'page' : undefined"
            :class="[
              'group inline-flex items-center gap-1.5 border px-2.5 py-1 rounded text-sm transition-all duration-150 focus:outline-none focus:ring-2 focus:ring-juniper/50',
              isActive(tag.slug)
                ? 'text-juniper font-semibold border-juniper bg-juniper/10 shadow-sm'
                : 'border-slate/50 hover:text-juniper hover:border-juniper hover:bg-juniper/5'
            ]"
          >
            <span>{{ tag.language }}</span>
            <span
              :class="[
                'text-xs tabular-nums',
                isActive(tag.slug)
                  ? 'text-juniper'
                  : 'text-vanilla-400 group-hover:text-juniper'
              ]"
            >
              <span class="sr-only">issues count:</span>&times; {{ tag.count }}
            </span>
          </NuxtLink>
        </div>

        <!-- Empty Search State -->
        <p v-else class="text-xs text-slate italic py-2">
          No languages matching "{{ searchQuery }}"
        </p>

        <!-- Show More / Less Toggle -->
        <button
          v-if="hasMoreTags && !searchQuery"
          type="button"
          :aria-expanded="isExpanded"
          class="mt-3 text-xs font-medium text-vanilla-400 hover:text-juniper transition-colors flex items-center gap-1 focus:outline-none focus:underline"
          @click="isExpanded = !isExpanded"
        >
          <span>
            {{ isExpanded ? 'Show fewer languages' : `Show all ${filteredTags.length} languages` }}
          </span>
        </button>
      </nav>

      <!-- CTA Button -->
      <div>
        <a
          class="bg-juniper hover:bg-light_juniper active:scale-[0.99] text-ink-400 uppercase rounded-md font-bold text-sm tracking-wide text-center px-4 py-3 flex items-center justify-center gap-2 transition-all shadow-sm focus:outline-none focus:ring-2 focus:ring-juniper focus:ring-offset-2 focus:ring-offset-ink-400"
          :href="EXTERNAL_LINKS.ADD_PROJECT"
          target="_blank"
          rel="noopener noreferrer"
        >
          <PlusCircleIcon class="h-5 w-5 stroke-2" aria-hidden="true" />
          <span>Add your project</span>
        </a>
      </div>
    </div>

    <!-- Footer Attribution -->
    <footer class="text-sm pt-8 mt-auto">
      <a
        class="flex justify-center items-center gap-1.5 text-vanilla-400 hover:text-vanilla-200 transition-colors group focus:outline-none focus:underline"
        target="_blank"
        rel="noopener noreferrer"
        :href="EXTERNAL_LINKS.DEEPSOURCE"
      >
        <HeartIcon
          class="w-4 h-4 text-cherry group-hover:scale-110 transition-transform"
          aria-hidden="true"
        />
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
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import rawTags from '~/data/tags.json'
import { PlusCircleIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'

export interface LanguageTag {
  language: string
  slug: string
  count: number
}

const props = withDefaults(
  defineProps<{
    tags?: LanguageTag[]
    initialVisibleCount?: number
  }>(),
  {
    tags: () => rawTags as LanguageTag[],
    initialVisibleCount: 12
  }
)

const EXTERNAL_LINKS = {
  ADD_PROJECT: 'https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project',
  DEEPSOURCE: 'https://deepsource.com?ref=gfi'
} as const

const route = useRoute()
const searchQuery = ref('')
const isExpanded = ref(false)

const currentSlug = computed(() =>
  typeof route.params.slug === 'string' ? route.params.slug : null
)

const isActive = (slug: string): boolean => currentSlug.value === slug

const sortedTags = computed(() =>
  [...props.tags].sort((a, b) => b.count - a.count)
)

const filteredTags = computed(() => {
  if (!searchQuery.value) return sortedTags.value
  const query = searchQuery.value.toLowerCase()
  return sortedTags.value.filter((tag) =>
    tag.language.toLowerCase().includes(query)
  )
})

const hasMoreTags = computed(
  () => filteredTags.value.length > props.initialVisibleCount
)

const visibleTags = computed(() => {
  if (isExpanded.value || searchQuery.value) {
    return filteredTags.value
  }
  return filteredTags.value.slice(0, props.initialVisibleCount)
})

// Expande automaticamente se o utilizador aceder diretamente a uma URL de linguagem
// que esteja fora do top inicial (ex: /language/rust na posição 15)
watch(
  currentSlug,
  (newSlug) => {
    if (!newSlug) return
    const index = sortedTags.value.findIndex((t) => t.slug === newSlug)
    if (index >= props.initialVisibleCount) {
      isExpanded.value = true
    }
  },
  { immediate: true }
)
</script>