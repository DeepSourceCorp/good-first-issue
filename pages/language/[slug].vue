<template>
  <div class="p-4 w-full">

    <!-- ✅ Added summary -->
    <div v-if="isFiltered" class="mb-4 text-sm text-vanilla-400">
      Showing {{ filteredRepositories.length }} of {{ totalCount }} repositories
    </div>

    <!-- ✅ Added sorting -->
    <div class="mb-4">
      <button @click="sortBy = 'default'">Default</button>
      <button @click="sortBy = 'stars'">⭐ Stars</button>
      <button @click="sortBy = 'activity'">🕐 Activity</button>
    </div>

    <!-- ✅ replaced repositories with filteredRepositories -->
    <RepoBox
      v-for="repo in filteredRepositories"
      :key="repo.id"
      :repo="repo"
    />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'
import dayjs from 'dayjs'
import isBefore from 'dayjs/plugin/isBefore'

dayjs.extend(isBefore)

const route = useRoute()

const minStars = useMinStars()
const maxMonths = useMaxMonths()
const sortBy = ref('default')

const allRepos = Repositories.filter(
  repository => repository.slug === route.params.slug
)

const totalCount = allRepos.length

const isFiltered = computed(() =>
  minStars.value > 0 || maxMonths.value > 0
)

const filteredRepositories = computed(() => {
  let result = allRepos.filter(repo => {
    if (minStars.value > 0 && repo.stars < minStars.value) return false

    if (maxMonths.value > 0) {
      const cutoff = dayjs().subtract(maxMonths.value, 'month')
      if (dayjs(repo.last_modified).isBefore(cutoff)) return false
    }

    return true
  })

  if (sortBy.value === 'stars') {
    result = [...result].sort((a, b) => b.stars - a.stars)
  } else if (sortBy.value === 'activity') {
    result = [...result].sort(
      (a, b) =>
        dayjs(b.last_modified).valueOf() -
        dayjs(a.last_modified).valueOf()
    )
  }

  return result
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