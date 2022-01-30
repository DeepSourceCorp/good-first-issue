<template>
  <div class="p-4 w-full">
    <repo-box v-for="repo in repos" :key="repo.id" :repo="repo"></repo-box>
  </div>
</template>

<script>
import { filter, includes, map, find } from 'lodash'
import RepoBox from '~/components/RepoBox.vue'
import Tags from '~/data/tags.json'
import Repositories from '~/data/generated.json'
import dayjs from 'dayjs'

export default {
  components: {
    RepoBox
  },
  validate({ params }) {
    return includes(map(Tags, 'slug'), params.slug)
  },
  async asyncData({ params }) {
    const tag = find(Tags, { slug: params.slug })
    return { tag }
  },
  computed: {
    repos() {
      const repos = filter(Repositories, { slug: this.tag.slug })
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
