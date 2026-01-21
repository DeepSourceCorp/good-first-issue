<template>
  <div class="p-4 w-full">
    <input
      v-model="searchQuery"
      type="text"
      placeholder="Search projects..."
      class="mb-4 px-3 py-2 rounded border border-ink-200 w-full bg-ink-400 text-vanilla-100 text-sm placeholder:text-vanilla-400"
    />

    <div class="mb-4">
      <div class="inline-flex items-center border border-ink-200 bg-ink-400 text-vanilla-100 rounded px-3 py-1 text-sm">
        <label for="sortOrder" class="mr-2 text-slate font-semibold">Sort by:</label>
        <select
          v-model="sortOrder"
          id="sortOrder"
          class="bg-ink-400 text-vanilla-100 font-semibold border-none outline-none cursor-pointer"
        >
          <option value="">Best match</option>
          <option value="newest">Newest</option>
          <option value="oldest">Oldest</option>
        </select>
      </div>
    </div>

    <RepoBox
      v-for="repo in filteredAndSortedRepos"
      :key="repo.id"
      :repo="repo"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useFilteredRepos } from '~/composables/useFilteredRepos'
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const filteredRepos = ref(
  Repositories.filter(repo => repo.slug === route.params.slug)
)

const {
  searchQuery,
  sortOrder,
  filteredAndSortedRepos
} = useFilteredRepos(filteredRepos)

const tag = Tags.find(t => t.slug === route.params.slug)

useHead({
  title: `${tag.language} | Good First Issue`,
  meta: [
    {
      name: 'description',
      content: `Curated list of issues in ${tag.language} from popular open-source projects that you can easily fix.`
    }
  ]
})
</script>
