export const repoMutations = {
  expandIssue(state, id) {
    if (state.activeIssue === id.toString()) {
      state.activeIssue = ''
    } else {
      state.activeIssue = id.toString()
    }
  }
}
