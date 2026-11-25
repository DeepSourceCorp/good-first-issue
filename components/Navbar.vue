<template>
  <header class="w-full py-4 px-4 sm:px-6 border-b border-ink-200 bg-ink-400">
    <div class="max-w-7xl mx-auto relative flex items-center justify-center min-h-12">
      <nav
        aria-label="Breadcrumb navigation"
        class="flex items-center justify-center flex-wrap gap-1"
      >
        <NuxtLink
          :to="homeTo"
          aria-label="Good First Issue home"
          class="inline-flex items-center rounded focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper"
        >
          <img
            src="~/assets/gfi-logo-white.svg"
            alt="Good First Issue"
            class="h-12 w-auto"
          />
        </NuxtLink>

        <template v-if="activeTag">
          <span
            class="font-normal mx-2 text-2xl text-slate select-none"
            aria-hidden="true"
          >
            /
          </span>

          <div class="inline-flex items-center gap-1.5 rounded-md bg-ink-300/50 border border-ink-200/80 px-2.5 py-1">
            <NuxtLink
              :to="`/language/${activeTag.slug}`"
              aria-current="page"
              class="text-lg sm:text-xl font-semibold text-juniper hover:underline focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper rounded"
            >
              {{ activeTag.language }}
            </NuxtLink>

            <span
              v-if="showCount && typeof activeTag.count === 'number'"
              class="text-xs font-medium text-vanilla-400 tabular-nums"
            >
              ({{ activeTag.count }})
            </span>

            <NuxtLink
              :to="homeTo"
              :aria-label="`Clear ${activeTag.language} filter`"
              title="Clear language filter"
              class="ml-0.5 rounded p-0.5 text-slate hover:text-vanilla-200 hover:bg-ink-200/50 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper"
            >
              <XMarkIcon class="w-4 h-4" aria-hidden="true" />
            </NuxtLink>
          </div>
        </template>
      </nav>

      <div v-if="$slots.right" class="hidden md:flex items-center gap-3 absolute right-0">
        <slot name="right" />
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { XMarkIcon } from '@heroicons/vue/20/solid'
import rawTags from '~/data/tags.json'

export interface LanguageTag {
  language: string
  slug: string
  count?: number
}

interface Props {
  tags?: LanguageTag[]
  homeTo?: string
  showCount?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  tags: () => rawTags as LanguageTag[],
  homeTo: '/',
  showCount: true
})

const route = useRoute()

const currentSlug = computed<string | null>(() => {
  const slug = route.params.slug
  if (typeof slug === 'string') return slug
  if (Array.isArray(slug) && typeof slug[0] === 'string') return slug[0]
  return null
})

const activeTag = computed<LanguageTag | undefined>(() => {
  if (!currentSlug.value) return undefined
  return props.tags.find((tag) => tag.slug === currentSlug.value)
})
</script>