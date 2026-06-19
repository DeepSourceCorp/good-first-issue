function getRepositoryStars(repository) {
  const stars = Number(repository?.stars)

  return Number.isFinite(stars) ? stars : 0
}

function getRepositoryLastModified(repository) {
  if (!repository?.last_modified) {
    return null
  }

  const timestamp = new Date(repository?.last_modified).getTime()

  return Number.isFinite(timestamp) ? timestamp : null
}

function getActivityCutoff(activityMonths) {
  if (activityMonths === 'all' || activityMonths === null || activityMonths === undefined) {
    return null
  }

  const months = Number(activityMonths)

  if (!Number.isFinite(months) || months <= 0) {
    return null
  }

  const cutoff = new Date()
  cutoff.setMonth(cutoff.getMonth() - months)

  return cutoff.getTime()
}

export function filterAndSortRepositories(repositories, { slug, minStars = 0, activityMonths = 'all' } = {}) {
  if (!Array.isArray(repositories)) {
    return []
  }

  const minimumStars = Number(minStars)
  const activeMinimumStars = Number.isFinite(minimumStars) && minimumStars > 0 ? minimumStars : 0
  const activityCutoff = getActivityCutoff(activityMonths)
  const hasActivityFilter = activityCutoff !== null
  const hasLanguageFilter = Boolean(slug)

  const filteredRepositories = repositories
    .map((repository, index) => ({
      repository,
      index,
      stars: getRepositoryStars(repository),
      lastModified: getRepositoryLastModified(repository)
    }))
    .filter(({ repository, stars, lastModified }) => {
      if (hasLanguageFilter && repository?.slug !== slug) {
        return false
      }

      if (stars < activeMinimumStars) {
        return false
      }

      if (hasActivityFilter) {
        return lastModified !== null && lastModified >= activityCutoff
      }

      return true
    })

  if (activeMinimumStars === 0 && !hasActivityFilter) {
    return filteredRepositories.map(({ repository }) => repository)
  }

  return filteredRepositories
    .sort((firstRepository, secondRepository) => {
      if (activeMinimumStars > 0) {
        const starsDifference = firstRepository.stars - secondRepository.stars

        if (starsDifference !== 0) {
          return starsDifference
        }
      }

      if (hasActivityFilter) {
        const firstLastModified = firstRepository.lastModified ?? Number.NEGATIVE_INFINITY
        const secondLastModified = secondRepository.lastModified ?? Number.NEGATIVE_INFINITY
        const activityDifference = secondLastModified - firstLastModified

        if (activityDifference !== 0) {
          return activityDifference
        }
      }

      return firstRepository.index - secondRepository.index
    })
    .map(({ repository }) => repository)
}
