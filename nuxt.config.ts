// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', 'nuxt-gtag', 'nuxt-simple-sitemap'],
  nitro: {
    prerender: {
      crawlLinks: true
    }
  },
  site: {
    url: 'https://goodfirstissue.dev' ,
    compatibilityDate: '2026-01-08'
  }
})
