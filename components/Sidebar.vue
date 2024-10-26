<template>
  <div>
    <!-- Language Browsing Section -->
    <div class="pt-6">
      <h3 class="section-heading">Browse by language</h3>
      <div class="pt-4">
        <LanguageTag
          v-for="tag in Tags"
          :key="tag.slug"
          :tag="tag"
          :isActive="isActiveTag(tag)"
        />
      </div>
    </div>

    <!-- Project Link Section -->
    <div class="pt-6">
      <a
        href="https://github.com/deepsourcelabs/good-first-issue#adding-a-new-project"
        target="_blank"
        rel="noopener noreferrer"
        class="flex items-center space-x-2"
      >
        <PlusCircleIcon class="h-5 w-5 stroke-2" />
        <span>Add your project</span>
      </a>
    </div>

    <!-- Initiative Footer Section -->
    <div class="text-sm pt-6">
      <a
        class="flex justify-center items-center"
        href="https://deepsource.io"
        target="_blank"
        rel="noopener noreferrer"
      >
        <HeartIcon class="h-4 w-4 text-juniper" />
        <span class="ml-2">
          A <span class="inline hover:underline text-juniper" title="Visit DeepSource website">DeepSource</span>
          initiative
        </span>
      </a>
    </div>
  </div>
</template>

<script setup>
import Tags from '~/data/tags.json'
import { PlusCircleIcon, HeartIcon } from '@heroicons/vue/24/outline'
import { ref, computed } from 'vue'
import LanguageTag from '~/components/LanguageTag.vue'

// Helper function to determine active state based on route parameters
const isActiveTag = (tag) => computed(() => $route.params.slug === tag.slug)
</script>

<style scoped>
.section-heading {
  @apply text-sm font-bold uppercase tracking-wider mb-2 text-slate;
}
</style>