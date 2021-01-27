<template>
  <div class="p-4 w-full">
    <repo-box v-for="repo in repos" :key="repo.id" :repo="repo"></repo-box>
  </div>
</template>

<script>
import { filter, includes, map, find } from 'lodash'
import RepoBox from '~/components/RepoBox.vue'
import Tags from '~/data/tags.json'
import Repositories from '~/data/generated.json'

export default {
  components: {
    RepoBox
  },
  validate({ params }) {
    return includes(map(Tags, 'slug'), params.slug)
  },
  async asyncData({ params }) {
    const repos = filter(Repositories, { slug: params.slug })
    const tag = find(Tags, { slug: params.slug })
    return { repos, tag }
  },
  data: function () {
    return {
      repos: Repositories
    }
  }
}
</script>
