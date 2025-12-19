<template>
  <!-- <AppView></AppView> -->
  <AppLayout>
    <div class="flex-1">
      <div class="flex flex-col md:flex-row gap-8">
        <Sidebar class="w-full md:w-64 flex-shrink-0" />
        <main class="flex-1">
          <slot />
        </main>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import AppLayout from '~/layouts/AppLayout.vue'
import Sidebar from '~/components/Sidebar.vue'

const route = useRoute()
const tags = useState('tags', () => [])

// Fetch tags if not already loaded
if (process.client && tags.value.length === 0) {
  const { data } = await useFetch('/api/tags')
  if (data.value) {
    tags.value = data.value
  }
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
