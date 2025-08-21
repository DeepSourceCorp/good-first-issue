<template>
  <div
    :id="`repo-${repo.id}`"
    :class="{
      'border-juniper hover:bg-ink-400 dark:hover:bg-ink-400': isCardOpen,
      'border-ink-200 dark:border-ink-200 border-slate/20': !isCardOpen
    }"
    class="select-none border w-full rounded-md mb-4 cursor-pointer hover:bg-vanilla-300 dark:hover:bg-ink-300 group"
    @click="toggle(repo.id)"
  >
    <div class="px-5 py-3">
      <div class="flex flex-row">
        <a
          :title="`Open ${repo.owner}/${repo.name} on GitHub`"
          :href="repo.url"
          target="_blank"
          rel="noopener noreferrer"
          class="text-lg font-semibold group-hover:text-juniper dark:group-hover:text-juniper"
          :class="{ 'text-juniper': isCardOpen }"
          >{{ repo.owner }} / {{ repo.name }}</a
        >
        <span class="flex-1"></span>
        <span
          class="hidden md:inline text-sm border px-3 py-1 ml-2 rounded-full font-semibold"
          :class="{
            'text-ink-400 bg-juniper border-transparent': isCardOpen,
            'text-ink-400 dark:text-vanilla-200 border-slate/20 dark:border-transparent': !isCardOpen
          }"
          >{{ issuesDisplay }}</span
        >
      </div>
      <div class="flex-row flex text-sm py-1 overflow-auto">
        {{ repo.description }}
      </div>
      <div
        class="flex-row flex text-sm py-1 font-mono"
        :class="{ 'text-honey dark:text-honey': isCardOpen, 'text-slate dark:text-vanilla-400': !isCardOpen }"
      >
        <div class="mr-4"><span class="text-slate/70 dark:text-vanilla-400">lang: </span>{{ repo.language }}</div>
        <div class="mr-4"><span class="text-slate/70 dark:text-vanilla-400">stars: </span>{{ repo.stars_display }}</div>
        <div class="mr-4">
          <span class="text-slate/70 dark:text-vanilla-400">last activity: </span><span>{{ lastModifiedDisplay }}</span>
        </div>
      </div>
    </div>
    <ol v-if="isCardOpen" class="px-5 py-3 text-base leading-loose border-t border-ink-200 dark:border-ink-200">
      <li v-for="issue in repo.issues" :key="issue.url" class="flex flex-row items-start justify-start py-1">
        <span class="text-slate dark:text-slate text-right px-2 leading-snug font-mono" style="min-width: 70px">#{{ issue.number }}</span>
        <div class="flex items-start flex-row flex-auto">
          <a
            title="Open issue on GitHub"
            :href="issue.url"
            target="_blank"
            rel="noopener noreferrer"
            class="leading-snug font-medium hover:text-juniper text-ink-400 dark:text-vanilla-300 block flex-auto"
            >{{ issue.title }}</a
          >
          <div
            v-if="issue.comments_count > 0"
            class="flex flex-row items-center justify-end mt-1 w-10"
            :title="getIssueCommentsCounterTooltip(issue)"
          >
            <ChatBubbleLeftRightIcon class="mt-px w-3.5 h-3.5" />
            <span class="ml-1 text-sm leading-snug font-mono">{{ issue.comments_count }}</span>
          </div>
        </div>
      </li>
    </ol>
  </div>
</template>

<script setup>
import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'
import { ChatBubbleLeftRightIcon } from '@heroicons/vue/24/outline'

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
  return numIssues > 1 ? `${numIssues} issues` : `${numIssues} issue`
})

const lastModifiedDisplay = computed(() => {
  return dayjs(props.repo.last_modified).fromNow()
})

const isCardOpen = computed(() => {
  return openRepoId.value === props.repo.id
})

function toggle(repoId) {
  if (isCardOpen.value) {
    openRepoId.value = null
  } else {
    openRepoId.value = repoId
  }
}

function getIssueCommentsCounterTooltip(issue) {
  const numComments = issue.comments_count
  if (numComments === 0) {
    return `There are no comments on this issue`
  }
  return numComments > 1 ? `There are ${numComments} comments on this issue` : `There is one comment on this issue`
}
</script>
