<template>
  <header class="w-full py-4 border-b border-ink-200 bg-ink-400">
    <nav class="flex items-center justify-center md:justify-start flex-wrap max-w-6xl mx-auto px-6">
      <nuxt-link to="/" class="flex items-center text-gray-700 font-bold">
        <img src="~/assets/gfi-logo-white.svg" alt="Good First Issue" class="h-12" />
      </nuxt-link>
      <span class="text-2xl cursor-pointer hidden md:inline-block" v-if="activeTag">
        <span class="font-normal ml-2 mr-1 text-slate">/</span>
        <span class="font-semibold text-juniper">{{ activeTag.language }}</span>
      </span>
      <ul class="hidden md:flex flex-auto justify-center md:justify-end flex-row gap-4">
        <li>
          <nuxt-link to="/guide">Guide</nuxt-link>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
import { find } from 'lodash'
import Tags from '~/data/tags.json'

export default {
  props: {
    tag: Object
  },
  computed: {
    activeTag: function () {
      return find(Tags, { slug: this.$route.params.slug })
    }
  }
}
</script>
