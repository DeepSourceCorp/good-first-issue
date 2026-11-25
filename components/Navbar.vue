<template>
  <header class="w-full py-4 px-4 sm:px-6 border-b border-ink-200 bg-ink-400">
    <nav
      aria-label="Primary navigation"
      class="max-w-7xl mx-auto flex items-center justify-center flex-wrap gap-1"
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

      <NuxtLink
        v-if="activeTag"
        :to="`/language/${activeTag.slug}`"
        aria-current="page"
        class="inline-flex items-center text-xl sm:text-2xl rounded px-1.5 py-0.5 hover:bg-ink-300/60 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper"
      >
        <span class="font-normal mr-2 text-slate select-none" aria-hidden="true">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </NuxtLink>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import rawTags from '~/data/tags.json'

export interface LanguageTag {
  language: string
  slug: string
  count?: number
}

interface Props {
  tags?: LanguageTag[]
  homeTo?: string
}

const props = withDefaults(defineProps<Props>(), {
  tags: () => rawTags as LanguageTag[],
  homeTo: '/'
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
</script><template>
  <header class="w-full py-4 px-4 sm:px-6 border-b border-ink-200 bg-ink-400">
    <nav
      aria-label="Primary navigation"
      class="max-w-7xl mx-auto flex items-center justify-center flex-wrap gap-1"
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

      <NuxtLink
        v-if="activeTag"
        :to="`/language/${activeTag.slug}`"
        aria-current="page"
        class="inline-flex items-center text-xl sm:text-2xl rounded px-1.5 py-0.5 hover:bg-ink-300/60 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-juniper"
      >
        <span class="font-normal mr-2 text-slate select-none" aria-hidden="true">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </NuxtLink>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import rawTags from '~/data/tags.json'

export interface LanguageTag {
  language: string
  slug: string
  count?: number
}

interface Props {
  tags?: LanguageTag[]
  homeTo?: string
}

const props = withDefaults(defineProps<Props>(), {
  tags: () => rawTags as LanguageTag[],
  homeTo: '/'
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