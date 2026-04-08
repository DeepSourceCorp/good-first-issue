<template>
  <div class="p-4 w-full">
    <div v-if="repositories.length === 0" class="text-center py-8">
      <p class="text-vanilla-400">No repositories match the selected filters.</p>
    </div>
    <RepoBox v-for="repo in repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import dayjs from 'dayjs'

const starsFilter = useStarsFilter()
const activityFilter = useActivityFilter()
const issueCountFilter = useIssueCountFilter()

const repositories = computed(() => {
  let filtered = [...Repositories]

  // Filter by minimum stars
  if (starsFilter.value > 0) {
    filtered = filtered.filter(repo => repo.stars >= starsFilter.value)
  }

  // Filter by last activity (in days)
  if (activityFilter.value !== null && activityFilter.value !== undefined) {
    const cutoffDate = dayjs().subtract(activityFilter.value, 'days')
    filtered = filtered.filter(repo => dayjs(repo.last_modified).isAfter(cutoffDate))
  }

  // Filter by issue count
  if (issueCountFilter.value) {
    filtered = filtered.filter(repo => {
      const count = repo.issues.length
      switch (issueCountFilter.value) {
        case '1-3':
          return count >= 1 && count <= 3
        case '4-10':
          return count >= 4 && count <= 10
        case '11-20':
          return count >= 11 && count <= 20
        case '20+':
          return count >= 20
        default:
          return true
      }
    })
  }

  // Implicit smart sorting
  // Prioritize sorting by whichever filter user selected
  if (issueCountFilter.value) {
    // User filtered by issues → show most opportunities first
    return filtered.sort((a, b) => b.issues.length - a.issues.length)
  } else if (starsFilter.value > 0) {
    // User filtered by stars → show most popular first
    return filtered.sort((a, b) => b.stars - a.stars)
  } else if (activityFilter.value !== null && activityFilter.value !== undefined) {
    // User filtered by activity → show most recent first
    return filtered.sort((a, b) => new Date(b.last_modified) - new Date(a.last_modified))
  } else {
    // Default: balance all factors - stars → recency → issues
    const sorted = filtered.sort((a, b) => {
      const starDiff = b.stars - a.stars
      if (starDiff !== 0) return starDiff

      const recencyDiff = new Date(b.last_modified) - new Date(a.last_modified)
      if (recencyDiff !== 0) return recencyDiff

      return b.issues.length - a.issues.length
    })
    return sorted
  }
})

useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
  {
    name: 'description',
    content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
  }
  ]
})
</script>
