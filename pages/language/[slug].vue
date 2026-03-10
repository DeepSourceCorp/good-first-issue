<template>
  <div class="flex flex-col md:flex-row gap-6 p-4 w-full">
    <aside class="w-full md:w-64 flex-shrink-0">
      <div class="sticky top-4 flex flex-col gap-6 p-4 bg-ink-400 rounded-lg border border-ink-200">
        <h3 class="text-juniper font-bold uppercase text-xs tracking-widest">Filter {{ tag?.language }}</h3>

        <div class="flex flex-col gap-2">
          <label class="text-vanilla-400 text-sm font-mono uppercase italic">Min Stars</label>
          <select
            v-model="minStars"
            class="bg-ink-300 text-vanilla-100 border border-ink-100 rounded px-3 py-2 outline-none focus:border-juniper cursor-pointer"
          >
            <option :value="0">Any stars</option>
            <option :value="100">100+</option>
            <option :value="500">500+</option>
            <option :value="1000">1k+</option>
            <option :value="5000">5k+</option>
            <option :value="5000">10k+</option>
            <option :value="5000">20k+</option>
            <option :value="5000">50k+</option>
            <option :value="5000">100k+</option>
          </select>
        </div>

        <div class="flex flex-col gap-2">
          <label class="text-vanilla-400 text-sm font-mono uppercase italic">Last Activity</label>
          <select
            v-model="activityRange"
            class="bg-ink-300 text-vanilla-100 border border-ink-100 rounded px-3 py-2 outline-none focus:border-juniper cursor-pointer"
          >
            <option :value="10000">All Time</option>
            <option :value="30">Past Month</option>
            <option :value="180">Past 6 Months</option>
            <option :value="365">Past Year</option>
            <option :value="730">Past 2 Years</option>
            <option :value="1825">Past 5 Years</option>
            <option :value="3650">Past 10 Years</option>
            <option :value="7300">Past 20 Years</option>
          </select>
        </div>

        <div class="pt-4 border-t border-ink-100 text-slate text-xs font-mono">
          Found: {{ filteredRepositories.length }}
        </div>
      </div>
    </aside>

    <main class="flex-1">
      <div v-if="filteredRepositories.length > 0">
        <RepoBox v-for="repo in filteredRepositories" :key="repo.id" :repo="repo" />
      </div>
      <div v-else class="text-center py-20 bg-ink-400 rounded-lg border border-dashed border-ink-100">
        <p class="text-vanilla-400 font-mono">No projects match these criteria.</p>
        <button @click="resetFilters" class="mt-4 text-juniper underline text-sm">Reset Filters</button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import dayjs from 'dayjs'
import Repositories from '~/data/generated.json'
import Tags from '~/data/tags.json'

const route = useRoute()

const minStars = ref(0)
const activityRange = ref(100000)

const filteredRepositories = computed(() => {
  return Repositories.filter((repo) => {
    const matchSlug = repo.slug === route.params.slug

    const matchStars = repo.stars >= minStars.value

    const lastAcitivity = dayjs(repo.last_modified)
    const deadline = dayjs().subtract(activityRange.value, 'days')
    const matchAcitity = lastAcitivity.isAfter(deadline)

    return matchSlug && matchStars && matchAcitity
  })
})

function resetFilters() {
  minStars.value = 0
  activityRange.value = 100000
}

const tag = Tags.find((t) => t.slug === route.params.slug)

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
