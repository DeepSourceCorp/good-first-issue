<template>
  <div class="p-4 w-full">
    <repo-box v-for="repo in filteredRepos()" :key="repo.id" :repo="repo"></repo-box>
  </div>
</template>

<script>
import RepoBox from '~/components/RepoBox.vue'
import { mapState, mapGetters } from 'vuex'

export default {
  components: {
    RepoBox
  },
  computed: {
    ...mapState(['activeSortOption', 'isOrderByDesc']),
    ...mapGetters(['filteredRepos'])
  }
}
</script>
