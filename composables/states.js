export const useOpenRepoId = () => useState('openRepoId', () => null)

export const useTheme = () => {
  const theme = useState('theme', () => {
    if (process.client) {
      const savedTheme = localStorage.getItem('theme')
      return savedTheme || 'dark'
    }
    return 'dark'
  })

  watch(theme, (newTheme) => {
    if (process.client) {
      localStorage.setItem('theme', newTheme)
    }
  })

  return theme
}