import { sortingMutations } from './mutations/sorting'

export const state = () => ({
  activeIssue: '',
  activeSortOption: {},
  isOrderByDesc: true
})

export const mutations = {
  expandIssue(state, id) {
    if (state.activeIssue === id.toString()) {
      state.activeIssue = ''
    } else {
      state.activeIssue = id.toString()
    }
  },
  ...sortingMutations
}
