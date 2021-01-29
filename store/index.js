export const state = () => ({
  activeIssue: '',
  sectionName: ''
})

export const mutations = {
  expandIssue(state, id) {
    if (state.activeIssue === id.toString()) {
      state.activeIssue = ''
    } else {
      state.activeIssue = id.toString()
    }
  },
  setSectionName(state, name) {
    state.sectionName = name
  },
  clearSectionName(state) {
    state.sectionName = ''
  }
}
