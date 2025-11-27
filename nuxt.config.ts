// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', 'nuxt-gtag', 'nuxt-simple-sitemap'],
  css: ['~/assets/main.css'],
  nitro: {
    prerender: {
      crawlLinks: true
    }
  },
  site: {
    url: 'https://goodfirstissue.dev'
  },
  app: {
    head: {
      title: 'Good First Issue',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Making your first open-source contribution is easier than you think. Good First Issue is a curated list of issues from popular open-source projects that you can easily fix. Start today!' }
      ]
    }
  }
})
