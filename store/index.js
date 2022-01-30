export const state = () => ({
  activeIssue: '',
  activeSortBy: ''
})

export const mutations = {
  expandIssue(state, id) {
    if (state.activeIssue === id.toString()) {
      state.activeIssue = ''
    } else {
      state.activeIssue = id.toString()
    }
  },
  setActiveSortBy(state, sortBy) {
    if (state.activeSortBy === sortBy) {
      state.activeSortBy = ''
    } else {
      state.activeSortBy = sortBy
    }
  }
}
