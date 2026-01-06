// https://nuxt.com/docs/api/configuration/nuxt-config
const isProd = process.env.NODE_ENV === 'production'

export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    'nuxt-gtag',
    // nuxt-simple-sitemap should only run where Nitro can handle it safely
    ...(isProd ? ['nuxt-simple-sitemap'] : [])
  ],
  nitro: {
    compatibilityDate: '2026-01-05',
    prerender: {
      crawlLinks: true
    }
  },
  site: {
    url: 'https://goodfirstissue.dev'
  }
})
