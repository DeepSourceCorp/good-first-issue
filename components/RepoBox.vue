<template>
  <!-- Repository Card -->
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
      <!-- Repo Header -->
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

        <!-- Issue Counter -->
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

      <!-- Repo Description -->
      <div class="flex-row flex text-sm py-1 overflow-auto">
        {{ repo.description }}
      </div>

      <!-- Repo Metadata -->
      <div
        class="flex-row flex text-sm py-1 font-mono"
        :class="{ 'text-honey': isCardOpen, 'text-vanilla-400': !isCardOpen }"
      >
        <div class="mr-4"><span class="text-vanilla-400">lang: </span>{{ repo.language }}</div>
        <div class="mr-4"><span class="text-vanilla-400">stars: </span>{{ repo.stars_display }}</div>
        <div class="mr-4">
          <span class="text-vanilla-400">last activity: </span><span>{{ lastModifiedDisplay }}</span>
        </div>
      </div>
    </div>

    <!-- Repo Issues -->
    <ol v-if="isCardOpen" class="px-5 py-3 text-base leading-loose border-t border-ink-200">
      <li
        v-for="issue in repo.issues"
        :key="issue.url"
        class="flex flex-row items-start justify-start py-1"
      >
        <span
          class="text-slate text-right px-2 leading-snug font-mono"
          style="min-width: 70px"
        >
          #{{ issue.number }}
        </span>

        <div class="flex items-start flex-row flex-auto">
          <a
            title="Open this issue on GitHub"
            :href="issue.url"
            target="_blank"
            rel="noopener noreferrer"
            class="leading-snug font-medium hover:text-juniper text-vanilla-300 block flex-auto"
          >
            {{ issue.title }}
          </a>

          <!-- Issue Comments Count -->
          <div
            v-if="issue.comments_count > 0"
            class="flex flex-row items-center justify-end mt-1 w-10"
            :title="getIssueCommentsCounterTooltip(issue)"
          >
            <ChatBubbleLeftRightIcon class="mt-px w-3.5 h-3.5" />
            <span class="ml-1 text-sm leading-snug font-mono">
              {{ issue.comments_count }}
            </span>
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

// Shared store for open repository state
const openRepoId = useOpenRepoId()

// Display number of issues (pluralization handled)
const issuesDisplay = computed(() => {
  const issueCount = props.repo.issues.length
  return issueCount > 1 ? `${issueCount} issues` : `${issueCount} issue`
})

// Show relative time since last modification
const lastModifiedDisplay = computed(() => {
  return dayjs(props.repo.last_modified).fromNow()
})

// Check if this card is currently open
const isCardOpen = computed(() => openRepoId.value === props.repo.id)

// Toggle open/close state of a repo card
function toggle(repoId) {
  openRepoId.value = isCardOpen.value ? null : repoId
}

// Tooltip for issue comment count
function getIssueCommentsCounterTooltip(issue) {
  const count = issue.comments_count
  if (count === 0) return `There are no comments on this issue`
  return count > 1
    ? `There are ${count} comments on this issue`
    : `There is one comment on this issue`
}
</script>
