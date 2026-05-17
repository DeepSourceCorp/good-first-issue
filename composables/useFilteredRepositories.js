import dayjs from 'dayjs'

export const useFilteredRepositories = (repositoriesRef) => {
  const minStars = useMinStars()
  const lastActivity = useLastActivity()

  return computed(() => {
    const repos = unref(repositoriesRef)
    // Create a copy of the array before sorting, as sort mutates in place
    return [...repos].filter(repo => {
      if (minStars.value > 0 && repo.stars < minStars.value) {
        return false
      }
      if (lastActivity.value > 0) {
        const monthsAgo = dayjs().diff(dayjs(repo.last_modified), 'month')
        if (monthsAgo > lastActivity.value) {
          return false
        }
      }
      return true
    }).sort((a, b) => {
      if (minStars.value > 0 && lastActivity.value === 0) {
        return b.stars - a.stars
      } else if (lastActivity.value > 0 && minStars.value === 0) {
        return dayjs(b.last_modified).valueOf() - dayjs(a.last_modified).valueOf()
      } else if (minStars.value > 0 && lastActivity.value > 0) {
        const timeDiff = dayjs(b.last_modified).valueOf() - dayjs(a.last_modified).valueOf()
        if (timeDiff !== 0) return timeDiff
        return b.stars - a.stars
      }
      return 0
    })
  })
}
