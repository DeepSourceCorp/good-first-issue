<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

const selectedTags = useState('selectedTags')

const filteredRepositories = computed(() => {
  if (!selectedTags.value.length) return Repositories
  
  return Repositories.filter(repo => {
    if (repo.language && selectedTags.value.includes(repo.language.toLowerCase())) {
      return true
    }
    
    if (repo.languages) {
      return Object.keys(repo.languages).some(lang => 
        selectedTags.value.includes(lang.toLowerCase())
      )
    }
    
    return false
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
