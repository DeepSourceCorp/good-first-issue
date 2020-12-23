<template>
  <div
    class="select-none border w-full rounded-md mb-4 cursor-pointer hover:bg-ink-300 group"
    :class="{'border-juniper hover:bg-ink-400': isIssueOpen, 'border-ink-200': !isIssueOpen}"
    :id="`repo-${repo.id}`"
    @click="toggle(repo.id)"
  >
    <div class="px-5 py-3">
      <div class="flex flex-row">
        <a
          :title="`Open ${repo.owner}/${repo.name} on GitHub`"
          :href="repo.url"
          target="_blank"
          class="text-xl font-bold group-hover:text-juniper"
          :class="{'text-juniper': isIssueOpen}"
          >{{ repo.owner }} / {{ repo.name }}</a
        >
        <span class="flex-1"></span>
        <span
          class="hidden md:inline text-sm border px-3 py-1 ml-2 rounded-full font-semibold"
          :class="{'text-ink-400 bg-juniper border-transparent': isIssueOpen, 'text-vanilla-200': !isIssueOpen}"
          >{{ issuesDisplay }}</span>
      </div>
      <div class="flex-row flex text-sm py-1 overflow-auto">
        {{ repo.description }}
      </div>
      <div class="flex-row flex text-sm py-1 font-mono" :class="{'text-honey': isIssueOpen, 'text-vanilla-400': !isIssueOpen}">
        <div class="mr-4">
          <span class="text-green-600">lang: </span>{{ repo.language }}
        </div>
        <div class="mr-4">
          <span class="text-blue-600">stars: </span>{{ repo.stars_display }}
        </div>
        <div class="mr-4">
          <span class="text-red-600">last activity: </span
          ><span>{{ lastModifiedDisplay }}</span>
        </div>
      </div>
    </div>
    <ol
      class="px-5 py-3 text-base leading-loose border-t border-ink-200"
      v-if="isIssueOpen"
    >
      <li class="flex flex-row items-start justify-start py-1" v-for="issue in repo.issues" :key="issue.url">
        <span
          class="text-slate text-right px-2 leading-snug"
          style="min-width: 70px;"
          >#{{ issue.number }}</span
        >
        <a
          title="Open issue on GitHub"
          :href="issue.url"
          target="_blank"
          class="leading-snug font-semibold hover:text-juniper text-vanilla-300"
          >{{ issue.title }}</a
        >
      </li>
    </ol>
  </div>
</template>

<script>
import dayjs from "dayjs"
import relativeTime from "dayjs/plugin/relativeTime"
import { mapMutations } from 'vuex'

dayjs.extend(relativeTime)

export default {
  props: {
    repo: Object
  },
  computed: {
    issuesDisplay: function () {
      const numIssues = this.repo.issues.length
      if (numIssues > 1) {
        return `${numIssues} issues`
      }
      return `${numIssues} issue`
    },
    lastModifiedDisplay: function () {
      return dayjs(this.repo.last_modified).fromNow()
    },
    isIssueOpen: function () {
      return this.$store.state.activeIssue === this.repo.id
    }
  },
  methods: {
    ...mapMutations({
      toggle: 'expandIssue'
    })
  }
}
</script>
