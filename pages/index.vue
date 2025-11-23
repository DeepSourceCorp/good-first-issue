<template>
  <div class="p-4 w-full">

     <button
      @click="toggleTheme"
      class="absolute right-4 top-4 rounded px-3 py-1 border bg-white/80 dark:bg-slate-800/80 dark:text-white"
      :aria-label="theme + ' mode'">
      {{ theme === 'dark' ? '☀️' : '🌙' }}
    </button>

  <RepoBox v-for="repo in Repositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import Repositories from '~/data/generated.json'

useHead({
  title: 'Good First Issue: Make your first open-source contribution',
  meta: [
  {
    name: 'description',
    content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!'
  }
  ]
})

 const theme = ref('light')

function applyTheme(t) {
  const el = document.documentElement
  if (t === 'dark') el.classList.add('dark')
  else el.classList.remove('dark')
  theme.value = t
  try { localStorage.setItem('theme', t) } catch (e) { /* ignore */ }
}

function toggleTheme() {
  applyTheme(theme.value === 'dark' ? 'light' : 'dark')
}

onMounted(() => {
  const saved = typeof localStorage !== 'undefined' ? localStorage.getItem('theme') : null
  if (saved) {
    applyTheme(saved)
    return
  }
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
  applyTheme(prefersDark ? 'dark' : 'light')
})

</script>
