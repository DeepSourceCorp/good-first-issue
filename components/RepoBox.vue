<template>
  <div
    :id="`repo-${repo.id}`"
    :class="{
      'border-juniper hover:bg-ink-400': isCardOpen,
      'border-ink-200': !isCardOpen
    }"
    class="select-none border w-full rounded-md mb-4 cursor-pointer hover:bg-ink-300 group"
    @click="toggle(repo.id)"
  >
    <div class="px-5 py-3">
      <div class="flex flex-row">
        <a
          :title="`Open ${repo.owner}/${repo.name} on GitHub`"
          :href="repo.url"
          target="_blank"
          rel="noopener noreferrer"
          class="text-lg font-semibold group-hover:text-juniper"
          :class="{ 'text-juniper': isCardOpen }"
        >
          {{ repo.owner }} / {{ repo.name }}
        </a>

        <span class="flex-1"></span>

        <span
          class="hidden md:inline text-sm border px-3 py-1 ml-2 rounded-full font-semibold"
          :class="{
            'text-ink-400 bg-juniper border-transparent': isCardOpen,
            'text-vanilla-200': !isCardOpen
          }"
        >
          {{ issuesDisplay }}
        </span>
      </div>

      <div class="flex-row flex text-sm py-1 overflow-auto">
        {{ repo.description }}
      </div>

      <div
        class="flex-row flex text-sm py-1 font-mono"
        :class="{ 'text-honey': isCardOpen, 'text-vanilla-400': !isCardOpen }"
      >
        <div class="mr-4">
          <span class="text-vanilla-400">lang: </span>{{ repo.language }}
        </div>
        <div class="mr-4">
          <span class="text-vanilla-400">stars: </span>{{ repo.stars_display }}
        </div>
        <div class="mr-4">
          <span class="text-vanilla-400">last activity: </span>
          <span>{{ lastModifiedDisplay }}</span>
          <span
            v-if="isFresh"
            class="ml-2 px-2 py-0.5 text-xs rounded-full font-bold text-ink-400 bg-lime-400"
            title="Recently updated repository"
          >
            🟢 Fresh
          </span>
        </div>
      </div>
    </div>

    <ol
      v-if="isCardOpen"
      class="px-5 py-3 text-base leading-loose border-t border-ink-200"
    >
      <li
        v-for="issue in repo.issues"
        :key="issue.url"
        class="flex flex-row items-start py-1"
      >
        <span
          class="text-slate text-right px-2 leading-snug font-mono"
          style="min-width: 70px"
        >
          #{{ issue.number }}
        </span>

        <a
          title="Open issue on GitHub"
          :href="issue.url"
          target="_blank"
          rel="noopener noreferrer"
          class="leading-snug font-medium hover:text-juniper text-vanilla-300 block flex-auto"
        >
          {{ issue.title }}
        </a>
      </li>
    </ol>
  </div>
</template>

<script setup>
import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'

dayjs.extend(relativeTime)

const props = defineProps({
  repo: {
    type: Object,
    required: true
  }
})

const openRepoId = useOpenRepoId()

const issuesDisplay = computed(() => {
  const numIssues = props.repo.issues.length
  return numIssues === 1 ? '1 issue' : `${numIssues} issues`
})

const lastModifiedDisplay = computed(() => {
  return dayjs(props.repo.last_modified).fromNow()
})

const isCardOpen = computed(() => {
  return openRepoId.value === props.repo.id
})

const isFresh = computed(() => {
  const modifiedDate = new Date(props.repo.last_modified)
  const today = new Date()
  const diffDays = (today - modifiedDate) / (1000 * 60 * 60 * 24)
  return diffDays <= 30
})

function toggle(repoId) {
  openRepoId.value = isCardOpen.value ? null : repoId
}
</script>
