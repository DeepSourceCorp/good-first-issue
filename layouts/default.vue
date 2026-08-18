<template>
  <div class="bg-ink-400 flex flex-col min-h-screen antialiased text-vanilla-300">
    <Navbar />
    <main class="flex flex-1">
      <section class="container max-w-6xl mx-auto flex flex-col md:flex-row">
        <Sidebar />
        <slot />
      </section>
    </main>
  </div>
</template>

<script setup>
import Tags from '~/data/tags.json'
const route = useRoute()
const router = useRouter()
const searchQuery = useSearchQuery()

const tag = ref({})

if (route.params.slug) {
  tag.value = Tags.find((t) => t.slug === route.params.slug)
}

// Sync from URL to state
watch(
  () => route.query.q,
  (newVal) => {
    if (searchQuery.value !== (newVal || '')) {
      searchQuery.value = newVal || ''
    }
  },
  { immediate: true }
)

// Sync from state to URL
if (process.client) {
  watch(searchQuery, (newVal) => {
    if (route.query.q !== (newVal || undefined)) {
      router.replace({ query: { ...route.query, q: newVal || undefined } })
    }
  })
}

useHead({
  charset: 'utf-8',
  link: [
    {
      rel: 'apple-touch-icon',
      sizes: '180x180',
      href: '/apple-touch-icon.png'
    },
    {
      rel: 'icon',
      type: 'image/png',
      sizes: '32x32',
      href: '/favicon-32x32.png'
    },
    {
      rel: 'icon',
      type: 'image/png',
      sizes: '16x16',
      href: '/favicon-16x16.png'
    },
    {
      rel: 'manifest',
      href: '/site.webmanifest'
    }
  ]
})

useSeoMeta({
  ogImage: '/images/meta.jpg'
})
</script>
