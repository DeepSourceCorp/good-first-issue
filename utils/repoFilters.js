function getTimestamp(value) {
  const timestamp = new Date(value).getTime()
  return Number.isNaN(timestamp) ? 0 : timestamp
}

function getThresholdDate(now, months) {
  const threshold = new Date(now)
  threshold.setMonth(threshold.getMonth() - months)
  return threshold
}

export function filterAndSortRepositories(repositories, options = {}) {
  const {
    slug,
    minStars = 0,
    activityMonths = 0,
    now = new Date()
  } = options

  const thresholdDate = activityMonths > 0 ? getThresholdDate(now, activityMonths) : null

  return repositories
    .filter(repository => !slug || repository.slug === slug)
    .filter(repository => repository.stars >= minStars)
    .filter(repository => {
      if (!thresholdDate) {
        return true
      }
      const lastModifiedDate = new Date(repository.last_modified)
      if (Number.isNaN(lastModifiedDate.getTime())) {
        return false
      }
      return lastModifiedDate >= thresholdDate
    })
    .sort((a, b) => {
      if (b.stars !== a.stars) {
        return b.stars - a.stars
      }
      return getTimestamp(b.last_modified) - getTimestamp(a.last_modified)
    })
}
