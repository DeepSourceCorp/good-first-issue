import Repositories from '~/data/generated'
import { filter } from 'lodash'
import { getRepoDataBySortOption } from '~/utils/sortUtils'

export const repoGetters = {
  filteredRepos: state => slug => {
    const repositoriesData = slug ? filter(Repositories, { slug }) : Repositories
    const sortOptionPath = state.activeSortOption.pathToValue
    if (sortOptionPath) {
      repositoriesData.sort((a, b) => {
        if (state.isOrderByDesc) {
          return getRepoDataBySortOption(a, sortOptionPath) <
            getRepoDataBySortOption(b, sortOptionPath)
            ? 1
            : -1
        }
        return getRepoDataBySortOption(a, sortOptionPath) >
          getRepoDataBySortOption(b, sortOptionPath)
          ? 1
          : -1
      })
    }
    return repositoriesData
  }
}
