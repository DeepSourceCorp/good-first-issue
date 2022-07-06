export const sortingMutations = {
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
