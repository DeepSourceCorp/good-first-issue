<template>
  <div>
    <section class="container max-w-6xl mx-auto px-6 py-6 flex flex-col gap-y-6">
      <div class="text-3xl font-bold text-vanilla-100 mt-6">{{ article.title }}</div>
      <nuxt-content class="prose prose-xl text-vanilla-200" :document="article" />
    </section>
  </div>
</template>

<script>
export default {
  layout: 'content',
  head () {
    return {
      title: `${this.article.title} · Good First Issue`,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.article.description
        }
      ]
    }
  },
  async asyncData({ $content, params }) {
    const article = await $content('guide', params.slug).fetch()
    return {
      article
    }
  }
}
</script>
