<template>
  <div class="p-4 w-full">
    <repo-box
      v-for="repo in filteredRepos($route.params.slug)"
      :key="repo.id"
      :repo="repo"
    ></repo-box>
  </div>
</template>

<script>
import { includes, map, find } from 'lodash'
import RepoBox from '~/components/RepoBox.vue'
import Tags from '~/data/tags.json'
import { mapState, mapGetters } from 'vuex'

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
    ...mapState(['activeSortOption', 'isOrderByDesc']),
    ...mapGetters(['filteredRepos'])
  }
}
</script>
