<template>
  <div :class="rootClasses">
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
import useTheme from '~/composables/useTheme'
import { ref, computed } from 'vue'

const route = useRoute()

const tag = ref({})

if (route.params.slug) {
  tag.value = Tags.find(t => t.slug === route.params.slug)
}

const { isDark } = useTheme()

const rootClasses = computed(() => {
  // dark: original classes; light: swap bg/text to light variants
  return isDark.value
    ? 'bg-ink-400 flex flex-col min-h-screen antialiased text-vanilla-300'
    : 'bg-vanilla-100 flex flex-col min-h-screen antialiased text-ink-100'
})

useHead({
  charset: "utf-8",
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

<style>
/* Ensure elements using 'text-vanilla-*' become dark in light mode for accessibility */
.light .text-vanilla-300,
.light .text-vanilla-200,
.light .text-vanilla-100 {
  color: #000 !important;
}

/* Keep repo cards light in light mode: hover and open states should not turn dark */
.light .repo-box {
  background-color: transparent !important;
}
.light .repo-box:hover {
  background-color: #f5f5f5 !important; /* tailwind vanilla-200 */
}
.light .repo-box.border-juniper,
.light .repo-box.border-juniper:hover {
  background-color: #f5f5f5 !important;
}

.light .repo-box .text-slate,
.light .repo-box .text-vanilla-300,
.light .repo-box .text-vanilla-400,
.light .repo-box .text-vanilla-200 {
  color: #000 !important;
}
</style>
