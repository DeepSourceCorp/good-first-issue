<template>
  <div class="p-4 w-full">

    <!-- Filters -->
    <div class="mb-4 flex gap-4">

      <!-- Stars filter -->
      <select v-model="minStars" class="border p-2 rounded">
        <option value="0">Any stars</option>
        <option value="10">10+ stars</option>
        <option value="50">50+ stars</option>
        <option value="100">100+ stars</option>
        <option value="500">500+ stars</option>
        <option value="1000">1000+ stars</option>
      </select>

      <!-- Last activity filter -->
      <select v-model="months" class="border p-2 rounded">
        <option value="1">Last 1 month</option>
        <option value="3">Last 3 months</option>
        <option value="6">Last 6 months</option>
        <option value="12">Last 1 year</option>
      </select>

    </div>


    <!-- Repo list -->
    <RepoBox
      v-for="repo in filteredRepos"
      :key="repo.id"
      :repo="repo"
    />

    <!-- Empty message -->
    <p v-if="filteredRepos.length === 0">
      No repositories found
    </p>

  </div>
</template>


<script setup>
import { ref, computed } from 'vue'
import Repositories from '~/data/generated.json'


/* filters */
const minStars = ref(0)
const months = ref(12)


/* filtering logic */
const filteredRepos = computed(() => {

  const dateLimit = new Date()
  dateLimit.setMonth(dateLimit.getMonth() - months.value)

  return Repositories.filter(repo => {
    return (
      repo.stars >= minStars.value &&
      new Date(repo.last_modified) >= dateLimit
    )
  })

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
