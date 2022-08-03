export const sortingMutations = {
  handleActiveSortOptionToggle(state, sortOption) {
    if (JSON.stringify(state.activeSortOption) === JSON.stringify(sortOption)) {
      state.activeSortOption = {}
    } else {
      state.activeSortOption = sortOption
    }
  },
  handleOrderByToggle(state, isOrderByDesc) {
    state.isOrderByDesc = isOrderByDesc
  }
}
