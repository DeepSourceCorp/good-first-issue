<template>
  <header class="w-full py-4 px-4 sm:px-6 border-b border-ink-200 bg-ink-400">
    <div class="max-w-7xl mx-auto relative flex items-center justify-center min-h-12">
      <nav
        aria-label="Primary navigation"
        class="flex items-center justify-center flex-wrap gap-1"
      >
        <NuxtLink
          :to="homeTo"
          :aria-label="brandName"
          class="inline-flex items-center rounded focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper"
        >
          <slot name="logo">
            <img
              :src="logoSrc"
              :alt="brandName"
              class="h-12 w-auto"
            />
          </slot>
        </NuxtLink>

        <Transition
          mode="out-in"
          enter-active-class="transition-all motion-reduce:transition-none duration-200 ease-out"
          enter-from-class="opacity-0 -translate-x-1"
          enter-to-class="opacity-100 translate-x-0"
          leave-active-class="transition-all motion-reduce:transition-none duration-150 ease-in"
          leave-from-class="opacity-100 translate-x-0"
          leave-to-class="opacity-0 translate-x-1"
        >
          <div
            v-if="resolvedTag"
            :key="resolvedTag.slug"
            class="inline-flex items-center"
          >
            <span
              class="font-normal mx-2 text-2xl text-slate select-none"
              aria-hidden="true"
            >
              /
            </span>

            <slot name="active-tag" :tag="resolvedTag">
              <div
                class="inline-flex items-center gap-1.5 rounded-md bg-ink-300/60 border border-ink-200 px-2.5 py-1"
              >
                <NuxtLink
                  :to="`/language/${resolvedTag.slug}`"
                  aria-current="page"
                  class="text-lg sm:text-xl font-semibold text-juniper hover:underline focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper rounded"
                >
                  {{ resolvedTag.language }}
                </NuxtLink>

                <span
                  v-if="showCount && typeof resolvedTag.count === 'number'"
                  class="text-xs font-medium text-vanilla-400 tabular-nums"
                >
                  ({{ resolvedTag.count }})
                </span>

                <NuxtLink
                  :to="homeTo"
                  :aria-label="`Clear ${resolvedTag.language} filter`"
                  title="Clear language filter"
                  class="ml-0.5 rounded p-0.5 text-slate hover:text-vanilla-200 hover:bg-ink-200/60 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper"
                >
                  <XMarkIcon class="w-4 h-4" aria-hidden="true" />
                </NuxtLink>
              </div>
            </slot>
          </div>
        </Transition>
      </nav>

      <div
        v-if="$slots.right"
        class="hidden md:flex items-center gap-3 absolute right-0"
      >
        <slot name="right" :active-tag="resolvedTag" />
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { XMarkIcon } from '@heroicons/vue/20/solid'
import defaultLogo from '~/assets/gfi-logo-white.svg'
import rawTags from '~/data/tags.json'

export interface LanguageTag {
  language: string
  slug: string
  count?: number
}

interface Props {
  tags?: LanguageTag[]
  homeTo?: string
  logoSrc?: string
  brandName?: string
  showCount?: boolean
  fallbackFromSlug?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  tags: () => rawTags as LanguageTag[],
  homeTo: '/',
  logoSrc: defaultLogo,
  brandName: 'Good First Issue',
  showCount: true,
  fallbackFromSlug: true
})

const route = useRoute()

const currentSlug = computed<string | null>(() => {
  const slug = route.params.slug
  if (typeof slug === 'string' && slug.trim().length > 0) return slug
  if (Array.isArray(slug) && typeof slug[0] === 'string' && slug[0].trim().length > 0) {
    return slug[0]
  }
  return null
})

const formatSlugAsLabel = (slug: string): string =>
  slug
    .split('-')
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ')

const resolvedTag = computed<LanguageTag | null>(() => {
  const slug = currentSlug.value
  if (!slug) return null

  const matched = props.tags.find((tag) => tag.slug === slug)
  if (matched) return matched

  if (props.fallbackFromSlug) {
    return {
      slug,
      language: formatSlugAsLabel(slug)
    }
  }

  return null
})
</script>