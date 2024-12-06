<template>
  <section class="masthead font-sans pt-6 border-r border-ink-200 px-6 text-vanilla-300 flex-none w-full md:max-w-sm">
    <div>
      <h3 class="section-heading">About</h3>
      <p class="text-sm">
        Good First Issue curates easy pickings from popular open-source projects, and helps you make your first
        contribution to open-source.
      </p>
    </div>

    <div class="pt-6 relative" ref="dropdownRef">
      <h3 class="section-heading">Browse by language</h3>
      
      <!-- 已选择的标签 -->
      <div class="flex flex-wrap gap-2 mb-2">
        <div
          v-for="slug in selectedTags"
          :key="slug"
          class="active-pill px-2 py-1 rounded-sm text-sm flex items-center gap-1"
        >
          {{ allTags.find(t => t.slug === slug)?.language }}
          <button
            @click="toggleTag(slug)"
            class="hover:text-cherry ml-1"
            aria-label="Remove tag"
          >
            ×
          </button>
        </div>
      </div>

      <!-- 下拉菜单触发器 -->
      <button
        @click="isDropdownOpen = !isDropdownOpen"
        class="w-full px-4 py-2 text-left border border-slate rounded-sm flex justify-between items-center hover:border-juniper group"
      >
        <span class="group-hover:text-juniper">Select Languages</span>
        <ChevronDownIcon
          class="w-4 h-4 group-hover:text-juniper transition-transform duration-200"
          :class="{ 'transform rotate-180': isDropdownOpen }"
        />
      </button>

      <!-- 下拉菜单内容 -->
      <div
        v-show="isDropdownOpen"
        class="absolute left-0 right-0 mt-1 bg-ink-400 border border-slate rounded-sm shadow-lg z-50"
      >
        <div class="max-h-[300px] overflow-y-auto">
          <div
            v-for="tag in allTags"
            :key="tag.slug"
            @click="toggleTag(tag.slug)"
            class="px-4 py-2 hover:bg-ink-300 cursor-pointer flex justify-between items-center"
            :class="{ 'text-juniper': selectedTags.includes(tag.slug) }"
          >
            <span>{{ tag.language }}</span>
            <span class="text-sm text-vanilla-400">{{ tag.count }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="pt-6">
      <a
        class="bg-juniper hover:bg-light_juniper text-ink-400 uppercase rounded-md font-bold text-center px-1 py-3 flex flex-row items-center justify-center space-x-1"
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
        <span class="ml-2">A <span class="inline hover:underline text-juniper">DeepSource</span> initiative</span>
      </a>
    </div>
  </section>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import { PlusCircleIcon } from '@heroicons/vue/24/outline'
import { HeartIcon, ChevronDownIcon } from '@heroicons/vue/24/solid'
import { onClickOutside } from '@vueuse/core'

const selectedTags = useState('selectedTags', () => [])
const isDropdownOpen = ref(false)
const dropdownRef = ref(null)

const allTags = computed(() => {
  const tagCount = {}
  
  Repositories.forEach(repo => {
    if (repo.language) {
      const langSlug = repo.language.toLowerCase()
      tagCount[langSlug] = tagCount[langSlug] || { 
        language: repo.language,
        slug: langSlug,
        count: 0
      }
      tagCount[langSlug].count++
    }
    
    if (repo.languages) {
      Object.keys(repo.languages).forEach(lang => {
        const langSlug = lang.toLowerCase()
        tagCount[langSlug] = tagCount[langSlug] || {
          language: lang,
          slug: langSlug,
          count: 0
        }
        tagCount[langSlug].count++
      })
    }
  })
  
  return Object.values(tagCount).sort((a, b) => b.count - a.count)
})

const toggleTag = (slug) => {
  const index = selectedTags.value.indexOf(slug)
  if (index === -1) {
    selectedTags.value.push(slug)
  } else {
    selectedTags.value.splice(index, 1)
  }
}

onClickOutside(dropdownRef, () => {
  isDropdownOpen.value = false
})
</script>

<style scoped>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate;
}

.active-pill {
  @apply text-juniper font-semibold border-juniper border;
}

/* 自定义滚动条样式 */
.overflow-y-auto {
  scrollbar-width: thin;
  scrollbar-color: theme('colors.juniper') theme('colors.ink.300');
}

.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: theme('colors.ink.300');
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: theme('colors.juniper');
  border-radius: 3px;
}
</style>
