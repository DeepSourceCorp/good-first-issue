
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', 'nuxt-gtag', 'nuxt-simple-sitemap'],
  compatibilityDate: '2026-02-10;,  
  nitro: {
    prerender: {
      crawlLinks: true
    }
  },
  site: {
    url: 'https://goodfirstissue.dev'
  }
})
