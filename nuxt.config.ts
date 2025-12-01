// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/color-mode',
    'nuxt-gtag',
    'nuxt-simple-sitemap'
  ],
  colorMode: {
    classSuffix: '',
    preference: 'system',
    fallback: 'dark'
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
