import dayjs from 'dayjs'

/*
  Composable that returns a computed list of repositories filtered by
  the shared minStars / activityFilter state and optionally sorted by
  relevance (stars descending, then most-recently-active first).
 
  @param {import('vue').Ref<Array>|Array} sourceRepos – the raw repo list (or ref)
 */
export const useFilteredRepos = (sourceRepos) => {
  const minStars = useMinStars()
  const activityFilter = useActivityFilter()

  const activityCutoff = computed(() => {
    switch (activityFilter.value) {
      case '1m':
        return dayjs().subtract(1, 'month')
      case '6m':
        return dayjs().subtract(6, 'month')
      case '1y':
        return dayjs().subtract(1, 'year')
      default:
        return null // "all" — no cutoff
    }
  })

  const filteredRepos = computed(() => {
    const repos = Array.isArray(sourceRepos) ? sourceRepos : sourceRepos.value
    const cutoff = activityCutoff.value
    const stars = minStars.value

    let result = repos

    // Filter by minimum stars
    if (stars > 0) {
      result = result.filter((r) => r.stars >= stars)
    }

    // Filter by last activity date
    if (cutoff) {
      result = result.filter((r) => dayjs(r.last_modified).isAfter(cutoff))
    }

    // Sort: most stars first, then most-recently-active first
    result = [...result].sort((a, b) => {
      if (b.stars !== a.stars) return b.stars - a.stars
      return dayjs(b.last_modified).unix() - dayjs(a.last_modified).unix()
    })

    return result
  })

  return filteredRepos
}
