<template>
  <div class="p-4 w-full">
    <!-- Filter Controls -->
    <div class="flex flex-wrap gap-4 mb-6">
      <div class="flex flex-col gap-1">
        <label
          class="text-xs font-bold uppercase tracking-wider"
          style="color: #8b9cb0;"
        >Min Stars</label>
        <select
          v-model="minStars"
          class="border border-ink-200 rounded px-3 py-1 text-sm cursor-pointer"
          style="background-color: #2a2f3a; color: #d4dae3; border-color: #3a4150;"
        >
          <option :value="0" style="background-color: #2a2f3a;">Any Stars</option>
          <option :value="100" style="background-color: #2a2f3a;">100+ Stars</option>
          <option :value="500" style="background-color: #2a2f3a;">500+ Stars</option>
          <option :value="1000" style="background-color: #2a2f3a;">1,000+ Stars</option>
          <option :value="5000" style="background-color: #2a2f3a;">5,000+ Stars</option>
          <option :value="10000" style="background-color: #2a2f3a;">10,000+ Stars</option>
        </select>
      </div>

      <div class="flex flex-col gap-1">
        <label
          class="text-xs font-bold uppercase tracking-wider"
          style="color: #8b9cb0;"
        >Last Active</label>
        <select
          v-model="maxMonthsAgo"
          class="border border-ink-200 rounded px-3 py-1 text-sm cursor-pointer"
          style="background-color: #2a2f3a; color: #d4dae3; border-color: #3a4150;"
        >
          <option :value="0" style="background-color: #2a2f3a;">Any Time</option>
          <option :value="1" style="background-color: #2a2f3a;">Last 1 month</option>
          <option :value="3" style="background-color: #2a2f3a;">Last 3 months</option>
          <option :value="6" style="background-color: #2a2f3a;">Last 6 months</option>
          <option :value="12" style="background-color: #2a2f3a;">Last 1 year</option>
          <option :value="36" style="background-color: #2a2f3a;">Last 3 years</option>
          <option :value="60" style="background-color: #2a2f3a;">Last 5 years</option>
        </select>
      </div>

      <div class="flex items-end pb-1">
        <span class="text-xs" style="color: #8b9cb0;">
          {{ filteredRepositories.length }} repo{{ filteredRepositories.length !== 1 ? 's' : '' }}
        </span>
      </div>
    </div>

    <!-- Repo List -->
    <RepoBox
      v-for="repo in filteredRepositories"
      :key="repo.id"
      :repo="repo"
    />

    <!-- Empty State -->
    <div
      v-if="filteredRepositories.length === 0"
      class="text-center py-12"
      style="color: #8b9cb0;"
    >
      No repositories match your filters. Try adjusting the criteria.
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

// Filter state
const minStars = ref(0)
const maxMonthsAgo = ref(0)

// Base repos for this language slug
const baseRepositories = Repositories.filter(
  repository => repository.slug === route.params.slug
)

// Computed: filter + sort
const filteredRepositories = computed(() => {
  return baseRepositories
    .filter(repo => {
      // Stars filter
      const matchesStars = repo.stars >= minStars.value

      // Activity filter
      let matchesActivity = true
      if (maxMonthsAgo.value > 0) {
        const lastActive = new Date(repo.last_modified)
        const cutoff = new Date()
        cutoff.setMonth(cutoff.getMonth() - maxMonthsAgo.value)
        matchesActivity = lastActive >= cutoff
      }

      return matchesStars && matchesActivity
    })
    .sort((a, b) => {
      // Sort by stars descending when stars filter is active
      if (minStars.value > 0) return b.stars - a.stars
      return 0
    })
})

const tag = Tags.find(t => t.slug === route.params.slug)

useHead({
  title: `${tag.language} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
  }]
})
</script>