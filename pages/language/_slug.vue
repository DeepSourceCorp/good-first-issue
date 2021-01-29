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
  head() {
    return {
      title: `${this.tag.language} · Good First Issue`,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: `Good first issues from popular ${this.tag.language} projects. Get started with your first contribution now!`
        }
      ]
    }
  },
  data: function () {
    return {
      repos: Repositories
    }
  },
  validate({ params }) {
    return includes(map(Tags, 'slug'), params.slug)
  },
  async asyncData({ params }) {
    const repos = filter(Repositories, { slug: params.slug })
    const tag = find(Tags, { slug: params.slug })
    return { repos, tag }
  },
  components: {
    RepoBox
  }
}
</script>
