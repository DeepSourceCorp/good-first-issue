import { get } from 'lodash'
export const getRepoDataBySortOption = (repo, sortOptionPath) => {
  const repoValueOfSortOption = get(repo, sortOptionPath)
  if (sortOptionPath === 'issues') {
    return repoValueOfSortOption.length
  } else if (sortOptionPath === 'last_modified') {
    return new Date(repoValueOfSortOption)
  }
  return repoValueOfSortOption
}
