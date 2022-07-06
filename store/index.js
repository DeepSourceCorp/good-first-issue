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
  handleActiveSortOptionToggle(state, sortOption) {
    if (state.activeSortOption === sortOption) {
      state.activeSortOption = {}
    } else {
      state.activeSortOption = sortOption
    }
  },
  handleOrderByToggle(state, isOrderByDesc) {
    state.isOrderByDesc = isOrderByDesc
  }
}
