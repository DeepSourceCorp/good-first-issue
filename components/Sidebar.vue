<template>
  <section
    class="masthead font-sans pt-6 border-r border-ink-200 dark:border-ink-600 px-6 text-vanilla-300 dark:text-ink-200 flex-none w-full md:max-w-sm bg-ink-100 dark:bg-ink-900 min-h-screen"
  >
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-bold">Good First Issue</h2>
      <button
        @click="toggleDarkMode"
        class="p-2 rounded-full hover:bg-ink-200 dark:hover:bg-ink-700 transition-colors"
        :title="isDarkMode ? 'Switch to light mode' : 'Switch to dark mode'"
        aria-label="Toggle dark mode"
      >
        <MoonIcon v-if="!isDarkMode" class="w-5 h-5" />
        <SunIcon v-else class="w-5 h-5" />
      </button>
    </div>

    <div class="relative mb-6">
      <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
        <MagnifyingGlassIcon class="h-4 w-4 text-ink-400" />
      </div>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search languages..."
        class="w-full pl-10 pr-4 py-2 border border-ink-200 dark:border-ink-600 rounded-md bg-white dark:bg-ink-800 text-ink-900 dark:text-ink-100 focus:ring-2 focus:ring-juniper focus:border-transparent"
      />
    </div>

    <div class="mb-6">
      <h3 class="section-heading">About</h3>
      <p class="text-sm">
        Good First Issue curates easy pickings from popular open-source projects, and helps you make your first
        contribution to open-source.
      </p>
    </div>
    <div class="pt-6">
      <div class="flex justify-between items-center mb-2">
        <h3 class="section-heading">Browse by language</h3>
        <span class="text-xs text-ink-400">{{ filteredTags.length }} languages</span>
      </div>
      <div class="max-h-[calc(100vh-400px)] overflow-y-auto pr-2 -mr-2">
        <nuxt-link
                  <!-- v-for="tag in Tags" -->
          v-for="tag in filteredTags"
          :key="tag.slug"
          :key="tag.slug"
          :to="'/language/' + tag.slug"
          :class="{
            'active-pill': $route.params.slug === tag.slug,
            'border-slate hover:text-juniper hover:border-juniper': $route.params.slug !== tag.slug
          }"
          class="group mx-1 border px-2 py-1 inline-block rounded-sm my-1 text-sm"
          >{{ tag.language }}
          <span
            :class="{
              'text-vanilla-400 group-hover:text-juniper': $route.params.slug !== tag.slug
            }"
            >&times; {{ tag.count }}</span
          ></nuxt-link
        >
      </div>
    </div>
    <div class="pt-6">
      <a
        class="bg-juniper hover:bg-light_juniper text-ink-400 dark:text-ink-900 uppercase rounded-md font-bold text-center px-4 py-3 flex flex-row items-center justify-center space-x-2 transition-all duration-200 hover:shadow-lg hover:scale-[1.02]"
        href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
        target="_blank"
        rel="noopener noreferrer"
      >
        <PlusCircleIcon class="h-5 w-5 stroke-2" />
        <span>Add your project</span>
      </a>
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
import { ref, computed } from 'vue'
import Tags from '~/data/tags.json'
import { PlusCircleIcon, MoonIcon, SunIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/outline'
import { HeartIcon } from '@heroicons/vue/24/solid'

const searchQuery = ref('')
const isDarkMode = ref(false)

const filteredTags = computed(() => {
  if (!searchQuery.value) return Tags
  const query = searchQuery.value.toLowerCase()
  return Tags.filter((tag) => tag.language.toLowerCase().includes(query) || tag.slug.toLowerCase().includes(query))
})

const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value
  document.documentElement.classList.toggle('dark', isDarkMode.value)
}
</script>
<style>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider text-slate dark:text-ink-300;
}

.active-pill {
  @apply text-juniper dark:text-juniper-400 font-semibold border-juniper dark:border-juniper-400 bg-juniper/5 dark:bg-juniper/10;
}

.active-pill > span {
  @apply text-juniper dark:text-juniper-400;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  @apply bg-ink-100 dark:bg-ink-800;
}

::-webkit-scrollbar-thumb {
  @apply bg-ink-300 dark:bg-ink-600 rounded-full;
}

::-webkit-scrollbar-thumb:hover {
  @apply bg-ink-400 dark:bg-ink-500;
}
</style>
