import { ref, computed } from 'vue'

export function useFilteredRepos(repositories) {
  const searchQuery = ref('')
  const sortOrder = ref('')

  const filteredAndSortedRepos = computed(() => {
    return [...repositories.value]
      .filter(repo => {
        const q = searchQuery.value.toLowerCase()
        return (
          repo.name.toLowerCase().includes(q) ||
          repo.description?.toLowerCase().includes(q) ||
          repo.owner.toLowerCase().includes(q)
        )
      })
      .sort((a, b) => {
        const dateA = new Date(a.last_modified)
        const dateB = new Date(b.last_modified)
        return sortOrder.value === 'newest'
          ? dateB - dateA
          : sortOrder.value === 'oldest'
          ? dateA - dateB
          : 0
      })
  })

  return {
    searchQuery,
    sortOrder,
    filteredAndSortedRepos
  }
}
