import { ref, computed, onMounted } from 'vue'

const STORAGE_KEY = 'gfi-theme'

const theme = ref('dark')

function applyTheme(t) {
  if (process.client) {
    document.documentElement.classList.toggle('light', t === 'light')
    document.documentElement.classList.toggle('dark', t === 'dark')
  }
}

export default function useTheme() {
  function setTheme(t) {
    theme.value = t
    try { localStorage.setItem(STORAGE_KEY, t) } catch (e) {}
    applyTheme(t)
  }

  function toggle() {
    setTheme(theme.value === 'dark' ? 'light' : 'dark')
  }

  const isDark = computed(() => theme.value === 'dark')

  onMounted(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY)
      if (saved === 'light' || saved === 'dark') {
        theme.value = saved
      } else {
        theme.value = 'dark'
      }
    } catch (e) {
      theme.value = 'dark'
    }
    applyTheme(theme.value)
  })

  return { theme, setTheme, toggle, isDark }
}
