// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', 'nuxt-gtag', '@nuxtjs/sitemap'],

  nitro: {
    prerender: {
      crawlLinks: true
    }
  },
  runtimeConfig: {
    public: {
      siteUrl: 'https://goodfirstissue.dev',
    }
  }
})
