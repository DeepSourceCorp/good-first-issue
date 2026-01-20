// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  compatibilityDate: '2026-01-20',

  modules: [
    '@nuxtjs/tailwindcss',
    'nuxt-gtag',
    '@nuxtjs/color-mode'
  ],

  colorMode: {
    preference: 'system',
    fallback: 'light',
    classSuffix: '',
    storageKey: 'color-mode'
  },

  nitro: {
    prerender: {
      crawlLinks: true
    }
  },

  site: {
    url: 'https://goodfirstissue.dev'
  }
})
