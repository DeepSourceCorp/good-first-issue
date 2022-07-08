<template>
  <div class="p-4 w-full">
    <repo-box v-for="repo in filteredRepos" :key="repo.id" :repo="repo"></repo-box>
  </div>
</template>

<script>
import RepoBox from '~/components/RepoBox.vue'
import Repositories from '~/data/generated.json'
import { mapState } from 'vuex'
import { cloneDeep, get } from 'lodash'

export default {
  components: {
    RepoBox
  },
  computed: {
    ...mapState(['activeSortOption', 'isOrderByDesc']),
    filteredRepos() {
      const repositoriesData = cloneDeep(Repositories)
      if (this.activeSortOption.id) {
        repositoriesData.sort((a, b) => {
          if (this.isOrderByDesc) {
            return this.getRepoDataBySortOption(a) < this.getRepoDataBySortOption(b) ? 1 : -1
          } else {
            return this.getRepoDataBySortOption(a) > this.getRepoDataBySortOption(b) ? 1 : -1
          }
        })
      }
      return repositoriesData
    }
  },
  methods: {
    getRepoDataBySortOption(repo) {
      const sortOptionPath = this.activeSortOption.pathToValue
      const repoValueOfSortOption = get(repo, sortOptionPath)
      if (sortOptionPath === 'issues') {
        return repoValueOfSortOption.length
      } else if (sortOptionPath === 'last_modified') {
        return new Date(repoValueOfSortOption)
      }
      return repoValueOfSortOption
    }
  }
}
</script>
