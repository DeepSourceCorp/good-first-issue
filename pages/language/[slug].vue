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
import Tags from '~/data/tags.json'

const route = useRoute()

const repositories = Repositories.filter(repository => repository.slug === route.params.slug)

const tag = Tags.find(t => t.slug === route.params.slug)

const sortType = ref('none') 

const sortedRepos = computed(() => {
  let list = [...repositories]
  
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
  title: `${tag.language} | Good First Issue`,
  meta: [{
    name: 'description',
    content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
  }]
})
</script>
