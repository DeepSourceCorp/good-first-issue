import { filter } from 'lodash'
import { getRepoDataBySortOption } from '~/utils/sortUtils'
import Repositories from '~/data/generated.json'

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
        } else {
          return getRepoDataBySortOption(a, sortOptionPath) >
            getRepoDataBySortOption(b, sortOptionPath)
            ? 1
            : -1
        }
      })
    }
    return repositoriesData
  }
}
