<template>
  <div class="p-4 w-full">
    <div class="mb-4 space-y-4">
      <div class="flex items-center space-x-4">
        <label class="text-sm text-vanilla-400">Min stars:</label>
        <input type="range" min="0" max="50000" step="10" v-model.number="minStars" class="w-64" />
        <div class="text-sm text-vanilla-300 font-mono">{{ formatStars(minStars) }}</div>
      </div>

      <div class="flex items-center space-x-4">
        <label class="text-sm text-vanilla-400">Active within:</label>
        <input type="range" min="0" max="24" step="1" v-model.number="activeWithinMonths" class="w-64" />
        <div class="text-sm text-vanilla-300 font-mono">{{ activeWithinMonths === 0 ? 'Any' : activeWithinMonths + ' mo' }}</div>
      </div>

      <div>
        <button @click="resetFilters" class="bg-juniper text-white px-3 py-1 rounded text-sm">Reset</button>
      </div>
    </div>

    <div>
      <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
      <div v-if="filteredRepositories.length === 0" class="text-sm text-vanilla-400">No repositories match the selected filters.</div>
    </div>
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import dayjs from 'dayjs'
import { ref, computed } from 'vue'

useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
  {
    name: 'description',
    content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
  }
  ]
})

const allRepos = Repositories

const minStars = ref(0)
const activeWithinMonths = ref(0)

function resetFilters() {
  minStars.value = 0
  activeWithinMonths.value = 0
}

const filteredRepositories = computed(() => {
  const now = dayjs()

  let repos = allRepos.filter(r => {
    if (minStars.value && Number(r.stars) < Number(minStars.value)) return false
    if (activeWithinMonths.value) {
      const months = Number(activeWithinMonths.value)
      const last = dayjs(r.last_modified)
      if (!last.isValid()) return false
      if (now.diff(last, 'month') > months) return false
    }
    return true
  })

  if (minStars.value && activeWithinMonths.value) {
    repos.sort((a, b) => {
      if (b.stars !== a.stars) return b.stars - a.stars
      return new Date(b.last_modified) - new Date(a.last_modified)
    })
  } else if (minStars.value) {
    repos.sort((a, b) => b.stars - a.stars)
  } else if (activeWithinMonths.value) {
    repos.sort((a, b) => new Date(b.last_modified) - new Date(a.last_modified))
  }

  return repos
})

function formatStars(n) {
  if (!n || n === 0) return 'Any'
  if (n >= 1000) return `${(n / 1000).toFixed(n % 1000 === 0 ? 0 : 1)}K`
  return String(n)
}
</script>
