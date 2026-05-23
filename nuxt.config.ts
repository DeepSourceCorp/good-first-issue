// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2026-05-23',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', 'nuxt-gtag', 'nuxt-simple-sitemap'],
  nitro: {
    prerender: {
      crawlLinks: true
    }
  },
  site: {
    url: 'https://goodfirstissue.dev'
  }
})