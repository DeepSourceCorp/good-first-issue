<template>
  <div class="border border-ink-200 rounded-md p-4 mb-4">
    <div class="flex items-start justify-between">
      <div>
        
          :href="repo.url"
          target="_blank"
          rel="noopener noreferrer"
          class="text-juniper font-semibold text-lg hover:underline"
        >
          {{ repo.owner }}/{{ repo.name }}
        </a>
        <p class="text-sm text-vanilla-300 mt-1">{{ repo.description }}</p>
      </div>
      <span class="text-sm text-vanilla-400 ml-4">⭐ {{ repo.stars_display }}</span>
    </div>

    <!-- Top 3 languages fix for issue #2246 -->
    <div class="mt-3 flex flex-wrap gap-1">
      <nuxt-link
        v-for="lang in topLanguages"
        :key="lang.slug"
        :to="'/language/' + lang.slug"
        class="border border-slate px-2 py-1 rounded-sm text-xs text-vanilla-300 hover:text-juniper hover:border-juniper"
      >
        {{ lang.language }}
      </nuxt-link>
    </div>

    <!-- Issues -->
    <div class="mt-3 space-y-1">
      
        v-for="issue in repo.issues"
        :key="issue.number"
        :href="issue.url"
        target="_blank"
        rel="noopener noreferrer"
        class="block text-sm text-vanilla-300 hover:text-juniper hover:underline"
      >
        #{{ issue.number }} — {{ issue.title }}
      </a>
    </div>
  </div>
</template>

<script setup>
import Tags from '~/data/tags.json'

const props = defineProps({
  repo: {
    type: Object,
    required: true
  }
})

// Issue #2246: show top 3 languages instead of just 1
const topLanguages = Tags.filter(tag => tag.slug === props.repo.slug).slice(0, 3)
</script>