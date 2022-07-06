import { repoMutations } from './mutations/repo'
import { sortingMutations } from './mutations/sorting'

export const state = () => ({
  activeIssue: '',
  activeSortOption: {},
  isOrderByDesc: true
})

export const mutations = {
  ...repoMutations,
  ...sortingMutations
}
