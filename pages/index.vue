<template>
  <div class="p-4 w-full">
    <div class="flex flex-wrap gap-2">
      <SortButton 
        :active="sortType === 'stars'" 
        @toggle="toggleSort('stars')"
      >
        {{ sortType === 'stars' ? 'Sorted by Stars' : 'Sort by Stars' }}
      </SortButton>

      <SortButton 
        :active="sortType === 'activity'" 
        @toggle="toggleSort('activity')"
      >
        {{ sortType === 'activity' ? 'Sorted by Last Activity' : 'Sort by Last Activity' }}
      </SortButton>
      
    </div>
    <RepoBox v-for="repo in sortedRepos" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'


const sortType = ref('none') 

const sortedRepos = computed(() => {
  let list = [...Repositories]
  
  if (sortType.value === 'stars') {
    list.sort((a, b) => b.stars - a.stars)
  } else if (sortType.value === 'activity') {
    list.sort((a, b) => new Date(b.last_modified) - new Date(a.last_modified))
  }
  
  return list
})

const toggleSort = (type) => {
  if (sortType.value === type) {
    sortType.value = 'none' 
  } else {
    sortType.value = type 
  }
}


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
