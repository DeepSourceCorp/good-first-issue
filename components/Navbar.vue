<template>
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center flex-wrap relative">
      <NuxtLink
        to="/"
        class="flex items-center text-gray-700 font-bold transform transition-transform duration-300 hover:scale-105"
        aria-label="Go to homepage"
      >
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
      </NuxtLink>

      <span
        v-if="activeTag"
        tabindex="0"
        role="button"
        class="relative text-2xl cursor-pointer transform transition-transform duration-300 hover:scale-110 hover:text-juniper-dark focus:outline-none focus:ring-2 focus:ring-juniper ml-4"
        @click="toggleDropdown"
        @keyup.enter="toggleDropdown"
        :aria-expanded="showDropdown.toString()"
        :aria-controls="'dropdown-' + activeTag.slug"
      >
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>

        <!-- Dropdown -->
        <div
          v-if="showDropdown"
          :id="'dropdown-' + activeTag.slug"
          class="absolute top-full mt-2 left-0 bg-white shadow-md rounded p-3 w-48 z-10"
          @click.outside="closeDropdown"
        >
          <p class="text-sm font-medium text-gray-800 mb-2">More about {{ activeTag.language }}</p>
          <ul>
            <li
              v-for="(related, index) in activeTag.relatedTags || []"
              :key="index"
              class="text-gray-600 hover:text-juniper cursor-pointer py-1"
              @click="onRelatedTagClick(related)"
              tabindex="0"
              @keyup.enter="onRelatedTagClick(related)"
            >
              {{ related }}
            </li>
            <li v-if="!(activeTag.relatedTags && activeTag.relatedTags.length)" class="text-gray-400 italic">
              No related tags
            </li>
          </ul>

          <!-- Definition box -->
          <div
            v-if="selectedDefinition"
            class="mt-4 p-2 bg-juniper-light text-juniper rounded text-sm border border-juniper"
          >
            <strong>{{ selectedTagName }}</strong
            >: {{ selectedDefinition }}
          </div>
        </div>
      </span>

      <!-- Loading shimmer if no activeTag yet -->
      <span v-else class="h-6 w-24 bg-gray-300 rounded animate-pulse ml-4"></span>
    </nav>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import Tags from '~/data/tags.json'

const route = useRoute()

const activeTag = computed(() => {
  return Tags.find((tag) => tag.slug === route.params.slug)
})

const showDropdown = ref(false)
const selectedDefinition = ref('')
const selectedTagName = ref('')

// Definitions for related tags
const definitions = {
  HTML: 'HTML (HyperText Markup Language) is the standard markup language for creating web pages.',
  CSS: 'CSS (Cascading Style Sheets) describes how HTML elements are to be displayed on screen.',
  JavaScript: 'JavaScript is a programming language that enables interactive web pages.',
  Vue: 'Vue.js is a progressive JavaScript framework for building user interfaces.'
}

function toggleDropdown() {
  showDropdown.value = !showDropdown.value
  // reset definition on open/close
  if (!showDropdown.value) {
    selectedDefinition.value = ''
    selectedTagName.value = ''
  }
}

function closeDropdown() {
  showDropdown.value = false
  selectedDefinition.value = ''
  selectedTagName.value = ''
}

function onRelatedTagClick(relatedTag) {
  console.log('Clicked related tag:', relatedTag)
  selectedTagName.value = relatedTag
  selectedDefinition.value = definitions[relatedTag] || 'Definition not available.'
}

// Handle click outside dropdown to close it
function onClickOutside(event) {
  const dropdown = document.getElementById('dropdown-' + (activeTag.value?.slug || ''))
  const tagButton = event.target.closest('[role="button"]')

  if (showDropdown.value && dropdown && !dropdown.contains(event.target) && !tagButton) {
    closeDropdown()
  }
}

onMounted(() => {
  document.addEventListener('click', onClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', onClickOutside)
})
</script>

<style scoped>
.bg-juniper-light {
  background-color: #e6f4ea; /* example light green */
}
.text-juniper {
  color: #22863a; /* example juniper green */
}
</style>
