<template>
  <div class="p-4 w-full">
    <repo-box v-for="repo in repos" :key="repo.id" :repo="repo"></repo-box>
  </div>
</template>

<script>
import RepoBox from '~/components/RepoBox.vue'
import Repositories from '~/data/generated.json'
import dayjs from 'dayjs'

export default {
  components: {
    RepoBox
  },
  computed: {
    repos() {
      const repos = Repositories
      const sortedRepos = repos.sort((a, b) => {
        switch (this.$store.state.activeSortBy) {
          case 'stars': return a.stars < b.stars ? 1 : -1
          case 'activity': return dayjs(a.date_modified).isAfter(b.date_modified) ? 1 : -1
          case 'issues': return a.issues.length < b.issues.length ? 1 : -1
          default: return 1
        }
      })
      return sortedRepos
    }
  }
}
</script>
