export const useRepositorySearch = (repositories) => {
  const searchQuery = ref('')
  const filteredRepositories = ref(repositories)

  const handleSearch = (query) => {
    if (!query || query.trim() === '') {
      filteredRepositories.value = repositories
      return
    }

    const lowerQuery = query.toLowerCase()
    filteredRepositories.value = repositories.filter(repo => {
      return (
        repo.name.toLowerCase().includes(lowerQuery) ||
        repo.owner.toLowerCase().includes(lowerQuery) ||
        repo.description.toLowerCase().includes(lowerQuery) ||
        (repo.language && repo.language.toLowerCase().includes(lowerQuery))
      )
    })
  }

  const handleClear = () => {
    searchQuery.value = ''
    filteredRepositories.value = repositories
  }

  return {
    searchQuery,
    filteredRepositories,
    handleSearch,
    handleClear
  }
}
