<template>
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center flex-wrap">
      <nuxt-link to="/" class="flex items-center text-gray-700 font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
      </nuxt-link>
      <span v-if="activeTag" class="text-2xl cursor-pointer">
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
    </nav>
  </header>
</template>

<script>
import { find } from 'lodash'
import Tags from '~/data/tags.json'

export default {
  props: {
    tag: {
      type: Object,
      required: true
    }
  },
  computed: {
    activeTag: function () {
      return find(Tags, { slug: this.$route.params.slug })
    }
  }
}
</script>
