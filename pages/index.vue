<template>
  <div class="p-4 w-full">
    <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import allRepositories from '~/data/generated.json'
import { useSelectedTags } from '~/composables/states'
import RepoBox from '~/components/RepoBox.vue'

const { value: selectedTags } = useSelectedTags()

const filteredRepositories = computed(() => {
  if (!selectedTags || selectedTags.length === 0) return allRepositories

  return allRepositories.filter((repo) => selectedTags.every((tag) => repo.tags?.includes(tag)))
})
</script>
