// Nuxt configuration file
// Documentation: https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  // Enables Nuxt DevTools, which provide debugging and inspection tools during development.
  devtools: { enabled: true },

  // Specifies the Nuxt modules to include in the project.
  modules: [
    '@nuxtjs/tailwindcss',  // Adds Tailwind CSS support for styling.
    'nuxt-gtag',            // Integrates Google Analytics (GTag) for tracking.
    'nuxt-simple-sitemap'   // Automatically generates a sitemap for SEO purposes.
  ],

  // Nitro configuration for server-side rendering (SSR) and static site generation (SSG).
  nitro: {
    prerender: {
      crawlLinks: true  // Enables link crawling to discover pages to prerender during static generation.
    }
  },

  // Configuration for the site's metadata.
  site: {
    url: 'https://goodfirstissue.dev'  // The base URL for the site, used for generating absolute links.
  }
})
