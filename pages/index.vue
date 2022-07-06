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
      const getRepoDataBySortOption = repo => {
        const sortOptionPath = this.activeSortOption.pathToValue
        const repoValueOfSortOption = get(repo, sortOptionPath)
        if (sortOptionPath === 'stars') {
          return repoValueOfSortOption
        } else if (sortOptionPath === 'issues') {
          return repoValueOfSortOption.length
        } else if (sortOptionPath === 'last_modified') {
          return new Date(repoValueOfSortOption)
        }
      }
      if (this.activeSortOption.id) {
        repositoriesData.sort((a, b) => {
          if (this.isOrderByDesc) {
            return getRepoDataBySortOption(a) < getRepoDataBySortOption(b) ? 1 : -1
          } else {
            return getRepoDataBySortOption(a) > getRepoDataBySortOption(b) ? 1 : -1
          }
        })
      }
      return repositoriesData
    }
  }
}
</script>
