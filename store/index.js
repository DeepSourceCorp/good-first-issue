export const state = () => ({
  activeIssue: ''
})

export const mutations = {
  expandIssue(state, id) {
    if (state.activeIssue === id.toString()) {
      state.activeIssue = ''
    } else {
      state.activeIssue = id.toString()
    }
  }
}
