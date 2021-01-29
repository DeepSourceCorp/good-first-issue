<template>
  <div>
    <section class="container max-w-6xl mx-auto px-6 py-6 flex flex-col gap-y-6">
      <nuxt-link :to="article.path" v-for="article of articles" :key="article.slug">
        <div class="py-6 article group border-ink-200 border rounded-md px-6 hover:bg-ink-300">
          <div class="text-2xl mb-1 font-semibold text-vanilla-200 group-hover:text-juniper">
            {{ article.title }}
          </div>
          <div
            v-if="article.description"
            class="text-base text-vanilla-300 group-hover:text-vanilla-100"
          >
            {{ article.description }}
          </div>
        </div>
      </nuxt-link>
    </section>
  </div>
</template>

<script>
export default {
  layout: 'content',
  async asyncData({ $content, params }) {
    const articles = await $content('guide')
      .only(['title', 'description'])
      .sortBy('createdAt', 'desc')
      .fetch()

    return {
      articles
    }
  }
}
</script>
