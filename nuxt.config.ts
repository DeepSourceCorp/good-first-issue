export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', 'nuxt-gtag'],

  nitro: {
    prerender: {
      crawlLinks: true
    }
  },

  compatibilityDate: '2025-03-22'
})